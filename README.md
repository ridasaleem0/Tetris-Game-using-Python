# Tetris Game using Python3

## Problem description

The engine models a grid that pieces enter from top and come to rest at the bottom, as if pulled down by gravity. Each piece is made up of four unit squares.
No two unit squares occupy the same space in the grid at the same time.
The pieces are rigid, and come to rest as soon as any part of a piece contacts the bottom of the grid or any resting block. As in Tetris, whenever an entire row of the grid is filled, it disappears, and any higher rows drop into the vacated space without any change to the internal pattern of blocks in any row.
The exe file process a text of lines each representing a sequence of pieces entering the grid.
For each line of the input programs output the resulting height of the remaining blocks within the grid.
The file denotes the different possible shapes by letter. The letters used are Q, Z, S, T, I, L, and J. The shapes of the pieces they represent are shown in the table below:

</td>
</tr>
</table>
<table>
  <tr>
    <td>Letter</td>
    <td>Q</td>
    <td>Z</td>
    <td>S</td>
    <td>T</td>
    <td>I</td>
    <td>L</td>
    <td>J</td>
  </tr>
  <tr>
    <td>Shape</td>
    <td>
      <pre>
##
##
      </pre>
    </td>
    <td>
      <pre>
##
 ##
      </pre>
    </td>
    <td>
      <pre>
 ##
##
      </pre>
    </td>
    <td>
      <pre>
###
 #
      </pre>
    </td>
    <td>
      <pre>
####
      </pre>
    </td>
    <td>
      <pre>
#
#
##
      </pre>
    </td>
    <td>
      <pre>
 #
 #
##
      </pre>
    </td>
  </tr>
</table>

The program does not validate its input for now and assumes that there will be no illegal characters
Moreover, the script does not account for shape rotation in your model. The pieces will always have the orientations shown above.
Each line of the input file is a comma-separated list.
Each entry in the list is a single letter (from the set above) and a single-digit integer. The integer represents the left-most column of the grid that the shape occupies, starting from zero.
The grid of the game space is 10 units wide. For each line of the file, the grid’s initial state is empty.

For example, if the input file consisted of the line “Q0” the corresponding line in the output file would be “2”, since the block will drop to the bottom of the initially empty grid and has height two.

## Examples

### Example 1

A line in the input file contains `I0,I4,Q8` resulting in the following configuration:

```
  I0 │          │ I4  │          │ Q8  │          │
     │          │ ──► │          │ ──► │        ##│
     │####      │     │########  │     │##########│
     └──────────┘     └──────────┘     └──────────┘
      0123456789       0123456789       0123456789

```

The filled bottom row then disappears:

```
│          │
│          │
│        ##│
└──────────┘
 0123456789
```

Therefore, the output row for this sequence is “1”.

### Example 2

A line in the input file contains `T1,Z3,I4`.

```

     │          │       │          │       │    ####  │
  T1 │          │  Z3   │   ##     │  I4   │   ##     │
     │ ###      │  ──►  │ #####    │  ──►  │ #####    │
     │  #       │       │  #       │       │  #       │
     └──────────┘       └──────────┘       └──────────┘
      0123456789         0123456789         0123456789

```

No rows are filled, so the output for this sequence is “4”.

# Solution Instructions - Tetris Game

## Overview
This repository contains a simple implementation of the classic Tetris game in Python.

## Dependencies
The Tetris game has the following dependencies:
- Python (version 3.x)

## Installation
To run the Tetris game, follow these steps:

1. Navigate to the project directory:
   ```bash
   cd tetris-game
   ```

2. Make the `tetris` script executable:
   ```bash
   chmod +x tetris.py
   ```

## Usage
Run the Tetris game with the following command:

Replace `input.txt` with your desired input, and the game output will be saved in `output.txt`.

## Gameplay
Additional information about how to play the game or special features.

### Starting the Game
To play the Tetris game, follow these steps:

1. Open a terminal window.

2. Navigate to the project directory:
   ```bash
   cd path/to/encord-be-assignment
3. To start the game with default settings, type in terminal:
   ```bash
   ./tetris <input.txt>
   
### Ending the Game
The game will end if any key is pressed, except for the required input format. Ensure that your input follows the specified format (e.g., Q2, S2) to continue playing.
The final score will be displayed, and the game will exit.

## Running Test Cases

You can test the Tetris game with predefined input scenarios. Follow these steps:

Ensure that the game is working correctly by running the provided test cases:

```bash
python3 sample_test.py
```
Please note that the subprocess.run command in sample_test.py may need modification.

1. Replace this line in sample_test.py:
   ```bash
   p = subprocess.run(
           ["/bin/bash", ENTRY_POINT],
           input=test_case.sample_input,
           capture_output=True,
       )
   ```
   With this line:
   
   ```bash
   p = subprocess.run(
           [ENTRY_POINT],
           input=test_case.sample_input,
           capture_output=True,
       )
   ```
2. Replace `ENTRY_POINT` in sample_test.py with `./tetris.py`.

