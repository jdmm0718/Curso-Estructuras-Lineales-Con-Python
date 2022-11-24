from grid import Grid
from array import Array
import random


class Array():
    def __init__(self,depth, rows, columns,fill_value=None):
        self.data = Grid(rows, columns)
        for row in range(rows):
            for column in range(columns):
                self.data[row][column] = Array(depth, fill_value=fill_value)

    def get_rows(self):
        return self.data.get_height()

    def get_columns(self):
        return self.data.get_width()

    def get_depth(self):
        return len(self.data[0][0])
    
    def __getitem__(self, index):
        return self.data[index]

    def __str__(self):
        result = ""

        for depth in range(self.get_depth()):
            result += f'index depth: [{depth}] \n'
            for row in range(self.get_rows()):
                for column in range(self.get_columns()):
                    result += f'   {self.data[row][column][depth]} '
                result += "\n"
            result += "\n"
        return str(result)

    def random_fill3D(self, min, max):
        for i in range(self.get_rows()):
            for j in range(self.get_columns()):
                for x in range(self.get_depth()):
                    self[i][j][x] = random.randint(min, max)
                    


tensor3D =  Array(depth=2,rows=4,columns=3)
print(tensor3D.get_rows())
print(tensor3D.get_columns())
print(tensor3D.get_depth())
print()
print(tensor3D)

tensor3D.random_fill3D(0,9)
print(tensor3D)