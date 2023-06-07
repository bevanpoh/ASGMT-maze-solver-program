
file = """
XXXXXXXXXXXX
XX....XXXXXX
XX.XX.XXXXXX
XX....XXXXXX
XX.XXXXXXXXX
XXsXXXXXXXXX
XXeXXXXXXXXX
XXXXXXXXXXXX
"""

from temp.MapManager import MapManager
from temp.Map import Map

from LeftHandSolver import LeftHandSolver
from AStarSolver import AStarSolver

mapM = MapManager(None)
map = mapM.createMap(map_str=file)

print(map)

lhs = LeftHandSolver()
astart = AStarSolver()

print(lhs.solve(map.getGraph()))
