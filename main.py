from abc import ABC, abstractmethod
import copy

      
class piece(ABC):
    def __init__(self,space:str,life:bool,potential_moves,color:str):
        self.space:str = space
        self.life = life
        self.potential_moves = potential_moves
        self.color:str = color
    @abstractmethod
    def check_check(self):
        pass
    def check_moves(self):
        pass
    def move(self):
        pass
    def take(self):
        pass
    def upgrade(self):
        pass
    def self_ID(self):
        pass
class pawn(piece):
    def check_check(self):
        pass
    def check_moves(self):
        pass
    def move(self):
        pass
    def take(self):
        pass
    def upgrade(self):
        pass
    def self_ID(self):
        pass
class rook(piece):
    def check_check(self):
        pass
    def check_moves(self):
        pass
    def move(self):
        pass
    def take(self):
        pass
    def upgrade(self):
        pass
    def self_ID(self):
        pass
class knight(piece):
    def check_check(self):
        pass
    def check_moves(self):
        pass
    def move(self):
        pass
    def take(self):
        pass
    def upgrade(self):
        pass
    def self_ID(self):
        pass
class king(piece):
    def check_check(self):
        pass
    def check_moves(self):
        pass
    def move(self):
        pass
    def take(self):
        pass
    def upgrade(self):
        pass
    def self_ID(self):
        pass
class queen(piece):
    def check_check(self):
        pass
    def check_moves(self):
        pass
    def move(self):
        pass
    def take(self):
        pass
    def upgrade(self):
        pass
    def self_ID(self):
        pass
class bishop(piece):
    def check_check(self):
        pass
    def check_moves(self):
        pass
    def move(self):
        pass
    def take(self):
        pass
    def upgrade(self):
        pass
    def self_ID(self):
        pass
class space:
    def __init__(self,location:str,piece:piece):
        self.location = location
        self.piece = piece
board:space = [ [0 for i in range(8)] for j in range(8) ] 

def board_init():
    letters = ['a','b','c','d','e','f','g','h']
    for x in range (0,8):
        for y in range (0,8):
            board[x][y]= space((letters[y]) +str(8-x),None)
            print (str(x) + " " + str(y+1))
            print(board[x][y].location)

def piece_init():
    rank_8= [rook("a8",True,[],"black"),knight("b8",True,[],"black"),bishop("c8",True,[],"black"),queen("d8",True,[],"black"),king("e8",True,[],"black"),bishop("f8",True,[],"black"),knight("g8",True,[],"black"),rook("h8",True,[],"black")]
    rank_7= [pawn("a7",True,[],"black"),pawn("b7",True,[],"black"),pawn("c7",True,[],"black"),pawn("d7",True,[],"black"),pawn("e7",True,[],"black"),pawn("f7",True,[],"black"),pawn("g7",True,[],"black"),pawn("h7",True,[],"black")]
    rank_2= [pawn("a2",True,[],"white"),pawn("b2",True,[],"white"),pawn("c2",True,[],"white"),pawn("d2",True,[],"white"),pawn("e2",True,[],"white"),pawn("f2",True,[],"white"),pawn("g2",True,[],"white"),pawn("h2",True,[],"white")]
    rank_1= [rook("a1",True,[],"white"),knight("b1",True,[],"white"),bishop("c1",True,[],"white"),queen("d1",True,[],"white"),king("e1",True,[],"white"),bishop("f1",True,[],"white"),knight("g1",True,[],"white"),rook("h1",True,[],"white")]
    for x in range(0,8):
        board[7][x].piece = rank_1[x]
        print(board[7][x].piece)
    for x in range(0,8):
        board[6][x].piece = rank_2[x]
        print(board[6][x].piece)
    for x in range(0,8):
        board[1][x].piece = rank_7[x]
        print(board[1][x].piece)
    for x in range(0,8):
        board[0][x].piece = rank_8[x]
        print(board[0][x].piece)
    for x in range(0,8):
        for y in range (0,8):
            print(board[x][y].location)
            print(board[x][y].piece)

def space_check(spot:space)-> str:
    if spot.piece != None:
        if isinstance(spot.piece,pawn): return str("P"+spot.piece.color[0:1])
        if isinstance(spot.piece,knight): return str("N"+spot.piece.color[0:1])
        if isinstance(spot.piece,bishop): return str("B"+spot.piece.color[0:1])
        if isinstance(spot.piece,rook): return str("R"+spot.piece.color[0:1])
        if isinstance(spot.piece,queen): return str("Q"+spot.piece.color[0:1])
        if isinstance(spot.piece,king): return str("K"+spot.piece.color[0:1])
    else: return spot.location
    
def board_print() :
    print("______________________")
    for x in range (0,8):
        rowlist = []
        for y in range(0,8):
            rowlist.append(space_check(board[x][y]))
            rowlist.append("")
        rowlist.pop()
        print(rowlist)
    print("______________")
    
    
    
def location_finder(location:str)->space:
    letters = ['h','g','f','e','d','c','b','a']
    letter = ""
    num=""
    for x in range (0,8):
        if location[0] == letters[x]:
            letter = x
    num = location[1]
    print(letters[letter]+num)
    return board[int(num)][int(letter)]



def input_processing(input:str):
    piece_choice=""
    move_choice=""
    valid_locations = ["a1","a2","a3","a4","a5","a6","a7","a8","b1","b2","b3","b4","b5","b6","b7","b8","c1","c2","c3","c4","c5","c6","c7","c8", "d1","d2","d3","d4","d5","d6","d7","d8","e1","e2","e3","e4","e5","e6","e7","e8","f1","f2","f3","f4","f5","f6","f7","f8","g1","g2","g3","g4","g5","g6","g7","g8","h1","h2","h3","h4","h5","h6","h7","h8"]
    if "move" in input:
        for x in valid_locations:
            if x in input:
                piece_choice = x
                first_index = input.index(x)
                for y in valid_locations:
                    if y in input[first_index+1:]:
                        move_choice = y
                        break
                break
        
        
def game_controller():
    input_processing(input("what do you want to do?"))

def check_check():
    pass


def initalize():
    board_init()
    piece_init()
    board_print()

def main():
    initalize()
    
    
main()