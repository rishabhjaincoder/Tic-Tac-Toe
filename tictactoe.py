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

	def ai_move(self,player):
		# Choose random
		for i in range(1,10):
			if self.cells[i]==" ":
				self.update_cell(i,player)
				break

board = Board()

def print_header():                                    # prints header
	print(" Welcome to Tic-Tac-Toe\n")

def refresh_screen():                                  # refresh screen function
	# clear the screen
	os.system("cls")

	# print the header
	print_header()

	# show thw board
	board.display()

while True:
	refresh_screen()

	# getting X input 
	x_choice = int(input("\nX) Please choose 1 - 9. >"))

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
