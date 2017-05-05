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
       
    print 'Welcome to TicTacToe!'
    draw_board(moves)
    
    print '\n\nPlayer 1 will be X'
    print 'Player 2 will be O'
    
    while not game_won:
        take_turn(player)
    else:
        print_winner()
        exit()
                           
def take_turn(current_player):
    
    if current_player == 1:
        moves[get_input()-1] = PLAYER1_TOKEN
        draw_board(moves)
        is_game_won()

        
    elif current_player == 2:
        moves[get_input()-1] = PLAYER2_TOKEN
        draw_board(moves)
        is_game_won()

        
        
    
def get_input():
    
    valid_move = False
    print "\n\nIt is player {x}'s turn".format(x=str(player))
   
    while not valid_move:
        player_input = raw_input('Please enter the number where you would like to move.\n')
        if moves[int(player_input)-1] == PLAYER1_TOKEN or moves[int(player_input)-1] == PLAYER2_TOKEN:
            print 'That move is no longer available please try again.'
        else:
            valid_move = True
    return int(player_input)
    
def is_game_won():
    '''
    Winning combos
    1-2-3
    4-5-6
    7-8-9
    7-4-1
    8-5-2
    9-6-3
    1-5-9
    7-5-3
    '''
    global game_won
    global player
    
    if moves[0] == moves[1] and moves[0] == moves[2]:
        game_won = True
    elif moves[3] == moves[4] and moves[0] == moves[5]:
        game_won = True
    elif moves[6] == moves[7] and moves[6] == moves[8]:
        game_won = True
    elif moves[6] == moves[3] and moves[6] == moves[0]:
        game_won = True
    elif moves[7] == moves[4] and moves[7] == moves[1]:
        game_won = True
    elif moves[8] == moves[5] and moves[8] == moves[2]:
        game_won = True
    elif moves[0] == moves[4] and moves[0] == moves[8]:
        game_won = True
    elif moves[6] == moves[4] and moves[6] == moves[2]:
        game_won = True
    else:
        if player == 1:
            player = 2
        elif player == 2:
            player = 1
        
def print_winner():
    
    print '\n\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
    print 'Player {x} is the winner!!!'.format(x=str(player))
    print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
    
    

play_game()

