# ==========================================
# Name: Bevan Poh
# Student ID: 2112745
# Class: DAAA/FT/2B/02
# ==========================================

from .Map import Map
import networkx as nx


class MapManager:
    def __init__(self, graphSolvers, TSPOptimisers):
        self.__TSP_graph = False
        self.__graphSolvers = graphSolvers
        self.__TSPOptimisers = TSPOptimisers
        """"""

    def null():
        "solve graphs"
        # foreach solver, get a path for the graph
        # store paths in created maze objects

        # multi-endpoint solvers
        #

    # =============================================================== #
    # Getters and Setters
    # =============================================================== #
    def enableTSPGraph(self):
        self.__TSP_graph = True

    def disableTSPGraph(self):
        self.__TSP_graph = False

    # =============================================================== #
    # Overloaded Built-ins
    # =============================================================== #

    # =============================================================== #
    # Public Methods
    # =============================================================== #
    def createMap(self, map_str=None, map_arr=None):
        """
        Returns a full maze object with all the attributes
        """

        if map_arr is None:
            map_arr = self.__strToArr(map_str)
        map_graph = self.__arrToGraph(map_arr)
        solutions = self.__findSolutions(map_graph)
        print("==>> solutions: ", solutions)

        map = Map(map_arr, map_graph, solutions)

        return map

    def updateMap(self,map, new_map_arr):
        """
        Updates the map object with the new map array in place
        params:
            map: Map object class to be updated
            new_map_arr: 2D array of characters representing the maze
        """
        map.setArray(new_map_arr)
        # Update the graph, solutions, etc
        map.setGraph(self.__arrToGraph(new_map_arr))
        map.setSolutions(self.__findSolutions(map.getGraph()))
        print(f'Updated Map with new map array:')

        
        




    # =============================================================== #
    # Private Methods
    # =============================================================== #
    def __strToArr(self, map_str):
        """
        params:
            contents: string of characters representing the maze
        returns:
            Map: 2D array of characters representing the maze

        Sample conents:
        `
        X...X..X..eX
        X.X....X.XXX
        X..X.X.X.X.X
        XX.XXX.X...X
        X........X.X
        XsXX...X...X
        XXXXXXXXXXXX
        ` ==>
        [['X', '.', '.', '.', 'X', '.', '.', 'X', '.', '.', 'e', 'X'],
        ['X', '.', 'X', '.', '.', '.', '.', 'X', '.', 'X', 'X', 'X'],
        ['X', '.', '.', 'X', '.', 'X', '.', 'X', '.', 'X', '.', 'X'],
        ['X', 'X', '.', 'X', 'X', 'X', '.', 'X', '.', '.', '.', 'X'],
        ['X', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.', 'X'],
        ['X', 's', 'X', 'X', '.', '.', '.', 'X', '.', '.', '.', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        """
        line_splits = map_str.split()
        map_arr = [list(line) for line in line_splits]

        return map_arr

    def __arrToGraph(self, map_arr):
        """
        params:
            Map: 2D array of characters representing the maze
        returns:
            GraphMap: GraphMap object inherits from nx.Graph class with additon attributes

        Time complexity: O(m * n)
            where m is the number of rows in the map and n is the number of characters in each row

        The first loop that iterates over the rows of the map and the second loop that iterates over the characters in each row run in O(m * n) time.
        In each iteration, the code adds a node to the graph, which takes O(1) time.
        The second loop that iterates over the rows and characters of the map again takes O(m * n) time.
        In each iteration, the code checks if the node exists and its type, which takes O(1) time, and adds an edge to it, which takes O(1) time.

        Therefore, the overall time complexity of the function is O(m * n) + O(m * n) = O(m * n).
        """
        map_graph = nx.Graph()

        for i, row in enumerate(map_arr):
            # Iterate over the characters in the row
            for j, c in enumerate(row):
                if c == ".":
                    # Add a node representing a road
                    map_graph.add_node((i, j), type="road")
                elif c == "s":
                    # Add a node representing the start location and store its position
                    map_graph.add_node((i, j), type="start")
                elif c == "e":
                    # Add a node representing the delivery location and store its position
                    map_graph.add_node((i, j), type="delivery")

        for i, row in enumerate(map_arr):
            for j, c in enumerate(row):
                if (i, j) in map_graph:
                    # Add an edge to the node to the left, if it exists and is of the correct type
                    if (i, j - 1) in map_graph:
                        map_graph.add_edge((i, j), (i, j - 1))

                    # Add an edge to the node above, if it exists and is of the correct type
                    if (i - 1, j) in map_graph:
                        map_graph.add_edge((i, j), (i - 1, j))

        return map_graph

    def __findSolutions(self, map_graph):
        solutions = {}
        for solver in self.__graphSolvers:
            method = solver.getAlgorithmName()
            solutions[method] = solver.solve(map_graph)

        return solutions
