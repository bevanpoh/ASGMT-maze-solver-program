# ==========================================
# Name: Kaleb Nim
# Student ID: 2100829
# Class: DAAA/FT/2B/02
# ==========================================

from turtle import *
from .Square import Square

class Renderer:
    """
    The Renderer class is responsible for "rendering" the map , headings, legends and buttons on the screen.
    Additionally, it also handles the rendering of real-time updating of map states through user clicks.

    Methods:
        drawMap - Draws the map on the screen given a map object
        drawHeadings - Draws the headings on the screen, includes title
        drawLegend - Draws the legend on the screen

    Private Methods:
        __drawObject - Helper function to draw square given x_coord, y_coord, color. Reduces boilerplate code for telling map_pen to stamp a square at loctaion
        __calculateTileSize - Calculates the tile size based on the screen size and map size

    """
    def __init__(self,map:object,screen_width, screen_height, color_mapping= None):
        # If no color mapping is provided, use the default color mapping
        if color_mapping is None:
            print("No color mapping provided, using default color mapping")
            # Default color mapping
            self.color_mapping = {
                "s": "green",  # Assume start node is denoted by lowercase "s"
                "e": "blue",
                "X": "grey",
                ".": "white",
            }
        else:
            # Use the provided color mapping
            self.color_mapping = color_mapping

        # Store the screen width and height
        self.__screen_width = screen_width
        self.__screen_height=screen_height
        self.map = map

        # Get the map's dimensions
        self.__map_height, self.__map_width = self.map.getMapDimensions()

        self.__symbol_mapping = {
            "s": "Start Position",
            "e": "End Position",
            "X": "Wall",
            ".": "Path",
        }
        # Define the Map Artist's tile size
        self.__tile_size = self.__calcualteTileSize(self.__screen_width, self.__screen_height)
        print("==>> self.__tile_size: ", self.__tile_size)
        self.__screen_height=screen_height
        self.__screen_width=screen_width

        # Create the map pen which is a turle object for drawing the map
        self.__map_pen = Turtle()
        # Configure the map pen, shape,size, speed, etc. ( More details in the __configureMap_pen() method )
        self.__configureMap_pen()

        # Create the heading pen which is a turle object for drawing the heading
        self.__heading_pen = Turtle()
        self.__heading_pen.hideturtle()

        # the mapOfSquares acts as a memory of the squares that have been drawn
        self.__mapOfSquares = []  # This is a list of lists of squares
    # =============================================================== #
    # Getters and Setters
    # =============================================================== #
    def getTileSize(self):
        return self.__tile_size

    # =============================================================== #
    # Public Methods
    # =============================================================== #
    def drawLegend(self):
        """
        This function is fucked for now
        """
        self.mapping = {
            "s": "Start Position",
            "e": "End Position",
            "X": "Wall",
            ".": "Path",
        }
        # iterate through self.color_mapping
        padding = 0

        for symbol, color in self.color_mapping.items():
            self.__heading_pen.penup()
            x = (self.__screen_width / 2) - 400
            y = (self.__screen_height / 2) - 80 - padding

            symbol_text = self.__symbol_mapping[symbol].join(": ")
            self.__drawObject(x, y, color)
            self.__heading_pen.goto(x + 15, y)
            self.__map_pen.write(symbol_text, align="left", font=("Arial", 12, "normal"))
            padding += 40
        pass

    def drawHeading(self, text=None):
        if text == None:
            text = "PIZZA RUNNERS: Done by Kaleb Bevan, and DAAA/FT/2B/02"
        text_for_controls = "Controls: Click on the map to draw walls (GUI). 's' to save current map, 'tab' to switch between algorithms, 'Up' to move one step"
        text_for_more_controls = "'q' AutoPlay, 'w' Reset AutoPlay"
        # Write the heading onto the screen
        self.__heading_pen.penup()
        self.__heading_pen.goto(0, self.__screen_height / 2 - 40)
        self.__heading_pen.write(text, align="center", font=("Arial", 16, "normal"))
        self.__heading_pen.goto(0, -self.__screen_height / 2 + 80)
        self.__heading_pen.write(text_for_controls, align="center", font=("Arial", 12, "normal"))
        self.__heading_pen.goto(0, -self.__screen_height / 2 + 60)
        self.__heading_pen.write(text_for_more_controls, align="center", font=("Arial", 12, "normal"))
        pass

    def drawMap(self):
        """
        Draw the map onto the screen

        This function takes in a Map object and draws it on the screen.
        It does this by first getting the dimensions of the map using the `map.getMapDimensions()` method.
        Then, it retrieves the map as a 2D array using `map.getArray()`.

        For each cell in the map, the function checks if the character at that cell is a valid key in the `color_mapping` dictionary.
        If the character is in the `color_mapping`, the function uses the corresponding color to draw the object on the screen using the `__drawObject` method.
        If the character is not in the `color_mapping`, it is considered a wall and drawn using the color "black".

        params:
            map: Map object, representing the map to be drawn.
        """

        # Get the map as a 2D array
        map_arr = self.map.getArray()

        # Iterate through each cell in the map
        for i in range(self.__map_height):
            for j in range(self.__map_width):
                # Get the character at the each x,y coordinate
                character = map_arr[i][j]


                # Calculate screen coordinates from i j index
                x_coord, y_coord = self.__intToCoordinate(j, i)
                # Check if the character is a valid key in the color mapping
                if character in self.color_mapping:  # Lookup dictionary runtime: O(1)

                    # Draw the square onto the screen using the color mapping to get the color to draw
                    self.__drawObject(x_coord, y_coord, self.color_mapping[character])
                    # Create a square object and add it to the map of squares
                    self.__mapOfSquares.append(
                        Square(
                            x_coord,
                            y_coord,
                            self.color_mapping[character],
                            self.color_mapping,
                        )
                    )

                else:  # This error handling ensures program does not crash if the character is not in the color mapping
                    # Any other character is considered a wall
                    # Draw the square onto the screen using the color mapping to get the color to draw and will be a black square
                    self.__drawObject(x_coord, y_coord, "black")
                    # Add to the __mapOfSquares
                    x_coord, y_coord = self.__intToCoordinate(j, i)
                    self.__mapOfSquares.append(Square(x_coord, y_coord, "black"))

    # def drawButton(self):
    #     button = Button()
    #     # Set the button's position to bottom right corner
    #     button.hideturtle()
    #     button.goto(self.__screen_width / 2 - 100, -self.__screen_height / 2 + 50)
    #     # show the button
    #     button.showturtle()
    #     # Draw the button
    #     button.write("Generate Map", align="center", font=("Arial", 16, "normal"))
    #     # butoon onclick
    #     button.onclick(button.is_clicked(x=button.xcor(), y=button.ycor()))


    # =============================================================== #
    # Getters and Setters
    # =============================================================== #

    # =============================================================== #
    # Overloaded Built-ins
    # =============================================================== #

    def getClosestSquare(self, x_coord, y_coord):
        """
        Function ran when the user clicks on the screen
        getClosestSquare is a function that given coordinates, will return the closest square object
        if no square is closest, it will return None
        """
        # Get the closest square
        # iterate through the __mapOfSquares, return square that returns True when called square.isClosest(x_coord, y_coord)
        closest_square = None
        for square in self.__mapOfSquares:
            if square.isClosest(x_coord, y_coord):
                closest_square = square
                break
        return closest_square

    def updateMapVisuals(self, x_coord, y_coord):
        """
        updateMapVisuals is a function that given coordinates, will stamp turtle on the screen
        """
        # Get Square object closest to the coordinates
        closest_square = self.getClosestSquare(x_coord, y_coord)  # Map x_coord,y_coord to the cloest square center
        if (closest_square == None):  # Handle case where the coordinates clicked is not near any square
            return
        print(f"==>> closest_square center coords,color: {closest_square.getCenter()},{closest_square.color}")
        new_color = (closest_square.getNextColor())  # Color reversal logic is handled in the Square class

        print("==>> new_color: ", new_color)
        (center_square_x_coord,center_square_y_coord) = closest_square.getCenter()  # Get the center of the square
        print("==>> Closert center_square_x_coord: ", center_square_x_coord)
        print("==>> center_square_y_coord: ", center_square_y_coord)

        self.__drawObject(center_square_x_coord, center_square_y_coord, new_color)  # Draw the new color on the screen

    def updateCurrentMap(self):
        """
        Returns the current map as 2D array of characters representing the map from self.__mapOfSquares
        E.g 2D array
        [['X', '.', '.', '.', 'X', '.', '.', 'X', '.', '.', 'e', 'X'],
        ['X', '.', 'X', '.', '.', '.', '.', 'X', '.', 'X', 'X', 'X'],
        ['X', '.', '.', 'X', '.', 'X', '.', 'X', '.', 'X', '.', 'X'],
        ['X', 'X', '.', 'X', 'X', 'X', '.', 'X', '.', '.', '.', 'X'],
        ['X', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.', 'X'],
        ['X', 's', 'X', 'X', '.', '.', '.', 'X', '.', '.', '.', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        """
        # print('went into returnCurrentMap')
        map2d = []
        for i in range(self.__map_height):
            row = []
            for j in range(self.__map_width):
                x_coord, y_coord = self.__intToCoordinate(j, i)
                closest_square = self.getClosestSquare(x_coord, y_coord)
                color = closest_square.color
                # Using self.__color_mapping, convert color to character
                for char, color in self.color_mapping.items():
                    if color == closest_square.color:
                        row.append(char)

            map2d.append(row)
        print("==>> updated map: ", map2d)
        return map2d

    def updateCurrentMapFromGeneratedMap(self): # Back-end function to update the map from the generated map
        self.map.setArray()



    # =============================================================== #
    # Private Methods
    # =============================================================== #
    def __drawObject(self, x_coord, y_coord, color):

        """
        Draw an object on the screen

        This private helper function takes in the x and y coordinates, and the color of the object to be drawn.
        It uses the `map_pen` attribute to set the pen's color and position and finally draws the object using the `stamp()` method.

        params:
            x: int, x-coordinate of the object to be drawn
            y: int, y-coordinate of the object to be drawn
            color: string, color of the object to be drawn
        """

        # Pick up the pen so that it does not leave a trail
        self.__map_pen.penup()
        self.__map_pen.goto(x_coord, y_coord)
        # Set the pen color and draw the object
        self.__map_pen.color("black", color)
        self.__map_pen.stamp()
        self.__map_pen.pendown()

    def __intToCoordinate(self, x, y):
        """
        __intToCoordinate is a function that given coordinates in interger format, will convert it to a coordinate on the screen

        Calculation logic:
            Center the drawing by subtracting x and y index value by the maze width and height then /2: E.g Map range [0-8] --> [-4,4]
            Multiply by tile size to get the coordinate on the screen
        """
        x_coord = (x - (self.__map_width / 2)) * self.__tile_size
        y_coord = ((self.__map_height / 2) - y) * self.__tile_size
        return x_coord, y_coord

    def __coordinateToInt(self, x_coord, y_coord):
        """
        __coordinateToInt is a function that given coordinates in coordinate format, will convert it to an interger coordinate
        """
        x = (x_coord * self.__tile_size) + self.__map_width / 2
        y = (self.__map_height / 2) - (y_coord * self.__tile_size)
        return x, y


    def __configureMap_pen(self):
        """
        Configure the map pen for drawing the map
        parameters it configures:
            shape: square
            size: Relative to tile size
            speed: fastest
        """
        self.__map_pen.shape("square")
        self.__map_pen.shapesize(self.__tile_size / 20)  # HardCoded
        self.__map_pen.penup()
        self.__map_pen.speed("fastest")

    def __calcualteTileSize(self, screen_height, screen_width):
        """
        __calcualteTileSize is a function that calculates the tile size based on the screen height and width
        """
        # Calculate the tile size based on the screen height and width
        if self.__screen_height > self.__screen_width:
            tile_size = screen_width / (4*self.__map_width)
        else:
            tile_size = screen_height / (4*self.__map_height)
        return tile_size

