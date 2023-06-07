# ==========================================
# Name: Kaleb Nim
# Student ID: 2100829
# Class: DAAA/FT/2B/02
# ==========================================

class Square:
    """Square represents A square on the map. """
    def __init__(self, x_coord, y_coord,color,color_mapping):
        """
        params:
            x_coord: int, x-coordinate of the square's center
            y_coord: int, y-coordinate of the square's center
            color: string, color of the square
            color_mapping: dict, maps a color to the next color in the sequence
        """
        # Set the square's center coordinates as a tuple
        self.centerPoint = (x_coord, y_coord)
        self.color = color
        self.__color_mapping = color_mapping

    def isClosest(self, x_coord, y_coord):
        """
        params:
            x_coord: int, x-coordinate of the point clicked by the user
            y_coord: int, y-coordinate of the point clicked by the user
        returns:
            True if the point clicked by the user is closest to the square's center
            False otherwise
        """
        # print(f'Checking if {x_coord},{y_coord} is closest to {self.centerPoint}')
         # Check if x_coord is within 12 pixels of the center of the square, the reason why 12 pixels is used is because each tile size is 24 pixels wide
        if x_coord >= self.centerPoint[0] - 12 and x_coord <= self.centerPoint[0] + 12:
            # Check if y_coord is within 12 pixels of the center of the square , the reason why 12 pixels is used is because each tile size is 24 pixels wide
            if y_coord >= self.centerPoint[1] - 12 and y_coord <= self.centerPoint[1] + 12: 
                return True
        return False
    
    def getCenter(self):
        """
        returns:
             the x and y coordinates of the square's center.
        """
        center_square_x_coord = self.centerPoint[0] # Get the x coordinate of the center of the square
        center_square_y_coord = self.centerPoint[1] # Get the y coordinate of the center of the square
        return center_square_x_coord, center_square_y_coord
    
    def getNextColor(self):
        """
        Function does the color reversal logic, for updating the visuals
            Updates it's own color state and returns the new color
        Uses the color Mapping dictionary to determine the next color

        if square is start or end node, then it will not change color
        """
        # Using __color_mapping Check if key is either "X" or "."
        if self.color == self.__color_mapping["X"] or self.color == self.__color_mapping["."]:
            # If so, then change the color to the other one
            if self.color == self.__color_mapping["X"]:
                self.color = self.__color_mapping["."]
            else:
                self.color = self.__color_mapping["X"]
        
        # Return the new color
        return self.color 

