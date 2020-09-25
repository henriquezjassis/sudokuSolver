
board = [
	[7,8,0,4,0,0,1,2,0],
	[6,0,0,0,7,5,0,0,9],
	[0,0,0,6,0,1,0,7,8],
	[0,0,7,0,4,0,2,6,0],
	[0,0,1,0,5,0,9,3,0],
	[9,0,4,0,6,0,0,0,5],
	[0,7,0,3,0,0,0,1,2],
	[1,2,0,0,0,7,4,0,0],
	[0,4,9,2,0,6,0,0,7]
]

def is_valid(b, pos, num):
	print(pos)
	print(b[pos[0]][:])
	print(b[:][pos[1]])


	box = (pos[0] // 3, pos[1] // 3) # Finds out wich box we're in
	print(box)
	#Check Row
	if(num in b[pos[0]][:]):
		return False

	#Check Column
	for i in range(len(b)):
		if( b[i][pos[1]] == num):
			return False

	#Check Box
	for i in range(3):
		for j in range(3):
			if b[i + box[0]][j + box[1]]:
				return False

	return True


def print_sudoku(b):
	for i in range(len(b)):
		if (i % 3) == 0 :
			print(" - "*13)
		for j in range(len(b[i])):
			if (j % 3) == 0:
				print(" | ",end="")

			print(f" {b[i][j]} ",end="")

		print(" | ") # print new line.
	print(" - "*13)


def find_next_empty(b):
	for i in range(len(b)):
		for j in range(len(b[i])):
			if b[i][j] == 0:
				return (i,j)

	return False

if (__name__ == "__main__"):
	print_sudoku(board)
	x = find_next_empty(board)
	print(is_valid(board, x, 6))