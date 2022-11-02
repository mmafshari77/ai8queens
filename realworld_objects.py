class Piece:
    def __init__(self, p_type, p_color="black"):
        self.p_type = p_type
        self.p_color = p_color
        if (p_type=="Queen"):
            self.p_char = 'Q'

class Checkerboard:
    def __init__(self, chk_dimensions: int = 8):
        self.chk_dimensions = chk_dimensions
        self.chk = []
        for i in range(self.chk_dimensions):
            row = []
            for j in range(self.chk_dimensions):
                row.append(None)
            self.chk.append(row)

    # def __str__(self) -> str:
    #     chk_copy = self.chk
    #     for i in range(self.chk_dimensions):
    #         for j in range(self.chk_dimensions):
    #             chk_copy[i][j] = chk_copy[i][j].p_char)
    #     final_str = "\n".join(chk_copy)
    #     return final_str

    def print_board(self) -> None:
        table = []
        for i in range(self.chk_dimensions):
            row = []
            for j in range(self.chk_dimensions):
                if self.chk[i][j] == None:
                    row.append('-')
                else:
                    row.append(self.chk[i][j].p_char)
            table.append(" ".join(row))
        print("\n".join(table))

    def print_board_colorful(self) -> None:
        pass
