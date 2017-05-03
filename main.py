'''
Created on May 2, 2017

@author: Ryan
'''
moves = [1,2,3,4,5,6,7,8,9]
player = 1
PLAYER1_TOKEN = 'X'
PLAYER2_TOKEN = 'O'

def draw_board(board):
    
    print '\n\n'
    print '    |    |'
    print '  ' + str(board[6]) + ' | ' + str(board[7]) +  '  | ' + str(board[8])
    print '    |    |'
    print '--------------'
    print '    |    |'
    print '  ' + str(board[3]) + ' | ' + str(board[4]) +  '  | ' + str(board[5])
    print '    |    |'
    print '--------------'
    print '    |    |'
    print '  ' + str(board[0]) + ' | ' + str(board[1]) +  '  | ' + str(board[2])
    print '    |    |'
    
    
def play_game():
    
    print 'Welcome to TicTacToe1'
    draw_board(moves)
    
    print '\n\nPlayer 1 will be X'
    print 'Player 2 will be O'
    
    take_turn(player)
    
def take_turn(player):
    
    player_input = raw_input('Please enter the number where you would like to move.\n')
    moves[int(player_input)-1] = PLAYER1_TOKEN
    draw_board(moves)
    
    

play_game()