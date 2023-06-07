# ==========================================
# Name: Bevan Poh
# Student ID: 2112745
# Class: DAAA/FT/2B/02
# ==========================================

from turtle import Turtle


class Drone(Turtle):
    def __init__(self, instructions="string", name=None):
        super().__init__()

        print(instructions)
        self.__instructions = instructions
        self.__name = name
        self.__current_index = 0
        self.__current_steps = 0

        # Initialise Turtle
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.shapesize(0.5, 0.5, 0.5)
        self.hideturtle()
        self.goToStart()

    # =============================================================== #
    # Getters and Setters
    # =============================================================== #
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def setPath(self, instructions):
        self.__instructions = instructions

    def getCurrentStep(self):
        return self.__current_steps - 1

    # =============================================================== #
    # Overloaded Built-ins
    # =============================================================== #

    # =============================================================== #
    # Public Methods
    # =============================================================== #
    def performNextInstruction(self):
        if self.__current_index >= len(self.__instructions) - 1:
            return

        self.__current_index += 1

        instruction, (x, y) = self.__instructions[self.__current_index]
        self.__performAction(instruction, x, y)

    def performPreviousInstruction(self):
        if self.__current_index <= 1:
            return

        instruction, (x, y) = self.__instructions[self.__current_index]
        self.__performAction(instruction, x, y, reverse=True)

        self.__current_index -= 1

    def goToStart(self):
        self.__current_index = 0
        self.__current_steps = 0

        for i in range(2):
            instruction, (x, y) = self.__instructions[i]
            self.__performAction(instruction, x, y)
            print(x, y)
            print(self.heading())
            self.__current_index = i

    def isAtEnd(self):
        return self.__current_index == len(self.__instructions) - 1

    # =============================================================== #
    # Private Methods
    # =============================================================== #
    def __performAction(self, instruction, x, y, reverse=False):
        print("Button", (instruction, (x, y)))
        print(self.__current_index)
        if instruction == "walk":
            if reverse:
                self.__current_steps -= 1
            else:
                self.__current_steps += 1
            self.goto(x, y)

        else:
            angle = self.towards(x, y)
            self.setheading(-angle if reverse else angle)
