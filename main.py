from realworld_objects import Checkerboard
from problems import QueenProblem
from solver_agent import AI8QAgent

chk = Checkerboard()
problem = QueenProblem(chk, 8)
problem.populate()

print("This is the problem:")
problem.chk.print_board()

agent = AI8QAgent(problem)
agent.solve_with_heuristic()
agent.final_state.chk.print_board()