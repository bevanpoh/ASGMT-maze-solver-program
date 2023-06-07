# ==========================================
# Name: Bevan Poh , Kaleb Nim
# Student ID: 2112745, 2100829
# Class: DAAA/FT/2B/02
# ==========================================

import os
import sys


class FileManager:
    """
    A FileManager manages all files within the base path folder

    """
    def __init__(self, base_path=None):
        self.__base_path = base_path or os.path.dirname(sys.argv[0])

    # =============================================================== #
    # Properties
    # =============================================================== #

    # =============================================================== #
    # Overloaded Built-ins
    # =============================================================== #

    # =============================================================== #
    # Public Methods
    # =============================================================== #
    def openFile(self, filename):
        """
        Takes in filename
        Returns the contents of the file as a strings, one for each line
        """
        filepath = os.path.abspath(os.path.join(self.__base_path, filename))

        try:
            with open(filepath, "r") as f:
                contents = f.read()
            return contents
        except FileNotFoundError:
            print(f"Could not find file {filepath}")

    def saveFile(self, filename, contents):
        """
        Takes in filename and contents
        Saves the contents to the file

        creates the txt file if it does not exist
        params:
            filename: str
            contents: str
        returns:
            .txt file saved in the base path
        """
        filepath = os.path.abspath(os.path.join(self.__base_path, filename))

        # create the file if it does not exist
        if not os.path.exists(filepath):
            open(filepath, "w").close()
        
        # if the file exists, write to it and overwrite the contents
        with open(filepath, "w+") as f:
            f.write(contents)

            
    # =============================================================== #
    # Private Methods
    # =============================================================== #


if __name__ == "__main__":
    a = os.path.dirname(sys.argv[0])
    b = __file__
    print()
