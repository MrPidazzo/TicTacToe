'''
Created on May 2, 2017

@author: Ryan
'''
moves = [1,2,3,4,5,6,7,8,9]
player = 1
PLAYER1_TOKEN = 'X'
PLAYER2_TOKEN = 'O'
game_won = False

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
    
    while not game_won:
        take_turn(player)
    
def take_turn(current_player):
    global player
    if current_player == 1:
        moves[get_input()-1] = PLAYER1_TOKEN
        draw_board(moves)
        player = 2
    elif current_player == 2:
        moves[get_input()-1] = PLAYER2_TOKEN
        draw_board(moves)
        player = 1
        
    
def get_input():
    print "\n\nIt is player {x}'s turn".format(x=str(player))
    player_input = raw_input('Please enter the number where you would like to move.\n')
    return int(player_input)
    
def is_game_won(game_won):
    pass
    
    

play_game()

