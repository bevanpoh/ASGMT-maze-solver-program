# ==========================================
# Name: Bevan Poh , Kaleb Nim
# Student ID: 2112745, 2100829
# Class: DAAA/FT/2B/02
# ==========================================

from classes.FileManager import FileManager
from classes.MapManager import MapManager
import networkx as nx
import matplotlib.pyplot as plt
from classes.graphics.Renderer import Renderer
from turtle import *
from classes.GUI import GUI
from classes.drones.Drone import Drone
from classes.drones.DroneController import DroneController
from classes.solvers.LeftHandSolver import LeftHandSolver
from classes.solvers.AStarSolver import AStarSolver

# Set this to True to enable advanced features
ADVANCED_FEATURE_MODE = True

filename = "./test_maps/squareMap"  # @param {type:"string"}
fileManager = FileManager()
mapManager = MapManager([LeftHandSolver(), AStarSolver()], None)

b = fileManager._FileManager__base_path
Map = mapManager.createMap(map_str=fileManager.openFile(filename + ".txt"))


# Create a renderer, initialized with Big Map object
screen = Screen()
screen.setup(1200, 800)  # Set the size of the screen
screen.title("Algorithm Name: Left Hand Rule | No. Steps Taken: 0")
renderer = Renderer(
    map=Map,
    screen_width=screen.window_width(),
    screen_height=screen.window_height(),
    # Users are able to change the color mapping here
    color_mapping={
        "s": "green",  # Assume start node is denoted by lowercase "s"
        "e": "blue",  # Assume end node is denoted by lowercase "e"
        "X": "grey",
        ".": "white",
    },
)

screen.listen()
# Render the map
renderer.drawHeading()
renderer.drawMap()
renderer.drawLegend()
# renderer.drawButton()

# Intialize the drone manager
droneController = DroneController(
    graph_paths_dict=Map.getSolutions(),
    tile_size=renderer.getTileSize(),
    map_width=Map.getMapDimensions()[0],
    map_height=Map.getMapDimensions()[1],
)
droneController.showActiveDrone()

# Create a GUI
gui = GUI(
    Map=Map,
    screen=screen,
    renderer=renderer,
    mapManager=mapManager,
    FileManager=fileManager,
    droneController=droneController,
)


# screen.onkeypress(gui.saveMap(filename + "_updated.txt"), "Tab")
screen.onkeypress(gui.onTabPress, "Tab")
screen.onkeypress(gui.onEnterPress, "Return")
screen.onkeypress(gui.onUpPress, "Up")
screen.onkeypress(gui.onDownPress, "Down")

if ADVANCED_FEATURE_MODE:
    screen.onkeypress(gui.onPressGetInput, "c")
    screen.onscreenclick(gui.onClick)
    screen.onkeypress(gui.onQPress, "q")
    screen.onkeypress(gui.onWPress, "w")

# Dont close the screen
screen.mainloop()
