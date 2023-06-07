# ==========================================
# Name: Bevan Poh
# Student ID: 2112745
# Class: DAAA/FT/2B/02
# ==========================================

from .GraphSolver import GraphSolver
import networkx as nx
from ..utils.Math import Math

class AStarSolver(GraphSolver):
    _algorithm_name = "A*"

    def __init__(self, heurisitic=None, initial_direction=(-1, 0)):
        super().__init__(initial_direction)
        self.__heuristic = heurisitic or Math.manhattan_distance

    # =============================================================== #
    # Getters and Setters
    # =============================================================== #

    # =============================================================== #
    # Overloaded Built-ins
    # =============================================================== #

    # =============================================================== #
    # Public Methods
    # =============================================================== #
    def solve(self, graph):
        start, end = self._getStartAndEnd(graph)
        try:
            astar_path = nx.astar_path(graph, start, end, heuristic=self.__heuristic)
        except:
            astar_path = None

        steps = self.__preprocess_path(start, astar_path)
        return steps

    # =============================================================== #
    # Private Methods
    # =============================================================== #
    def __preprocess_path(self, start, path):
        steps = []
        initial_heading = Math.elementwise_addition(start, self._initial_direction)
        steps.append(("walk", start))
        steps.append(("turn", initial_heading))

        current_direction = self._initial_direction
        current_location = start

        if path != None:
            for path_node in path[1:]:
                direction_to_path_node = Math.elementwise_subtraction(
                    path_node, current_location
                )
                if direction_to_path_node != current_direction:
                    steps.append(("turn", path_node))
                    current_direction = direction_to_path_node
                steps.append(("walk", path_node))
                current_location = path_node

        return steps
