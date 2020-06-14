#import block
import random
import time

board = {}
empty_places=[1,2,3,4,5,6,7,8,9]
def initialize_board():
    for i in range(1,10):
        board[i]=" "
    


def game_board():
    print(board[1],"|",board[2],"|",board[3],"\t1 | 2 | 3")
    print("--+---+--"+"\t"+"--+---+--")
    print(board[4],"|",board[5],"|",board[6],"\t4 | 5 | 6")
    print("--+---+--"+"\t"+"--+---+--")
    print(board[7],"|",board[8],"|",board[9],"\t7 | 8 | 9")


def check_winner():
    if (
        (board[1]==board[2]==board[3]!=" ") or (board[4]==board[5]==board[6]!=" ") or (board[7]==board[8]==board[9]!=" ")
        ):
        return True
    elif (
        (board[1]==board[4]==board[7]!=" ") or (board[2]==board[5]==board[8]!=" ") or (board[3]==board[6]==board[9]!=" ")
        ):
        return True
    elif (
        (board[1]==board[5]==board[9]!=" ") or (board[7]==board[5]==board[3]!=" ")
        ):
        return True
    else:
        return False
    

def choose(turn,symbol,flag):
    while True:
        message=turn+" choose from Available places "+str(empty_places)+" : "
        choosen = int(input(message))
        if choosen in empty_places:
            board[choosen]=symbol
            break
        elif(choosen in range(1,10)):
            print("Value choosen is occupied")
        else:
            print("Value choosen is invalid")
    empty_places.remove(choosen)
    game_board()
    #print("flag",flag)
    if flag>3:
            if (check_winner()):
                print("Winner is ",turn)
                return True
            elif flag==8:
                print("It is a tie")
                return False

    

    


def main():
    print("TIC_TAC_TOE")
    print("Enter player details")
    player1_name = input("Player 1: ")
    player2_name = input("Player 2: ")
    score_card = {player1_name:0,player2_name:0}
    new_game = True
    while new_game == True:
        initialize_board()
        print("Heads is for ",player1_name)
        print("Tails is for ",player2_name)
        print("Tossing coin to decide who will go first")
        coin = random.randint(1,2)
        if coin == 1:
            coin = 'Heads'
            first = player1_name
            second = player2_name
        else:
            coin = 'Tails'
            first = player2_name
            second = player1_name
        for i in range(3):
            print("H|T")
            time.sleep(.33)
        print(coin," means ",first," will go first and have symbol 'O'" )
        print("SCORECARD")
        print(score_card)
        game_board()
        flag=0
        status=choose(first,"O",flag)
        
        for i in range(4):
            if status==True:
                score_card[first]=score_card[first]+1
                break
            flag=flag+1
            #print('f',flag)
            status = choose(second,"X",flag)
            if status==True:
                score_card[second]=score_card[second]+1
                break
            flag=flag+1
            #print('f',flag)
            status = choose(first,"O",flag)
        
        new_game=input("Do you want to play again y|Y|yes|YES -- ")
        if new_game in ['y','yes','Y','YES']:
            empty_places.clear()
            empty_places.extend([1,2,3,4,5,6,7,8,9])
            new_game = True
        else:
            print("SCORECARD")
            print(score_card)
            new_game = False
    

    
if __name__=="__main__": 
    main() 
    #game_board()