# ==========================================
# Name: Bevan Poh
# Student ID: 2112745
# Class: DAAA/FT/2B/02
# ==========================================

from .Drone import Drone


class DroneController:
    __colors= ["red", "orange", "yellow", "green", "blue", "purple"]

    def __init__(
        self, graph_paths_dict: dict, tile_size: int, map_width: int, map_height
    ):
        """
        This class is responsible for controlling activate drones(Turtle objects) and initializing them + storing them

        params:
            graph_paths: dict of paths, key is algorithm name, value is path: list of tuples+instructions
                E.g {
                        'Left Hand Rule': [('walk', (2, 1)), ('turn', (1, 1)), ('turn', (2, 2)), ('walk', (2, 2))],
                        'A*':[(...),(...),(...)],
                        "BFS": [(...),(...),(...)],
                    }
            The follwing 3 params are used to convert the path_list to coordinate format
                tile_size: int, size of each tile in pixels
                map_width: int, width of map in tiles
                map_height: int, height of map in tiles
        """
        self.__drones = []
        self.__active_index = 0
        self.__tile_size = tile_size
        self.__map_width = map_width
        self.__map_height = map_height
        self.__initialiseDrones(graph_paths_dict)

    # =============================================================== #
    # Getters and Setters
    # =============================================================== #
    def activeDrone(self):
        return self.__drones[self.__active_index]

    # =============================================================== #
    # Overloaded Built-ins
    # =============================================================== #

    # =============================================================== #
    # Public Methods
    # =============================================================== #
    def cycleActive(self):
        self.activeDrone().hideturtle()
        self.__active_index = (self.__active_index + 1) % len(self.__drones)
        self.activeDrone().showturtle()
        print(f"Current Active Drone: {self.activeDrone().getName()}")

    def moveActive(self):
        self.activeDrone().performNextInstruction()

    def moveBackActive(self):
        self.activeDrone().performPreviousInstruction()

    def showActiveDrone(self):
        self.activeDrone().showturtle()

    def resetAllDrones(self):
        for drone in self.__drones:
            drone.hideturtle()

        for drone in self.__drones:
            drone.goToStart()

    def resetActiveDrone(self):
        self.activeDrone().goToStart()

    def updateDronePaths(self, graph_path_dict):
        print("gpd:", graph_path_dict)
        for drone in self.__drones:
            new_path = graph_path_dict[drone.getName()]
            new_path_coordinates = self.__convertPathToCoordinates(new_path)

            drone.setPath(new_path_coordinates)

    def moveAllDrones(self):
        for drone in self.__drones:
            drone.showturtle()

        allDone = [0] * 2
        while sum(allDone) < len(self.__drones):
            for i, drone in enumerate(self.__drones):
                drone.performNextInstruction()
                allDone[i] = int(drone.isAtEnd())

    # =============================================================== #
    # Private Methods
    # =============================================================== #
    def __initialiseDrones(self, graph_paths_dict):
        """
        __initialiseDrones is a function that will create a drone for each algorithm in the graph_paths_dict
        After creating the drone, it will be appended to the __drones list to be managed

        params:
            graph_paths_dict: dict of paths, key is algorithm name, value is path_list: list of tuples
            E.g {'Left Hand Rule': [('walk', (2, 1)), ('turn', (1, 1)), ('turn', (2, 2)), ('walk', (2, 2))],
                 'A*':[(...),(...),(...)] }
        returns:
            Populate the __drones list with initialised drones
                initialised drones are drones that have been given a name, path_list to follow with instructions
        """
        for algo_name, path_list in graph_paths_dict.items():
            path_list_coordinate = self.__convertPathToCoordinates(path_list)
            self.__drones.append(
                Drone(instructions=path_list_coordinate, name=algo_name)
            )

    def __convertPathToCoordinates(self, path_list):
        print("==>> path_list: ", path_list)
        path_list_coordinate = []  # path_list in coordinate format
        # Convert the path_list to coordinate format, unpack the tuple
        for instrcution, (
            x,
            y,
        ) in path_list:  # nstruction is walk/turn, x and y are the coordinates
            print(f"(x, y): {(x, y)}")
            x_coord, y_coord = self.__intToCoordinate(x, y)
            path_list_coordinate_step = (instrcution, (x_coord, y_coord))
            path_list_coordinate.append(path_list_coordinate_step)

        return path_list_coordinate

    def __intToCoordinate(self, x, y):
        """
        __intToCoordinate is a function that given coordinates in interger format, will convert it to a coordinate on the screen

        Calculation logic:
            Center the drawing by subtracting x and y index value by the maze width and height then /2: E.g Map range [0-8] --> [-4,4]
            Multiply by tile size to get the coordinate on the screen
        """
        x_coord = ((self.__map_width / 2) - x) * self.__tile_size
        y_coord = (y - (self.__map_height / 2)) * self.__tile_size
        return y_coord, x_coord
