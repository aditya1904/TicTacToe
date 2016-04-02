#!/usr/bin/env python

winning_positions = ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6])
global board
board = [' ']* 9 
class Player:
	def __init__(self, Variable):
		self.variable = Variable
	def myturn(self, x_ord ):
		board[ x_ord ] = self.variable

def Check_Win(variable):
	win = False
	for i in range(len(winning_positions)):
		a,b,c = winning_positions[i]
		if board[a] == board[b] and board[b]==board[c] and board[c]==variable:
			win = True
			break
	return win

def display():
	print board[0], '|', board[1], '|', board[2]
	print '----------'
	print board[3], '|', board[4], '|', board[5]
	print '----------'
	print board[6], '|', board[7], '|', board[8]

def main():
	display()
	while True:
		Player1 = Player('X')
		Player2 = Player('O')
		print "Player 1 turn..."
		Player1.myturn(int(raw_input())
		display()
		if Check_Win(Player1.variable):
			print 'Player 1 wins'
			break
		print "Player 2 turn..."
		Player2.myturn(int(raw_input())
		display()
		if Check_Win(Player2.variable):
			print 'Player  2 wins'
			break
main()
