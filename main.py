from abc import ABC, abstractmethod
board =  [[0] * 8] * 2

        
class piece(ABC):
    def init(self,space:str,side,life,potential_moves,color:str):
        self.space:str = space
        self.side = side
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
        
def board_init():
    letters = ['a','b','c','d','e','f','g','h']
    for x in letters:
        for y in range (0,7):
            board[x][y] = space(letters + y, None)
def piece_init():
    rank_8= [rook("a8",True,[],"black"),knight("b8",True,[],"black"),bishop("c8",True,[],"black"),queen("d8",True,[],"black"),king("e8",True,[],"black"),bishop("f8",True,[],"black"),knight("g8",True,[],"black"),rook("h8",True,[],"black")]
    rank_7= [pawn("a7",True,[],"black"),pawn("a7",True,[],"black"),pawn("b7",True,[],"black"),pawn("c7",True,[],"black"),pawn("d7",True,[],"black"),pawn("e7",True,[],"black"),pawn("f7",True,[],"black"),pawn("g7",True,[],"black")]
    rank_2= [pawn("a2",True,[],"white"),pawn("a7",True,[],"white"),pawn("b2",True,[],"white"),pawn("c2",True,[],"white"),pawn("d2",True,[],"white"),pawn("e2",True,[],"white"),pawn("f2",True,[],"white"),pawn("g2",True,[],"white")]
    rank_1= [rook("a1",True,[],"white"),knight("b1",True,[],"white"),bishop("c1",True,[],"white"),queen("d1",True,[],"white"),king("e1",True,[],"white"),bishop("f1",True,[],"white"),knight("g1",True,[],"white"),rook("h1",True,[],"white")]
    for x in rank_8:
        board[x][7] = rank_8
    for x in rank_7:
        board[x][6] = rank_7
    for x in rank_2:
        board[x][1] = rank_2
    for x in rank_1:
        board[x][0] = rank_1
    for x in range(0,7):
        for y in range (0,7):
            print(board[x][y].piece)