from GraphSolver import GraphSolver

class BFSSolver(GraphSolver):

    _algorithm_name = "Breadth First Search"

    def __init__(self, initial_direction=(-1, 0)): # Start from up

        super().__init__(initial_direction)

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
        """
        params:
            graph: networkx graph
        returns:
            steps: list of tuples,first index is the action, second index is node, where node is a tuple of (row_index, column_index) and action is a string
            Example: [("turn", (1, 2)), ("walk", (2, 2)), ("turn", (2, 3)), ("walk", (2, 4))]
        """
        starts, ends = self._getStartAndEnd(graph)
        start = starts[0]
        end = ends[0]

        steps = []
        initial_heading = _elementwise_addition(start, self._initial_direction)
        steps.append(("turn", initial_heading))
    

test_graph = nx.Graph()
