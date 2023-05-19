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
class space:
    def __init__(self,location:str,piece:piece):
        self.location = location
        self.piece = piece
board:space = [ [0 for i in range(8)] for j in range(8) ] 

def board_init():
    letters = ['a','b','c','d','e','f','g','h']
    for x in range (0,8):
        for y in range (0,8):
            board[x][y]= space((letters[x]) +str(y),None)
            print (str(x) + " " + str(y))
            print(board[x][y].location)
board_init()
def piece_init():
    rank_8= [rook("a8",True,[],"black"),knight("b8",True,[],"black"),bishop("c8",True,[],"black"),queen("d8",True,[],"black"),king("e8",True,[],"black"),bishop("f8",True,[],"black"),knight("g8",True,[],"black"),rook("h8",True,[],"black")]
    rank_7= [pawn("a7",True,[],"black"),pawn("b7",True,[],"black"),pawn("c7",True,[],"black"),pawn("d7",True,[],"black"),pawn("e7",True,[],"black"),pawn("f7",True,[],"black"),pawn("g7",True,[],"black"),pawn("h7",True,[],"black")]
    rank_2= [pawn("a2",True,[],"white"),pawn("b2",True,[],"white"),pawn("c2",True,[],"white"),pawn("d2",True,[],"white"),pawn("e2",True,[],"white"),pawn("f2",True,[],"white"),pawn("g2",True,[],"white"),pawn("h2",True,[],"white")]
    rank_1= [rook("a1",True,[],"white"),knight("b1",True,[],"white"),bishop("c1",True,[],"white"),queen("d1",True,[],"white"),king("e1",True,[],"white"),bishop("f1",True,[],"white"),knight("g1",True,[],"white"),rook("h1",True,[],"white")]
    for x in range(0,8):
        board[x][7].piece = rank_8[x]
        print(board[x][7].piece)
    for x in range(0,8):
        board[x][6].piece = rank_7[x]
        print(board[x][6].piece)
    for x in range(0,8):
        board[x][1].piece = rank_2[x]
        print(board[x][1].piece)
    for x in range(0,8):
        board[x][0].piece = rank_1[x]
        print(board[x][0].piece)
    for x in range(0,8):
        for y in range (0,8):
            print(board[x][y].location)
            print(board[x][y].piece)

def board_print():
    print("______________________")
    