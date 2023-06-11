test = False
if test:
    data_file = 'data/day4/input_test'
else:
    data_file = 'data/day4/input'


# Function to check if a board has a completed row or column
def has_won(board):
    # Check rows
    for row in board:
        if all(cell is None for cell in row):
            return True

    # Check columns
    for j in range(5):
        if all(board[i][j] is None for i in range(5)):
            return True

    return False


# Reading data from file
with open(data_file) as file:
    numbers_called = list(map(int, file.readline().strip().split(',')))
    boards = []

    # Skip empty lines before the first board
    line = file.readline()
    while not line.strip():
        line = file.readline()

    # Read boards
    while line:
        board = []
        # Read rows of the current board
        for _ in range(5):
            if line.strip():  # Ignore empty lines
                row = [int(x) for x in line.split() if x.isdigit()]
                board.append(row)
            line = file.readline()
        boards.append(board)

        # Skip empty lines between boards, but make sure we don't get stuck in an infinite loop
        while line and not line.strip():
            line = file.readline()

# Debugging prints to see what was read into boards
# Used for printing out boards

# for idx, board in enumerate(boards):
#     print(f"Board {idx + 1}:")
#     for row in board:
#         print(row)

# PART 1
# Variables to store the results of the first winning board
first_winning_board = None
first_unmarked_sum = None
first_number = None

# Variables to store the results of the last winning board
last_winning_board = None
last_unmarked_sum = None
last_number = None

# Keep track of boards that have won
won_boards = set()

# Simulate the game
for number in numbers_called:
    for board_index, board in enumerate(boards):
        # Check if this board has already won
        if board_index in won_boards:
            continue

        # Mark only the number that has been called
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == number:
                    board[i][j] = None

        # Check if this board has won
        if has_won(board):
            # Calculate the sum of unmarked numbers
            unmarked_sum = sum(cell for row in board for cell in row if cell is not None)

            # Store results for the first winning board
            if first_winning_board is None:
                first_winning_board = board_index + 1
                first_unmarked_sum = unmarked_sum
                first_number = number

            # Store results for the last winning board
            last_winning_board = board_index + 1
            last_unmarked_sum = unmarked_sum
            last_number = number

            # Mark this board as having won
            won_boards.add(board_index)

    # Exit early if all boards have won
    if len(won_boards) == len(boards):
        break

# Output the results for Part 1
print("## PART 1 ##")
score1 = first_unmarked_sum * first_number
print(f"The winning board is board number {first_winning_board}")
print(f"The unmarked sum is: {first_unmarked_sum}")
print(f"The number is: {first_number}")
print(f"The score is: {score1}")

# Output the results for Part 2
print("## PART 2 ##")
score2 = last_unmarked_sum * last_number
print(f"The last winning board is board number {last_winning_board}")
print(f"The unmarked sum is: {last_unmarked_sum}")
print(f"The number is: {last_number}")
print(f"The score is: {score2}")