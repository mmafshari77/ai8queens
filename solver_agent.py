from realworld_objects import Checkerboard


from problems import QueenProblem


from copy import deepcopy



class AI8QAgent:


    class State:


        def __init__(self, chk: Checkerboard):
            self.chk = chk

        def move_to_new_state(self, a, b, direction):
            s = deepcopy(self)
            if a >= s.chk.chk_dimensions or b >= s.chk.chk_dimensions or a < 0 or b < 0:
                return None

            elif s.chk.chk[a][b] == None:
                return None

            elif direction == "up":
                if a-1 >= 0:
                    if s.chk.chk[a-1][b] != None:
                        return None
                    else:
                        s.chk.chk[a-1][b] = s.chk.chk[a][b]
                else:
                    return None

            elif direction == "down":
                if a+1 >= 0 and a+1 < s.chk.chk_dimensions:
                    if s.chk.chk[a+1][b] != None:
                        return None
                    else:
                        s.chk.chk[a+1][b] = s.chk.chk[a][b]
                    
                else:
                    return None

            elif direction == "right":
                if b+1 >= 0 and b+1 < s.chk.chk_dimensions:
                    if s.chk.chk[a][b+1] != None:
                        return None
                    else:
                        s.chk.chk[a][b+1] = s.chk.chk[a][b]
                else:
                    return None

            elif direction == "left":
                if b-1 >= 0:
                    if s.chk.chk[a][b-1] != None:
                        return None
                    else:
                        s.chk.chk[a][b-1] = s.chk.chk[a][b]
                else:
                    return None
            s.chk.chk[a][b] = None
            return s



        def expand(self):
            final_states = []
            for i in range(self.chk.chk_dimensions):
                for j in range(self.chk.chk_dimensions):
                    if self.chk.chk[i][j] != None:
                        if self.move_to_new_state(i, j, "up") != None:
                            final_states.append(self.move_to_new_state(i, j, "up"))
                        if self.move_to_new_state(i, j, "down") != None:
                            final_states.append(self.move_to_new_state(i, j, "down"))
                        if self.move_to_new_state(i, j, "right") != None:
                            final_states.append(self.move_to_new_state(i, j, "right"))
                        if self.move_to_new_state(i, j, "left") != None:
                            final_states.append(self.move_to_new_state(i, j, "left"))
            return final_states

    def __init__(self, problem: QueenProblem):


        self.problem = problem


        self.start_state = self.State(problem.chk)


        self.final_state = None


        print("Hi I'm the agent :)")



    # Huristic functions



    # how many rows and columns have more than two pieces?


    def h1(s: State): 


        count = 0


        for i in range(s.chk.chk_dimensions):

            common_in_row = 0


            for j in range(s.chk.chk_dimensions):


                if s.chk.chk[i][j] != None:

                    common_in_row += 1

            if common_in_row > 1:


                count += 1


        for j in range(s.chk.chk_dimensions):

            common_in_column = 0


            for i in range(s.chk.chk_dimensions):


                if s.chk.chk[i][j] != None:

                    common_in_column += 1

            if common_in_column > 1:


                count += 1
        return count



    def h2():


        pass



    def h3():


        pass




    def solve_with_heuristic(self, huristic_func = h1):


        print("Now I try to solve the problem you gave me! Please wait...")


        fringe = []


        observed_states = []


        fringe.append(self.start_state)



        while True:


            # print(fringe)


            minimum_element = fringe[0]
            

            for i in fringe:


                if huristic_func(i) < huristic_func(minimum_element):
                    minimum_element = i


            minimum_element.chk.print_board()
            print(huristic_func(minimum_element))
            if huristic_func(minimum_element) == 0:


                print("Yeah, I've solved it")
                self.final_state = minimum_element


                return 0

            


            observed_states.append(fringe.pop(fringe.index(minimum_element)))


            for i in minimum_element.expand():


                if i not in observed_states:


                    fringe.append(i)