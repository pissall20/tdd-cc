"""
A squad of robotic rovers are to be landed by NASA on a plateau on Mars.

This plateau, which is curiously rectangular, must be navigated by the rovers so that their on-board cameras can get a complete view of the surrounding terrain to send back to Earth.
A rover’s position and location is represented by a combination of x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.

In order to control a rover , NASA sends a simple string of letters. The possible letters are ‘L’, ‘R’ and ‘M’. ‘L’ and ‘R’ makes the rover spin 90 degrees left or right respectively, without moving from its current spot. ‘M’ means move forward one grid point, and maintain the same heading.

Assume that the square directly North from (x, y) is (x, y 1).

INPUT:
The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0,0.
The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover’s position, and the second line is a series of instructions telling the rover how to explore the plateau.

The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover’s orientation.

Each rover will be finished sequentially, which means that the second rover won’t start to move until the first one has finished moving.

OUTPUT:
The output for each rover should be its final co-ordinates and heading.

INPUT AND OUTPUT
Test Input:
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM

Expected Output:
1 3 N
5 1 E
"""


class Plateau:

    def __init__(self, x_coord, y_coord):
        self.x_coord = int(x_coord)
        self.y_coord = int(y_coord)
        self.grid = [[0] * self.x_coord] * self.y_coord

    def __str__(self):
        return str((self.x_coord, self.y_coord))

    def add_rover_position(self, x, y):
        if x <= len(self.grid) and y <= len(self.grid):
            self.grid[self.x_coord - x][y-1] = 1
        else:
            raise ValueError("Movement sequence landing out of grid-zone")

    def reset(self):
        self.grid = [[0] * self.x_coord] * self.y_coord

class Rover:

    def __init__(self, grid, rover_x, rover_y, direction):
        self.grid = grid
        self.x = int(rover_x)
        self.y = int(rover_y)
        self.direction = direction

        self.grid.add_rover_position(self.x, self.y)

    def __str__(self):
        return f"Position of rover is {str((self.x, self.y))} currently facing {self.direction}"

    def reset_position(self):
        self.grid.reset()

    def change_direction(self, new_direction):
        direction_list = ["N", "E", "S", "W"]
        current_index = direction_list.index(self.direction)
        if new_direction == "L":
            self.direction = direction_list[current_index-1]
        elif new_direction == "R":
            self.direction = direction_list[current_index+1]
            if current_index >= 3:
                self.direction = direction_list[0]

    def take_step(self):
        if self.direction == "N":  
            self.x += 1
        if self.direction == "S":
            self.x -= 1
        if self.direction == "E":
            self.y += 1
        if self.direction == "W":
            self.y -= 1

        self.reset_position()
        self.grid.add_rover_position(self.x, self.y)


    def move(self, sequence):
        if isinstance(sequence, str):
            sequence = list(sequence)
        
        for a_move in sequence:
            if a_move != "M":
                self.change_direction(a_move)
            elif a_move == "M":
                self.take_step()


if __name__ == "__main__":
    grid_input = input("Enter Plateau grid-size:").strip().split(" ")
    if len(grid_input) != 2:
        raise ValueError("Wrong number of arguments for Mars Plateau shape")
    
    rect_grid = Plateau(*grid_input)

    position_input = input("Enter rover coordinates:").split(" ")

    rover1 = Rover(rect_grid, *position_input)
    print(rover1)
    movement_input = input("Enter movement sequence:").strip()
    
    rover1.move(movement_input)
    print(rover1)

