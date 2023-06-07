# ==========================================
# Name: Kaleb Nim
# Student ID: 2100829
# Class: DAAA/FT/2B/02
# ==========================================

import turtle
from time import time
import random
from .perfectMaze import PerfectMaze
class GUI:
    """
    The GUI Class is in charge of listening for user input
    and managing user input to respective functions
    """
    def __init__(self, Map, screen, renderer, mapManager, FileManager, droneController):
        self.__Map = Map
        self.__screen = screen
        self.__renderer = renderer
        self.__mapManager = mapManager
        self.__fileManager = FileManager
        self.__droneController = droneController

        self.__time_of_last_event = time()
        self.__min_time_between_events = 0.30

    def onTabPress(self):
        """
        This function is called when the user presses the tab key,
        Purpose:
            switch between algorithms
            switch active drone
            Update title of screen with new algorithm, No.steps taken resert to 0
        """
        if not self.__minTimeLapsed():
            return

        # Reset current Drone
        self.__droneController.resetActiveDrone()
        # Cycle through the active drone using the drone controller
        self.__droneController.cycleActive()
        self.__droneController.resetActiveDrone()
        # Update the title of the screen with the new algorithm name and reset the number of steps taken to 0
        self.__screen.title(
            f"Algorithm Name: {self.__droneController.activeDrone().getName()} | No. Steps Taken: {0}"
        )

    def onEnterPress(self):
        """
        This function is called when the user presses the enter key,
        Purpose:
            Run the current algorithm from start to end and display the path
            At every step during the single process, update the title of the screen with the number of steps taken + 1 automatically
        """
        if not self.__minTimeLapsed():
            return

        pass

    def onUpPress(self):
        """
        This function is called when the user presses the up key,
        Purpose:
            Run the current algorithm one step at a time and display the path
        """
        if not self.__minTimeLapsed():
            return

        # Move the active drone by one step
        self.__droneController.moveActive()
        # Update the title of the screen with the number of steps taken + 1 automatically
        self.__screen.title(
            f"Algorithm Name: {self.__droneController.activeDrone().getName()} | No. Steps Taken: {self.__droneController.activeDrone().getCurrentStep()}"
        )

    def onDownPress(self):
        self.__droneController.moveBackActive()
        self.__screen.title(
            f"Algorithm Name: {self.__droneController.activeDrone().getName()} | No. Steps Taken: {self.__droneController.activeDrone().getCurrentStep()}"
        )

    # the onscreenclick method is used to register the get_coordinates function as a callback that will be invoked whenever the user clicks the screen. The get_coordinates function takes two arguments, x and y, which are the x and y coordinates of the location where the user clicked the screen, respectively.
    def onClick(self, x_coord, y_coord):
        if not self.__minTimeLapsed():
            return

        print("Mouse clicked at x_coord =", x_coord, "y_coord =", y_coord)

        # Update the map visuals
        self.__renderer.updateMapVisuals(x_coord, y_coord)

        # Computes the new map array and returns it
        new_map = self.__renderer.updateCurrentMap()
        # Update the Map object with the new map array
        self.__mapManager.updateMap(self.__Map, new_map)

        # re-calculate paths + recreate drones
        self.__droneController.updateDronePaths(self.__Map.getSolutions())

        # Reset drone back to start
        self.__droneController.resetAllDrones()
        self.__droneController.showActiveDrone()
        self.__screen.title(
            f"Algorithm Name: {self.__droneController.activeDrone().getName()} | No. Steps Taken: {self.__droneController.activeDrone().getCurrentStep()}"
        )

    def onPressSaveMap(self, filename):
        if not self.__minTimeLapsed():
            return
        updatedMapstr = str(self.__Map.getArray())

        print(f"updatedMapstr: {updatedMapstr}")
        print("Save Map Pressed")
        self.__fileManager.saveFile(filename, updatedMapstr)

    def onPressGetInput(self):
        if not self.__minTimeLapsed():
            return
        print(f'Get Input Dimensions Pressed')

        map_height, map_width = self.__Map.getMapDimensions()
        print("==>> map_height: ", map_height)
        print("==>> map_width: ", map_width)
        # Create a perfect maze
        # This is a loop that will keep running until the user enters an integer > 0 and < 50
        map_height , map_width = self.__Map.getMapDimensions()
        print(f'==>>Create Random map_width: {map_width}, map_height: {map_height}')
        convertedMap = PerfectMaze.createPerfectMaze(map_width, map_height)

        # Update the Map object with the new map array
        self.__mapManager.updateMap(self.__Map, convertedMap)
        self.__renderer.drawHeading()
        self.__renderer.drawMap()
        self.__renderer.drawLegend()

        # re-calculate paths + recreate drones
        self.__droneController.updateDronePaths(self.__Map.getSolutions())

        # Reset drone back to start
        self.__droneController.resetActiveDrone()
        self.__screen.title(
            f"Algorithm Name: {self.__droneController.activeDrone().getName()} | No. Steps Taken: {self.__droneController.activeDrone().getCurrentStep()}"
        )


    def onQPress(self):
        if not self.__minTimeLapsed():
            return

        self.__screen.title("Multi Mode")
        self.__droneController.moveAllDrones()

    def onWPress(self):
        if not self.__minTimeLapsed(factor=5):
            return

        self.__droneController.resetAllDrones()
        self.__droneController.showActiveDrone()

    def createButtons(self):
        """
        Create a Turtle button
        """

    def __minTimeLapsed(self, factor=1):
        now_time = time()
        time_lapsed = now_time - self.__time_of_last_event
        print(time_lapsed)

        if time_lapsed < factor * self.__min_time_between_events:
            return False
        else:
            self.__time_of_last_event = now_time
            return True
