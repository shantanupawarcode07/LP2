global N
N = 4
ld = [0] * 30
rd = [0] * 30
cl = [0] * 30
def printSolution(board):
	for i in range(N):
		for j in range(N):
			print(" Q " if board[i][j] == 1 else " . ", end="")
		print()
def solveNQUtil(board, col):
	if col >= N:
		return True
	for i in range(N):
		if (ld[i - col + N - 1] != 1 and rd[i + col] != 1) and cl[i] != 1:
			board[i][col] = 1
			ld[i - col + N - 1] = rd[i + col] = cl[i] = 1
			if solveNQUtil(board, col + 1):
				return True
			board[i][col] = 0
			ld[i - col + N - 1] = rd[i + col] = cl[i] = 0
	return False
def solveNQ():
	board = [[0 for _ in range(N)] for _ in range(N)]
	if not solveNQUtil(board, 0):
		print("Solution does not exist")
		return False
	printSolution(board)
	return True
# Driver program to test above function
if __name__ == "__main__":
	solveNQ()


# This code is an implementation of the N-Queens problem, a classic problem in computer science where you need to place N chess queens on an N×N chessboard in such a way that no two queens threaten each other. In this implementation, the goal is to find one such placement of queens.

# Let's break down the code step by step:

# solveNQUtil(board, col): This is a recursive function that tries to place a queen in each column col of the board. It returns True if it is able to place all queens, otherwise False. board is the current state of the chessboard, col is the current column being processed.
# if col >= N: return True: This condition checks if all queens are placed successfully, i.e., if col has reached or exceeded N.
# for i in range(N): This loop iterates through each row (i) in the current column (col) to try placing a queen.
# if (ld[i - col + N - 1] != 1 and rd[i + col] != 1) and cl[i] != 1:: This condition checks if it's safe to place a queen at position (i, col). It checks three things:
# ld[i - col + N - 1] != 1: This checks if there is no queen attacking from the left diagonal.
# rd[i + col] != 1: This checks if there is no queen attacking from the right diagonal.
# cl[i] != 1: This checks if there is no queen attacking from the same row.
# If all conditions are met, it marks the position (i, col) as a safe place to put a queen, and recursively calls solveNQUtil for the next column (col + 1).
# If solveNQUtil returns True, it means all queens are placed successfully, so it returns True to its caller.
# If solveNQUtil does not find a solution for the current column, it resets the position (i, col) and continues the loop to try the next row.
# solveNQ(): This function initializes an empty chessboard (board) and starts the recursion by calling solveNQUtil(board, 0) to place queens on the board starting from column 0.
# If solveNQUtil returns False, it means no solution exists, so it prints "Solution does not exist" and returns False.
# If solveNQUtil returns True, it means a solution was found. It then calls printSolution(board) to print the board configuration and returns True
