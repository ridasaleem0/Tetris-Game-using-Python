#!/usr/bin/env python
import sys  # Import the sys module for reading from STDIN

shapes = {
    'Q': [['#', '#'],
          ['#', '#']],
    'Z': [['#', '#', '.'],
          ['.', '#', '#']],
    'S': [['.', '#', '#'],
          ['#', '#', '.']],
    'T': [['#', '#', '#'],
          ['.', '#', '.']],
    'I': [['#', '#', '#', '#']],
    'L': [['#', '.'],
          ['#', '.'],
          ['#', '#']],
    'J': [['.', '#'],
          ['.', '#'],
          ['#', '#']]
}


class Piece:
    def __init__(self, piece):
        """Initialize the Piece class with the given piece matrix"""
        self.piece = piece

    @property
    def width(self):
        """ Get the width of the piece matrix """
        return len(self.piece[0])

    @property
    def height(self):
        """Get the height of the piece matrix"""
        return len(self.piece)

    # Printing piece for Debugging purposes
    def __str__(self):
        # Return a string representation of the piece matrix
        return '\n'.join(''.join(line) for line in self.piece)


class Grid:
    def __init__(self, width, height):
        """Initialize the grid with the given width and height."""
        self.max_height = height
        self.max_width = width
        self.grid = [['.'] * width for __ in range(height)]

    def completed_line(self):
        """Yield the index of completed lines in the grid."""
        for i, line in enumerate(self.grid):
            if line.count('.') == 0:
                yield i

    def unoccupied_line(self):
        """Return the number of unoccupied lines in the grid."""
        empty = 0
        for i, line in enumerate(self.grid):
            if line.count('#') == 0:
                empty += 1
        return empty

    def clear_line(self, index):
        """Clear the line at the given index and refill with empty cells."""
        del self.grid[index]
        self.grid.insert(0, ['.' for _ in range(self.max_width)])

    def drop(self, piece, start_column, grid_max_height):
        """Check if the letter piece can be dropped starting from the specified column."""
        last_level = grid_max_height - piece.height + 1
        for level in range(last_level):
            for i in range(piece.height):
                for j in range(piece.width):
                    if self.grid[level + i][start_column + j] == "#" and piece.piece[i][j] == "#":
                        return level - 1
        return last_level - 1

    def place_piece(self, piece, pos):
        """Place the piece at the specified position in the grid."""
        level, start_column = pos
        for i in range(piece.height):
            for j in range(piece.width):
                if piece.piece[i][j] == "#":
                    self.grid[level + i][start_column + j] = piece.piece[i][j]

    # Printing grid for Debugging purposes
    def __str__(self):
        return '\n'.join(''.join(line) for line in self.grid)


def find_best_position(grid, start_column, piece, grid_max_height):
    """
        Finds the best position to place a Tetris piece on the grid.

        Parameters:
        - grid: List of lists representing the current state of the Tetris grid.
        - start_column: The left-most column where the piece will be placed.
        - piece: The Tetris piece to be placed on the grid.
        - grid_max_height: The current maximum height of the Tetris grid.

        Returns:
        A list containing information about the best position:
        [number of blocks covered by the piece, column of the piece, row of the piece]
    """
    result = []

    # Calculate the highest level where the piece can be dropped
    level = grid.drop(piece, start_column, grid_max_height)
    # Calculate the total number of blocks covered by the piece at the current level
    blocks = sum(b.count('#') for b in grid.grid[level:level + piece.height])
    result.append([blocks, start_column, level])

    # Iterate over the result list to find the best position based on the maximum blocks,
    # given start column, and minimum level
    for i, fn in enumerate([max, min, min]):
        key = fn(result, key=lambda x: x[i])[i]
        result = [x for x in result if x[i] == key]
    return result[0]


def tetris_engine(line):
    """
        Processes a Tetris sequence and returns the resulting height of the remaining blocks within the grid.
        Removes filled Tetris rows.

        Parameters:
        - line: A string representing a Tetris sequence, where each entry is a letter and a single-digit integer.

        Returns:
        The resulting height of the remaining blocks within the grid.
    """

    # Split the input line into a list of entries
    input_values = line.split(',')

    # Create a new Tetris grid with dimensions 10x5 initially
    grid = Grid(10, 5)
    grid_height = 0

    # Iterate through each entry in the Tetris sequence
    for line in input_values:
        # Extract shape and start column information from the entry
        shape, start_column = line[0], int(line[1])

        # Create a Piece object with the given shape matrix
        p = shapes[shape]
        piece = Piece(p)

        # Adjust the grid height to accommodate each new incoming piece, grid height is not fixed
        for _ in range(0, piece.height):
            grid.grid.insert(0, ['.' for _ in range(10)])

        grid_max_height = len(grid.grid)
        # Find empty position for the shape matrix in the grid
        _, offset, level = find_best_position(grid, start_column, piece, grid_max_height)
        grid.place_piece(piece, (level, start_column))

        # Clear the filled lines in Tetris grid
        for i in grid.completed_line():
            grid.clear_line(i)

        # Update the resulting height of the grid
        grid_height = len(grid.grid) - grid.unoccupied_line()

    return grid_height


def main():
    """
        Main: Reads input from a STDIN, processes each line using the tetris_engine function,
        and prints and writes the output height of tetris to another file.

        Parameters:
        - input_file_path: The path to the input file containing Tetris sequences.

        Returns:
        Height of current Tetris grid and output.txt file
    """
    output = 0
    try:
        output_file_path = 'output.txt'
        # Read input from STDIN
        input_lines = []
        # Open the output file in write mode
        with open(output_file_path, 'w') as output_file:
            # Iterate through each line
            for line in sys.stdin:
                input_lines.append(line.strip())
                # Call the tetris_engine function to process the Tetris sequence
                # Write the result to the output file and print it
                output_file.write(str(tetris_engine(line.strip())) + '\n')
                output = tetris_engine(line.strip())
                print(output)
    except Exception:
        print("Game has ended. Your total tetris height is " + str(output) + ".\nThank you!")


if __name__ == "__main__":
    """***********************Tetris engine started**********************
    Type comma-separated shapes and their position to insert in the game.
    Press any key and enter to end the game."""
    main()
