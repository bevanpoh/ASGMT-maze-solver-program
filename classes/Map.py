# ==========================================
# Name: Bevan Poh
# Student ID: 2112745 
# Class: DAAA/FT/2B/02
# ==========================================


class Map:
    def __init__(self, map_arr, map_graph, solutions):
        self.__map_width = len(map_arr[0])
        self.__map_height = len(map_arr)

        # The reason why intatiate
        self.__array = map_arr
        self.__graph = map_graph
        self.__solutions = solutions

    # =============================================================== #
    # Getters and Setters
    # =============================================================== #
    def getMapDimensions(self):
        return self.__map_height, self.__map_width

    def getArray(self):
        return self.__array

    def getGraph(self):
        return self.__graph

    def setArray(self, map_arr):
        self.__array = map_arr
    
    def getSolutions(self):
        return self.__solutions
    
    def setSolutions(self, solutions):
        self.__solutions = solutions
    
    def setGraph(self, map_graph):
        self.__graph = map_graph
    
    
    # =============================================================== #
    # Overloaded Built-ins
    # =============================================================== #
    def __str__(self):
        return "\n".join(["".join(line) for line in self.__array])

    # =============================================================== #
    # Public Methods
    # =============================================================== #
   

    # =============================================================== #
    # Private Methods
    # =============================================================== #
