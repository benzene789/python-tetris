# A class for all the global variables needed
class Info:
    
    def __init__(self):
        self.columns = 10
        self.rows = 24
        self.width = 500
        self.height = 750
        self.o_block = [["B", "B"],
                        ["B", "B"]]

        self.i_block = [["B", "B", "B", "B"]]

        self.j_block = [["B", ".", "."],
                        ["B", "B", "B"]]

        self.l_block = [[".", ".", "B"],
                        ["B", "B", "B"]]
        
        self.s_block = [[".", "B", "B"],
                        ["B", "B", "."]]
        
        self.z_block = [["B", "B", "."],
                        [".", "B", "B"]]
        
        self.t_block = [[".", "B", "."],
                        ["B", "B", "B"]]

        self.all_shapes = [self.o_block, self.i_block, self.j_block, self.l_block,
                           self.s_block, self.z_block, self.t_block]
                    
        self.colours = ["", "blue", "green", "pink", "orange", "purple", "yellow", "red"]