#!/usr/bin/env python

winning_positions = ([0,4,8],[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8],[2,4,6])
global board
board = [' ']* 9 
global available_positions
available_positions = [0,1,2,3,4,5,6,7,8]
global priority_positions
priority_positions = [4,1,3,5,7]

class Player:
	def __init__(self, Variable):
		self.variable = Variable
	def myturn(self, x_ord):
		board[ x_ord ] = self.variable

def Update_Scores(variable, position):
	if variable == comp_var:
		for i in range(len(scoresdict)):
			if position in scoresdict[i][0]:
				scoresdict[i][1] = scoresdict[i][1] + 1
	if variable == player_var:
		for i in range(len(scoresdict)):
			if position in scoresdict[i][0]:
				scoresdict[i][1] = scoresdict[i][1] - 1
	
def Update_Scoredict():
	for i in range(len(scoresdict)):
		temp = [ x for x in available_positions if x in scoresdict[i]]
		if len(temp) == 0:
			del scoresdict[i]
def play_Computer():
	for i in range(len(scoresdict)):
		if scoresdict[i][1] == 2:
			print 'Selected COmbo',scoresdict[i][0]
			print 'Score', scoresdict[i][1]
			pos_avail = find_pos(scoresdict[i][0])
			print 'returned position', pos_avail
			return pos_avail
	for i in range(len(scoresdict)):
		if scoresdict[i][1] == -2:
			print 'Selected COmbo',scoresdict[i][0]
			print 'Score', scoresdict[i][1]
			pos_avail = find_pos(scoresdict[i][0])
			print 'returned position', pos_avail
			return pos_avail
	for i in range(len(scoresdict)):
		if scoresdict[i][1] == 1:
			print 'Selected COmbo',scoresdict[i][0]
			print 'Score', scoresdict[i][1]
			pos_avail = find_pos(scoresdict[i][0])
			print 'returned position', pos_avail
			return pos_avail
	for i in range(len(scoresdict)):
		if scoresdict[i][1] == -1:
			print 'Selected COmbo',scoresdict[i][0]
			print 'Score', scoresdict[i][1]
			pos_avail = find_pos(scoresdict[i][0])
			print 'returned position', pos_avail
			return pos_avail
	
	
def find_pos(templist):
	temp = [x for x in available_positions if x in templist]
	print 'Available Positions', temp
	if len(temp) == 1:
		return temp[0]
	temp2 = [x for x in priority_positions if x in temp]
	print 'Available from priority', temp2
	if len(temp2) == 0:
		return temp[0]
	else:
		return temp2[0]

def init_scores():
	global scoresdict
	scoresdict = {}
	for i in range(len(winning_positions)):
		scoresdict[i] = [winning_positions[i],0]

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
	init_scores()
	while True:
		global player_var
		player_var = 'X'
		global comp_var
		comp_var = 'O'
		user = Player('X')
		##PLayer PLays##
		print "Player turn...Input Square No.."
		player_chose_position = int(raw_input())
		available_positions.remove(player_chose_position)
		user.myturn(player_chose_position)
		Update_Scores(player_var, player_chose_position)
#		Update_Scoredict()
		print scoresdict
		display()
		if Check_Win(player_var):
			print "\t\t\t YOU WIN !!!!"
			break
	##Computer Plays##
		print "My turn...Thinking..."
		comp_chose_position = play_Computer()
		board[comp_chose_position] = comp_var
		available_positions.remove(comp_chose_position)
		Update_Scores(comp_var, comp_chose_position)
#		Update_Scoredict()
		print scoresdict
		display()
		if Check_Win(comp_var):
			print "\t\t\t COMPUTER WINS...."
			break

if __name__ == "__main__": main()
