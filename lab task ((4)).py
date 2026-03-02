# Lab 4 - N Queens Problem using Backtracking (Dynamic Size)

def show_board(chess, size):
    print()
    for r in range(size):
        line = ""
        for c in range(size):
            if chess[r][c] == 1:
                line += " Q "
            else:
                line += " . "
        print(line)
    print()


def check_position(chess, r, c, size):
    
    # Check left side of same row
    for i in range(c):
        if chess[r][i] == 1:
            return False

    # Check upper-left diagonal
    i, j = r, c
    while i >= 0 and j >= 0:
        if chess[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = r, c
    while i < size and j >= 0:
        if chess[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def place_queens(chess, column, size):
    
    # Base condition: all queens placed
    if column == size:
        return True

    # Try placing queen in each row of current column
    for r in range(size):

        if check_position(chess, r, column, size):
            
            chess[r][column] = 1
            print(f"Queen placed at (Row {r+1}, Column {column+1})")

            # Recursively place next queen
            if place_queens(chess, column + 1, size):
                return True

            # Backtracking step
            chess[r][column] = 0
            print(f"Backtracking from (Row {r+1}, Column {column+1})")

    return False


# -------- Main Program --------
n = int(input("Enter the value of N (number of queens): "))

# Create empty chess board
board = [[0 for _ in range(n)] for _ in range(n)]

print("\nSolving", n, "- Queens Problem")
print("=" * 40)

if place_queens(board, 0, n):
    print("\nFinal Solution:")
    show_board(board, n)
else:
    print("\nNo solution possible for given N")