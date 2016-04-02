#!/usr/bin/env python

winning_positions = ([0,4,8],[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8],[2,4,6])
global board
board = [' ']* 9 
global available_positions
available_positions = [0,1,2,3,4,5,6,7,8]
global priority_positions
priority_positions = [4,1,3,5,7]

def find_all():
	newlist1 = []
	newlist2 = []
	newlist3 = []
	newlist4 = []
	for i in range(len(scoresdict)):
		if scoresdict[i][1] == 2:
			for x in scoresdict[i][0]:
				newlist1.append(x)
	for i in range(len(scoresdict)):
		if scoresdict[i][1] == -2:
			for x in scoresdict[i][0]:
				newlist2.append(x)
	for i in range(len(scoresdict)):
		if scoresdict[i][1] == 1:
			for x in scoresdict[i][0]:
				newlist3.append(x)
	for i in range(len(scoresdict)):
		if scoresdict[i][1] == -1:
			for x in scoresdict[i][0]:
				newlist3.append(x)
	if len(newlist1) > 0:
		return newlist1
	if len(newlist2) > 0:
		return newlist2
	if len(newlist3) > 0:
		return newlist3
	if len(newlist4) > 0:
		return newlist4


class Player:
	def __init__(self, Variable):
		self.variable = Variable
	def myturn(self, x_ord):
		board[ x_ord ] = self.variable




def update_duplicate_scores(variable, position, scoreslist):
	if variable == comp_var:
		for i in range(len(scoreslist)):
			if position in scoreslist[i][0]:
				scoreslist[i][1] = scoreslist[i][1] + 1
	if variable == player_var:
		for i in range(len(scoreslist)):
			if position in scoreslist[i][0]:
				scoreslist[i][1] = scoreslist[i][1] - 1
	return scoreslist

def Update_Scores(variable, position):
	if variable == comp_var:
		for i in range(len(scoresdict)):
			if position in scoresdict[i][0]:
				scoresdict[i][1] = scoresdict[i][1] + 1
	if variable == player_var:
		for i in range(len(scoresdict)):
			if position in scoresdict[i][0]:
				scoresdict[i][1] = scoresdict[i][1] - 1
	
def find_pos(templist):
	temp = [x for x in available_positions if x in templist]
	return temp

def init_scores():
	global scoresdict
	scoresdict = {}
	for i in range(len(winning_positions)):
		scoresdict[i] = [winning_positions[i],0]

def play_Computer():
	ret_list = find_all()
	ret_list = list(set(ret_list))
	bestlist = find_pos(ret_list)
	print 'Bestlist' , bestlist
	pr_list = [x for x in priority_positions if x in bestlist]
	print 'pr_list', pr_list
	if len(pr_list) == 0:
		return bestlist[0]
	else:
		return pr_list[0]


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
		player_var = 'O'
		global comp_var
		comp_var = 'X'
		user = Player('O')
		##PLayer PLays##
		print "Player turn...Input Square No.."
		player_chose_position = int(raw_input())
		available_positions.remove(player_chose_position)
		user.myturn(player_chose_position)
		Update_Scores(player_var, player_chose_position)
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
		print scoresdict
		display()
		if Check_Win(comp_var):
			print "\t\t\t COMPUTER WINS...."
			break

if __name__ == "__main__": main()
