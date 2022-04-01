from mesa import Model
from mesa.time import SimultaneousActivation
from mesa.space import Grid
from mesa.datacollection import DataCollector
import numpy as np

from .cell import *

def get_owners(model): # informacoes gerais dos agentes
    dc = {}
    for (contents, x, y) in model.grid.coord_iter():
        if contents.owner == -1:
            continue
        try:
            dc[contents.owner]
        except:
            dc[contents.owner] = 1
    return len(dc)

def local_variety(model):
    ls = [0 for _ in range(2500)]
    cnt = 0
    for (contents, x, y) in model.grid.coord_iter():
        for neigh in contents.neighbors:
            if neigh.owner == -1 or neigh.owner == contents.owner:
                continue
            ls[cnt]+=1
        cnt += 1
    if len(ls) == 0:
        return 0
    rs = sum(ls)/len(ls)
    return math.sqrt(sum((x-rs)**2 for x in ls)/len(ls))

def group_size(model):
    ls = {}
    for (contents, x, y) in model.grid.coord_iter():
        if contents.owner == -1:
            continue
        try:
            ls[contents.owner] += 1
        except:
            ls[contents.owner] = 1
    if len(ls) == 0:
        return 0
    rs = sum(ls.values())/len(ls)
    return math.sqrt(sum((x-rs)**2 for x in ls.values())/len(ls))

class ConwaysGameOfLife(Model):
    """
    Represents the 2-dimensional array of cells in Conway's
    Game of Life.
    """

    def __init__(self, width=50, height=50, initial_chance=0.1, ambition_ceil=0.1, opinion_ceil=0.1, polarization = 1):
        """
        Create a new playing area of (width, height) cells.
        """

        # Set up the grid and schedule.

        # Use SimultaneousActivation which simulates all the cells
        # computing their next state simultaneously.  This needs to
        # be done because each cell's next state depends on the current
        # state of all its neighbors -- before they've changed.
        self.schedule = SimultaneousActivation(self)

        # Use a simple grid, where edges wrap around.
        self.grid = Grid(width, height, torus=True)
        self.datacollector = DataCollector(
            model_reporters={
                'Ideologies Quantity': get_owners,
                'Local Variety Index': local_variety,
                'Group Size Index': group_size
            }
        )
        # Place a cell at each location, with some initialized to
        # ALIVE and some to DEAD.
        cnt =0
        Cell.polarization = polarization
        for (contents, x, y) in self.grid.coord_iter():
            cnt += 1
            cell = Cell((x, y), self, ambition_ceil=ambition_ceil, opinion_ceil=opinion_ceil)
            if self.random.random() < initial_chance:
                cell.state = cell.ALIVE
                cell.owner = Cell.ID
                Cell.colors[cell.owner] = gen_color()
                Cell.ID += 1
            self.grid.place_agent(cell, (x, y))
            self.schedule.add(cell)
        self.running = True

    def step(self):
        """
        Have the scheduler advance each cell by one step
        """
        self.datacollector.collect(self)
        self.schedule.step()