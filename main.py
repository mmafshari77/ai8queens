from heuristic import Checkerboard, QueenProblem, print_board

chk = Checkerboard()
p = QueenProblem(chk, 8)
p.populate()
print_board(chk)EF