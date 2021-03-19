import math 
import numpy as np
#define Board 
class Board:
    # Constructor
    def __init__(self):
        #list to stoe board 
        self.board = []

    # fucntion to add matrix to board 
    def addBoard(self, u):
        self.board = u

    def takeSecond(self, elem):
        return elem[1]

    def getQueenPosition(self):   #get list of queens position 
        queen_position_list = []
        for index, row in enumerate(self.board):
            for i, value in enumerate(row):
                if value == "Q":
                    queen_position_list.append((index+1, i+1))
                    queen_position_list.sort(key=self.takeSecond)     #Reference: https://www.programiz.com/python-programming/methods/list/sort
        return queen_position_list

    def get_h_cost(self):         #get heuristic cost of each square in chess board
        heuristic_list = np.zeros((8,8)) 
        queen_position_list = self.getQueenPosition()
        for i in range(1,9):          # i is column 
            for j in range(1,9):      # y is row
                position_copy = queen_position_list.copy()          #create a copy of  queen_position_list
                position_copy.remove(queen_position_list[i-1])      # remove the 1st queen from queen_position_list and 
                position_copy.append((j,i))                         # append queen to position_copy 
                position_copy.sort(key=self.takeSecond)             # sort the position of the queens by column from left to right
                heuristic = 0 
                for index_attack, attack_queen in enumerate(position_copy):
                    row_attack, column_attack = attack_queen       # position of attack queen
                    for index_attacked in range(column_attack, 9):
                        row_attacked, column_attacked = position_copy[index_attacked -1]     # position of attacked queen   
                        if column_attack < index_attacked:   #avoid it calculate some attacking pair many times.
                            # compare the position of attack queen and attacked queen, if they can attack each other heuristic +1  
                            if row_attack == row_attacked or row_attack - column_attack == row_attacked - column_attacked or row_attack + column_attack == row_attacked + column_attacked:     
                                heuristic += 1 
                        heuristic_list[j-1][i-1] = heuristic   
        #print (heuristic_list) 
        # create a heuristic board  
        heuristic_board = []     
        for it in heuristic_list:
            heu_list = []
            for j in it:
                heu_list.append((str(int(j))))
            heuristic_board.append(heu_list)
        
        # Fill Q in the position as the original input
        for row_index, row in enumerate(heuristic_board):
            row_index +=1
            for column_index, column in enumerate(row):
                column_index += 1
                if (row_index, column_index) in queen_position_list:   
                    heuristic_board[row_index-1][column_index-1] = "Q"

    #     print('\n'.join([''.join([' {:4}'.format(str(item)) for item in row]) 
    #   for row in heuristic_board]))
    #Reference: https://stackoverflow.com/questions/17870612/printing-a-two-dimensional-array-in-python/36538558
        return ('\n'.join([''.join([' {:2}'.format(str(item)) for item in row]) 
      for row in heuristic_board]))
        
    

b  = Board()
board = []
# Driver code 
f = open("input.txt", "r")
for line in f:
    #u, v = [int(it) for it in line.strip().split(' ')]
        #for i in line:
            # a = []
            board.append([it for it in line.strip().split(' ')])

f.close()

b.addBoard(board)

print(b.get_h_cost())

h = open("output.txt","w")
for it in b.get_h_cost():
    h.write(it)
h.close()