import os
import random

os.system("cls")

class Board():
	def __init__(self):
		self.cells = [" "," "," "," "," "," "," "," "," "," "]

	def display(self):
		print(" %s | %s | %s " %( self.cells[1], self.cells[2], self.cells[3] ))
		print("-----------")
		print(" %s | %s | %s " %( self.cells[4], self.cells[5], self.cells[6] ))
		print("-----------")
		print(" %s | %s | %s " %( self.cells[7], self.cells[8], self.cells[9] ))

	def update_cell(self,cell_no,player):
		if self.cells[cell_no] == " ":
			self.cells[cell_no] = player

	def is_winner(self,player):
		for combo in [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]:
			result = True
			for cell_no in combo:
				if self.cells[cell_no] != player:
					result = False

			if result == True:
				return True
		return False

	def is_tie(self):
		used_cells = 0
		for cell in self.cells:
			if cell!= " ":
				used_cells += 1
		if used_cells == 9:
			return True
		else:
			False

	def reset(self):
		self.cells = [" "," "," "," "," "," "," "," "," "," "]

	import random
	def ai_move(self,player):
		# Choose random
		while(True):

			# Simply iterates over the list and 
			# checks if the grid is full or not
			grid_full = True
			for i in self.cells:
				if i!=" ":
					grid_full = False

			# If the grid is full, it breaks out of while
			if grid_full:
				break
			# Get a random number
			r = random.randint(1, 9)
			# Check if its empty
			if self.cells[r] != " ":
				# If it is, reiterate the loop and look for another
				continue
			else:
				# If it is not, update the board
				self.update_cell(r, player)
				break

		# Sequential stuff, not needed
		# for i in range(1,10):
		# 	if self.cells[i]==" ":
		# 		self.update_cell(i,player)
		# 		break

board = Board()

def print_header():                                    # prints header
	print(" Welcome to Tic-Tac-Toe\n")

def refresh_screen():                                  # refresh screen function
	# clear the screen
	# Different OS use different commands so the if statement
	# https://stackoverflow.com/questions/1325581/how-do-i-check-if-im-running-on-windows-in-python
	if os.name == 'nt':
		# It is running on windows
		os.system("cls")
	else:
		# It is running on linux, most probably
		# Could also check for Mac
		os.system("clear")

	# print the header
	print_header()

	# show thw board
	board.display()

while True:
	refresh_screen()

	# Adding code to solve the problem when user enter a number already occupied
	x_choice = -1
	while(True):
		# getting X input 
		x_choice = int(input("\nX) Please choose 1 - 9. >"))

		if board.cells[x_choice] == " ":
			# cell at x_choice is empty
			break
		else:
			# cell at x_choice is not empty
			print("Cell already occupied, please choose another number")
			continue

	# update board
	board.update_cell(x_choice,"X")

	# refresh the screen
	refresh_screen()

	# check for an X wins
	if board.is_winner("X"):
		print("\nX wins!\n")
		play_again = input("Would you like to play again (Y/N) >").upper()
		if play_again=="Y":
			board.reset()
			continue
		else:
			break

	# check for a Tie 
	if board.is_tie():
		print("\nTie game!\n")
		play_again = input("Would you like to play again (Y/N) >").upper()
		if play_again=="Y":
			board.reset()
			continue
		else:
			break

	# getting O input 
	#o_choice = int(input("\nO) Please choose 1 - 9. >"))

	board.ai_move("O")

	# update board
	#board.update_cell(o_choice,"O")

	# refresh the screen
	refresh_screen()

	# check for an O wins
	if board.is_winner("O"):
		print("\nO wins!\n")
		play_again = input("Would you like to play again (Y/N) >").upper()
		if play_again=="Y":
			board.reset()
			continue
		else:
			break

	# check for a Tie 
	if board.is_tie():
		print("\nTie game!\n")
		play_again = input("Would you like to play again (Y/N) >").upper()
		if play_again=="Y":
			board.reset()
			continue
		else:
			break
