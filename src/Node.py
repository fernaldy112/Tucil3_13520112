class Node:

    def __init__ (self, array, level, moves):
        self.puzzle = array
        self.level = level
        self.moves = moves

    def countCost (self):
        g = 0
        for i in range(len(self.puzzle)):
            if (self.puzzle[i]!=16 and self.puzzle[i]!=i+1):
                g += 1
        return int(self.level + g)
