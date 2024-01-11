import minesweeper

def saper():

    print("Witaj w grze Saper!")
    cols = minesweeper.get_number(8, 24, "Podaj liczbę kolumn planszy (od 8 do 24): ")
    rows = minesweeper.get_number(8, 30, "Podaj liczbę wierszy planszy (od 8 do 30): ")
    max_mines = (rows - 1) * (cols - 1)
    mines_num = minesweeper.get_number(10, max_mines, f"Podaj liczbę min (od 10 do {max_mines}): ")
    print(f"Rozpoczynamy grę z planszą o wymiarach {rows}x{cols} i {mines_num} minami.\n")

    board = minesweeper.create_board(mines_num, rows, cols)

    board_visible = [[' ' for c in range(cols)] for r in range(rows)]

    over = False

    while not over:
        minesweeper.print_board(board_visible, rows, cols)

        # Input from the user
        inp = input("Wprowadź wiersz i kolumnę (format: W K) = ").split()

        # Standard input
        if len(inp) == 2:

            try:
                val = list(map(int, inp))
            except ValueError:
                print("Błędny format danych!")
                continue

        else:
            print("Błedny format danych!")
            continue

        # Sanity checks
        if val[0] > rows or val[0] < 1 or val[1] > cols or val[1] < 1:
            print("Wartość poza zakresem!")
            continue

        # Get row and column number
        row = val[0] - 1
        col = val[1] - 1

        if board_visible[row][col] != ' ':
            print("Pole zostało już odkryte!")
            continue

        # If landing on a mine --- GAME OVER
        if board[row][col] == -1:
            board_visible[row][col] = 'X'
            minesweeper.print_board(board_visible, rows, cols)
            print("Przegrałeś!")
            over = True
            continue

        # If landing on a cell with 0 mines in neighboring cells
        elif board[row][col] == 0:
            visible = []
            board_visible[row][col] = '0'
            minesweeper.reveal_fields(board_visible, board, visible, row, col)

        # If selecting a cell with at least 1 mine in neighboring cells
        else:
            board_visible[row][col] = board[row][col]

        # Check for game completion
        if minesweeper.check_over(board_visible, rows, cols, mines_num):
            minesweeper.print_board(board_visible, rows, cols)
            print("Chociaż raz coś ci się w życiu udało")
            over = True
            continue

saper()