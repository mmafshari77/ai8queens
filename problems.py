from random import randint
from realworld_objects import Checkerboard, Piece


class QueenProblem:
    def __init__(self, chk: Checkerboard, queen_pieces_count: int):
        self.chk = chk
        self.queen_pieces_count = queen_pieces_count

    def populate(self):
        for i in range(self.queen_pieces_count):
            a = randint(0, self.chk.chk_dimensions-1)
            b = randint(0, self.chk.chk_dimensions-1)
            if self.chk.chk[a][b] != None:
                i -= 1
                continue
            else:
                self.chk.chk[a][b] = Piece(p_type="Queen")


