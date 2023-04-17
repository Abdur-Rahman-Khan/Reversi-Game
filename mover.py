import core
import copy

def get_move(board, player):
    return get_move_greedy(board, player)
   
def get_move_greedy(board,player):
    # test.print_board(board)
    board_copy = copy.deepcopy(board)
    valid_moves = core.get_valid_moves(board_copy,player)
    if len(valid_moves) == 0:
        return "NO MOVES"
    else:
        #iterate on all moves
        bestMove = valid_moves[0]
        minScore=  core.get_score(board)[player]
        for move in valid_moves:
            board_copy = copy.deepcopy(board)
            core.make_move(board_copy,move[0],move[1],player)
            #check if move is better
            print("move is: ",move," score is: ",core.get_score(board_copy)[player])
            if core.get_score(board_copy)[player] > minScore:
                bestMove = move
                minScore = core.get_score(board_copy)[player]
                print("best move is: ",bestMove)
        bestMove = convertToTuple(bestMove)
        return bestMove
    
#convert (2,2) to (c3)
def convertToTuple(move):
    x = chr(move[0]+97)
    y = move[1]+1
    return x+str(y)

