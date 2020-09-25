import time
import sys
import os

board = [
	[2,0,0,0,0,1,4,0,0],
	[7,0,0,0,9,0,0,0,0],
	[0,3,0,0,5,6,0,0,2],
	[0,7,0,2,1,8,5,0,6],
	[1,0,2,0,0,5,9,3,0],
	[0,6,0,0,0,9,0,0,0],
	[6,0,0,0,8,0,0,0,0],
	[9,0,0,5,0,3,8,0,0],
	[4,1,8,0,2,0,0,6,5]
]

def resolv_sudoku(b):
	pos = find_next_empty(b)
	if(pos != False):
		for i in range(1, len(b)+1):
			# print(f"{i}")
			# print(is_valid(b, pos, i))

			if(is_valid(b, pos, i)):
				b[pos[0]][pos[1]] = i
				os.system("clear")
				print_sudoku(b)
				sys.stdout.flush()
				time.sleep(0.2)
				if(resolv_sudoku(b)):
					return True
				else:
					b[pos[0]][pos[1]] = 0
					print_sudoku(b)
					continue

		return False
	else:
		return True


def is_valid(b, pos, num):
	# print(pos)
	# print(b[pos[0]][:])
	# print(b[:][pos[1]])

	box = (pos[0] // 3, pos[1] // 3) # Finds out wich box we're in
	# print(box)
	#Check Row
	for i in range(len(b)):
		if( b[pos[0]][i] == num):
			return False

	# print("Passou Row")
	#Check Column
	for i in range(len(b)):
		if( b[i][pos[1]] == num):
			return False

	# print("Passou Column")
	#Check Box
	for i in range(3):
		for j in range(3):
			if b[i + box[0]*3][j + box[1]*3] == num:
				return False

	return True


def print_sudoku(b):
	# for i in range(len(b)):
	# 	if (i % 3) == 0 :
	# 		print(" - "*13, end="\r")
	# 	for j in range(len(b[i])):
	# 		if (j % 3) == 0:
	# 			print(" | ",end="")

	# 		print(f" {b[i][j]} ",end="")

	# 	print(" | ") # print new line.
	# print(" - "*13)

	aux = []

	for i in range(len(b)):
		for j in range(len(b[i])):
			aux.append(b[i][j])

	print('''
		 - - - - - - - - - - - - -
		 | {} {} {} | {} {} {} | {} {} {} |
		 | {} {} {} | {} {} {} | {} {} {} |					 
		 | {} {} {} | {} {} {} | {} {} {} |
		 - - - - - - - - - - - - -
		 | {} {} {} | {} {} {} | {} {} {} |
		 | {} {} {} | {} {} {} | {} {} {} |
		 | {} {} {} | {} {} {} | {} {} {} |
		 - - - - - - - - - - - - - 
		 | {} {} {} | {} {} {} | {} {} {} |
		 | {} {} {} | {} {} {} | {} {} {} |
		 | {} {} {} | {} {} {} | {} {} {} |
		 - - - - - - - - - - - - -
		'''.format(*aux), end="\r")


def find_next_empty(b):
	for i in range(len(b)):
		for j in range(len(b[i])):
			if b[i][j] == 0:
				return (i,j)

	return False

if (__name__ == "__main__"):
	print_sudoku(board)
	resolv_sudoku(board)