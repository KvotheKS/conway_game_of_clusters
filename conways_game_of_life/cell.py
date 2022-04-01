from mesa import Agent
import random
import math

def gen_color():
    r,g,b = random.randint(0,255),random.randint(0,255),random.randint(0,255)
    return f'rgba({r},{g},{b},0.5)'

def change_stances(cell):
    dc = {}
    cnt = 0
    for i in cell.neighbors:
        if i.owner == -1:
            continue

        cnt += 1
        
        if i.owner == cell.owner:
            continue
        
        try:
            dc[i.owner] += 1
        except:
            dc[i.owner] = 1
    rs = Cell.polarization/2 if cell.isLeader else 1
    rs = cell.random.random()*cnt*Cell.polarization*rs
    cnt = 0
    for i in dc.items():
        if cnt + i[1] >= rs:
            cell._nextOwner = i[0]

class Cell(Agent):
    """Represents a single ALIVE or DEAD cell in the simulation."""

    DEAD = 0 # is not associated with any group
    ALIVE = 1 # is associated with a group
    polarization = 1
    colors = {}
    ID = 0

    def __init__(self, pos, model, init_state=DEAD, ambition_ceil=0.1, opinion_ceil=0.1):
        """
        Create a cell, in the given state, at the given x, y position.
        """
        super().__init__(pos, model)
        self.x, self.y = pos
        self.state = init_state
        self._nextState = None
        self._nextOwner = None
        self.timeAlive = 0
        self.isLeader = False
        self.owner = -1 # self.owner esta relacionado ao pensamento
        self.ambitions = ambition_ceil
        self.change_opinions = opinion_ceil
    
    @property
    def isAlive(self):
        return self.state == self.ALIVE

    @property
    def neighbors(self):
        return self.model.grid.iter_neighbors((self.x, self.y), True)

    def step(self):
        live_neighbors = sum(neighbor.isAlive for neighbor in self.neighbors)

        # Assume nextState is unchanged, unless changed below.
        self._nextState = self.state
        self._nextOwner = self.owner

        if self.isAlive:
            self.timeAlive += 1
            if self.random.random() < self.change_opinions:     
                if self.random.random()*100 <= 1: #celula decide desistir de "politica"
                    self._nextState = self.DEAD
                    self._nextOwner = -1
                    
                    if self.isLeader:
                        self.isLeader = False
                else:
                    change_stances(self)
            elif not self.isLeader and self.random.random() < self.ambitions:
                self.isLeader = True
                if self.owner == -1:
                    self._nextOwner = Cell.ID
                    Cell.ID += 1

        elif self.random.random() < self.change_opinions:
            self.timeAlive = 0
            if len([x for x in self.neighbors if x.owner != -1]) != 0:
                dc = {}
                res, act = 0, 0
                
                for i in [x for x in self.neighbors if x.isAlive]:
                    try:
                        dc[i.owner] += 1
                    except:
                        dc[i.owner] = 1
                    res += 1

                self._nextState = self.state
                self._nextOwner = self.owner

                res = random.randint(0,res)
                for i in dc.items():
                    
                    if res <= act + i[1]:
                        self._nextState = self.ALIVE
                        self._nextOwner = i[0]
                        break
                    act += i[1]
            else:
                self._nextState = self.ALIVE
                self._nextOwner = -1

    def advance(self):
        """
        Set the state to the new computed state -- computed in step().
        """
        self.state = self._nextState
        self.owner = self._nextOwner
        self.check_dicts()
        
    def check_dicts(self):
        if self.owner != None:
            try:
                Cell.colors[self.owner]
            except:
                Cell.colors[self.owner] = gen_color()