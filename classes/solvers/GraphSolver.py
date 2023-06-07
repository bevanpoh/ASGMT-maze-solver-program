# ==========================================
# Name: Bevan Poh
# Student ID: 2112745
# Class: DAAA/FT/2B/02
# ==========================================


class GraphSolver:
    _algorithm_name = False

    def __init__(self, initial_direction=(-1, 0)):
        self._initial_direction = initial_direction

    # =============================================================== #
    # Getters and Setters
    # =============================================================== #

    # =============================================================== #
    # Overloaded Built-ins
    # =============================================================== #

    # =============================================================== #
    # Public Methods
    # =============================================================== #
    def getAlgorithmName(self):
        # type(self) resolves to calling Class
        # so if inheritance resolvs to Child
        return type(self)._algorithm_name

    def solve(self, graph):
        raise NotImplementedError

    # =============================================================== #
    # Private Methods
    # =============================================================== #

    def _getStartAndEnd(self, graph):
        start = None
        end = None

        for n, v in graph.nodes(data=True):
            if v["type"] == "start":
                start = n

            if v["type"] == "delivery":
                end = n

            if start and end:
                break

        return start, end


if __name__ == "__main__":
    g = GraphSolver()

    print(g._algorithm_name)
    print(g.getAlgorithmName())
