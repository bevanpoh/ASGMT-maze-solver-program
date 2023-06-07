# ==========================================
# Name: Kaleb Nim
# Student ID: 2100829
# Class: DAAA/FT/2B/02
# ==========================================

import random
def convertGeneratedMap(generatedPerfectMap, start, end):
        """
        This function converts the generated map into a format that can be used by the Map class.
        """ 
        symbol_mapping = {
            0: ".",
            1: "X"
        }
        convertedMap = []
        # Convert the generated map into a format Map class
        for row in generatedPerfectMap:
            convertedRow = []
            for cell in row:
                convertedRow.append(symbol_mapping[cell])
            convertedMap.append(convertedRow)
        print(convertedMap)

        # Set the start and end nodes to s and e respectively
        convertedMap[start[1]][start[0]] = "s"
        convertedMap[end[1]][end[0]] = "e"

        print(convertedMap)
        return convertedMap
class PerfectMaze:
    def __init__():
        pass
    def createPerfectMaze(width, height):
        """
        This function creates a maze of given width and height using randomized depth-first search algorithm.
        """
        # Helper function to return the direction of unvisited cells
        def __find_neighbors(x, y):
            """
            This function finds the neighbors of a cell that have not been visited yet.
            """
            neighbors = [] #initialize the neighbors list
            # If a cell on the left of the current cell is not visited and within the boundary of the maze,
            # add it to the list of neighbors
            if x > 1 and not visited[x//2-1][y//2]:
                neighbors.append((x-2, y))
            # If a cell on the right of the current cell is not visited and within the boundary of the maze,
            # add it to the list of neighbors
            if x < width-2 and not visited[x//2+1][y//2]:
                neighbors.append((x+2, y))
            # If a cell above the current cell is not visited and within the boundary of the maze,
            # add it to the list of neighbors
            if y > 1 and not visited[x//2][y//2-1]:
                neighbors.append((x, y-2))
            # If a cell below the current cell is not visited and within the boundary of the maze,
            # add it to the list of neighbors
            if y < height-2 and not visited[x//2][y//2+1]:
                neighbors.append((x, y+2))
            # shuffle the neighbors list so that the order of visiting them is randomized
            random.shuffle(neighbors)
            return neighbors

        # Initialize the maze with walls represented by 1's
        maze = [[1 for x in range(width)] for y in range(height)]
        # Keep track of visited cells to ensure that we don't revisit a cell
        visited = [[False for x in range(width//2 + 1)] for y in range(height//2 + 1)]
        # Randomly select the starting cell
        start_x, start_y = random.randint(2, width-2), random.randint(2, height-2)
        # Randomly select the ending cell
        end_x, end_y = random.randint(2, width-2), random.randint(2, height-2)
        stack = [(start_x, start_y)] #initialize the stack with the starting cell
        visited[start_x//2][start_y//2] = True #mark the starting cell as visited

        # Keep visiting cells until the stack is empty
        while stack:
            # Get the last cell from the stack
            x, y = stack[-1]
            # If the current cell is the end cell, stop visiting cells
            if (x, y) == (end_x, end_y):
                break
            # Find the neighbors of the current cell that have not been visited yet
            neighbors = __find_neighbors(x, y)
            # If there are no unvisited neighbors, pop the current cell from the stack
            if not neighbors:
                stack.pop()
            else:
                # Get the first neighbor from the shuffled list of neighbors
                nx, ny = neighbors[0]
                # Break the wall between the current cell and the selected neighbor
                if nx < x:
                    maze[x-1][y] = 0
                elif nx > x:
                    maze[x+1][y] = 0
                elif ny < y:
                    maze[x][y-1] = 0
                elif ny > y:
                    maze[x][y+1] = 0
                # Mark the selected neighbor as visited and add it to the stack
                visited[nx//2][ny//2] = True
                stack.append((nx, ny))
        # Return the generated maze
        start = (start_x, start_y)
        end = (end_x, end_y)
        
        convertedMap = convertGeneratedMap(maze, start, end)

        return convertedMap

# Example usage
generatedPerfectMap = PerfectMaze.createPerfectMaze(20, 20)
print(f'generatedPerfectMap: {generatedPerfectMap}')