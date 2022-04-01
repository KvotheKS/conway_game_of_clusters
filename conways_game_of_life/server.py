
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter

from .portrayal import portrayCell
from .model import ConwaysGameOfLife
from mesa.visualization.modules import ChartModule

# Make a world that is 50x50, on a 250x250 display.
canvas_element = CanvasGrid(portrayCell, 50, 50, 250, 250)
owner_map = ChartModule(
    [
        {"Label": "Ideologies Quantity", "Color": "#FF3C33"}    
    ]
)
variety_map = ChartModule(
    [
        {"Label": "Local Variety Index", "Color": "#3CFF33"}    
    ]
)

group_map = ChartModule(
    [
        {"Label": "Group Size Index", "Color": "#3C33FF"}    
    ]
)

server = ModularServer(
    ConwaysGameOfLife, 
    [canvas_element, owner_map, variety_map, group_map], 
    "Game of Life", 
    {
        "height": 50, 
        "width": 50, 
        "initial_chance": UserSettableParameter(
            "slider",
            "Chance of initiating alive",
            0.1,
            0.01,
            1,
            0.01,
            description="Choose chance of each cell being alive",
        ),
        "ambition_ceil": UserSettableParameter(
            "slider",
            "max chance of a cell becoming a leader",
            0.1,
            0.01,
            1,
            0.01,
            description="Choose chance of cells becoming leaders",),
        "opinion_ceil": UserSettableParameter(
            "slider",
            "max chance of a cell changing opinion",
            0.1,
            0.01,
            1,
            0.01,
            description="Choose chance of cells changing opinion",),
        "polarization": UserSettableParameter(
            "slider",
            "how much leadership matters",
            1.5,
            1,
            5,
            0.5,
            description="how much leadership matters",)
    }
)