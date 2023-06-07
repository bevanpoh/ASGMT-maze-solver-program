# ==========================================
# Name: Bevan Poh
# Student ID: 2112745
# Class: DAAA/FT/2B/02
# ==========================================

from .GraphSolver import GraphSolver
from ..utils.Math import Math

# Define a class for the Left Hand Solver algorithm
class LeftHandSolver(GraphSolver):
    # Class attribute for the name of the algorithm
    _algorithm_name = "Left Hand Rule"

    # Class attribute to store the lookup table for the different directions
    __direction_lookup = {
        (-1, 0): {  # north, negative row_index direction
            "back": (1, 0),  # S
            "left": (0, -1),  # E
            "right": (0, 1),  # W
        },
        (1, 0): {  # south, positive row_index direction
            "back": (-1, 0),  # N
            "left": (0, 1),  # W
            "right": (0, -1),  # E
        },
        (0, 1): {  # east, positive column_index direction
            "back": (0, -1),  # W
            "left": (-1, 0),  # N
            "right": (1, 0),  # S
        },
        (0, -1): {  # west, negative columnn_index direction
            "back": (0, 1),  # E
            "left": (1, 0),  # S
            "right": (-1, 0),  # N
        },
    }

    # Constructor method to initialize the class
    def __init__(self, initial_direction=(-1, 0)):
        # Call the superclass's constructor
        super().__init__(initial_direction)

    # =============================================================== #
    # Getters and Setters
    # =============================================================== #

    # No getters and setters are defined in this code block

    # =============================================================== #
    # Overloaded Built-ins
    # =============================================================== #

    # No overloaded built-ins are defined in this code block

    # =============================================================== #
    # Public Methods
    # =============================================================== #
    # Method to solve the graph using the Left Hand Solver algorithm
    def solve(self, graph):
        # Get the starting and ending positions of the path to be taken in the graph
        start, end = self._getStartAndEnd(graph)

        # List to store the steps taken during the path
        steps = []
        # Get the first direction that the solver should take by adding the starting position with the initial direction
        initial_heading = Math.elementwise_addition(start, self._initial_direction)
        # Append the first step as "walk" to the starting position
        steps.append(("walk", start))
        # Append the first step as "turn" in the initial direction
        steps.append(("turn", initial_heading))

        # Counter to keep track of the number of steps taken
        step_count = 0

        # Current position and direction of the solver
        current_position = start
        current_direction = self._initial_direction

        # Continue the loop until the end position is reached or the number of steps is equal to 2 times the number of nodes in the graph
        while current_position != end and step_count < 2 * graph.number_of_nodes():
            step_count += 1

            # Check the direction to the left of the current direction
            left_direction = type(self).__direction_lookup[current_direction]["left"]
            left_location = Math.elementwise_addition(current_position, left_direction)
            # Check if the current position has 4 neighbors
            four_neighbors = len(list(graph.neighbors(current_position))) == 4
            # If the current position has 4 neighbors or there is a path in the left direction
            if four_neighbors or left_location in graph.neighbors(current_position):
                # Append the step as "turn" in the left direction
                steps.append(("turn", left_location))
                # Append the step as "walk" in the left direction
                steps.append(("walk", left_location))
                # Update the current position and direction to the left
                current_position = left_location
                current_direction = left_direction
                continue

            # Check the direction in front of the current direction
            forward_location = Math.elementwise_addition(
                current_position, current_direction
            )
            # If there is a path in the forward direction
            if forward_location in graph.neighbors(current_position):
                # Append the step as "walk" in the forward direction
                steps.append(("walk", forward_location))
                # Update the current position to the forward direction
                current_position = forward_location
                continue

            # Check the direction to the right of the current direction
            right_direction = type(self).__direction_lookup[current_direction]["right"]
            right_location = Math.elementwise_addition(
                current_position, right_direction
            )
            # Append the step as "turn" in the right direction
            steps.append(("turn", right_location))
            # If there is a path in the right direction
            if right_location in graph.neighbors(current_position):
                # Append the step as "walk" in the right direction
                steps.append(("walk", right_location))
                current_position = right_location
                current_direction = right_direction
                continue

            # if here there are no other options but to turn back
            back_direction = type(self).__direction_lookup[current_direction]["back"]
            back_location = Math.elementwise_addition(current_position, back_direction)
            steps.append(("turn", back_location))
            steps.append(("walk", back_location))
            current_position = back_location
            current_direction = back_direction

        print("Left hand steps:", step_count)
        return steps

    # =============================================================== #
    # Private Methods
    # =============================================================== #


if __name__ == "__main__":
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    lhs = LeftHandSolver()

    # for dire in directions:
    #     print(dire)
    #     print(lhs.(self).__direction_lookup[dire]["right"])
    #     print()

    print(type(lhs)._algorithm_name)
    print(lhs.getAlgorithmName())
    print(type(lhs)._LeftHandSolver__direction_lookup)
