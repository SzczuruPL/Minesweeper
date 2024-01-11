import random


def get_number(min, max, text):
    while True:
        try:
            number = int(input(text))
            if min <= number <= max:
                return number
            else:
                print(f"Liczba powinna być z zakresu {min} do {max}.")
        except ValueError:
            print("Nieprawidłowe dane. Wpisz liczbę całkowitą.")


def lay_mines(board, mines_num, rows, cols):

    # Track of number of mines already set up
    count = 0
    while count < mines_num:

        # Random number from all possible grid positions
        val_r = random.randint(0, rows * rows - 1)
        val_c = random.randint(0, cols * cols - 1)

        # Generating row and column from the number
        row = val_r // rows
        col = val_c % cols

        # Place the mine, if it doesn't already have one
        if board[row][col] != -1:
            count = count + 1
            board[row][col] = -1

    return board


def number_of_neighboring_mines(board, rows, cols):

    # Loop for counting each cell value
    for row in range(rows):
        for col in range(cols):

            # Skip, if it contains a mine
            if board[row][col] == -1:
                continue

            # Check up
            if row > 0 and board[row - 1][col] == -1:
                board[row][col] = board[row][col] + 1
            # Check down
            if row < rows - 1 and board[row + 1][col] == -1:
                board[row][col] = board[row][col] + 1
            # Check left
            if col > 0 and board[row][col - 1] == -1:
                board[row][col] = board[row][col] + 1
            # Check right
            if col < cols - 1 and board[row][col + 1] == -1:
                board[row][col] = board[row][col] + 1
            # Check top-left
            if row > 0 and col > 0 and board[row - 1][col - 1] == -1:
                board[row][col] = board[row][col] + 1
            # Check top-right
            if row > 0 and col < cols - 1 and board[row - 1][col + 1] == -1:
                board[row][col] = board[row][col] + 1
            # Check below-left
            if row < rows - 1 and col > 0 and board[row + 1][col - 1] == -1:
                board[row][col] = board[row][col] + 1
            # Check below-right
            if row < rows - 1 and col < cols - 1 and board[row + 1][col + 1] == -1:
                board[row][col] = board[row][col] + 1

    return board


def create_board(mines_num, rows, cols):

    board = [[0 for c in range(cols)] for r in range(rows)]

    lay_mines(board, mines_num, rows, cols)

    number_of_neighboring_mines(board, rows, cols)

    return board


def reveal_fields(board_visible, board, visited, row, col):

    # If the cell already not visited
    if [row, col] not in visited:

        # Mark the cell visited
        visited.append([row, col])

        # If the cell is zero-valued
        if board[row][col] == 0:

            # Display it to the user
            board_visible[row][col] = board[row][col]

            # Recursive calls for the neighbouring cells
            if row > 0:
                reveal_fields(board_visible, board, visited, row - 1, col)
            if row < rows - 1:
                reveal_fields(board_visible, board, visited, row + 1, col)
            if col > 0:
                reveal_fields(board_visible, board, visited, row, col - 1)
            if col < cols - 1:
                reveal_fields(board_visible, board, visited, row, col + 1)
            if row > 0 and col > 0:
                reveal_fields(board_visible, board, visited, row - 1, col - 1)
            if row > 0 and col < cols - 1:
                reveal_fields(board_visible, board, visited, row - 1, col + 1)
            if row < rows - 1 and col > 0:
                reveal_fields(board_visible, board, visited, row + 1, col - 1)
            if row < rows - 1 and col < cols - 1:
                reveal_fields(board_visible, board, visited, row + 1, col + 1)

                # If the cell is not zero-valued
        if board[row][col] != 0:
            board_visible[row][col] = board[row][col]

    return board


def print_board(mine_values, rows, cols):

    st = "  "
    for i in range(cols):
        if i < 10:
            st = st + "   " + str(i + 1)
        else:
            st = st + "  " + str(i + 1)
    print(st)

    for row in range(rows-1):
        st = "   ╔"
        if row == 0:
            for col in range(cols-1):
                st = st + "═══╦"
            st = st + "═══╗"
            print(st)

        if row < 9:
            st = " " + str(row + 1) + " "
        else:
            st = str(row + 1) + " "
        for col in range(cols):
            st = st + "║ " + str(mine_values[row][col]) + " "
        print(st + "║")

        st = "   ╠"
        for col in range(cols-1):
            st = st + "═══╬"
        print(st + '═══╣')

    st = str(row + 2) + " "
    for col in range(cols):
        st = st + "║ " + str(mine_values[row+1][col]) + " "
    print(st + "║")

    st = "   ╚"
    for col in range(cols - 1):
        st = st + "═══╩"
    print(st + '═══╝\n')


def check_over(mine_values, rows, cols, mines_num):

    count = 0

    for row in range(rows):
        for col in range(cols):

            if mine_values[row][col] != ' ' and mine_values[row][col] != 'F':
                count = count + 1

    if count == rows * cols - mines_num:
        return True
    else:
        return False