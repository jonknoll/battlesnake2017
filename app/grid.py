import sys


class Grid(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for x in range(width)] for y in range(height)]
    
    def set(self, coord, val):
        self.grid[coord[1]][coord[0]] = val
    
    def get(self, coord):
        if((coord[0] >= self.width) or (coord[0] < 0)):
            return(-1)
        elif((coord[1] >= self.height) or (coord[1] < 0)):
            return(-1)
        return self.grid[coord[1]][coord[0]]
    
    def setList(self, coordsList, val):
        for coord in coordsList:
            self.set(coord, val)
    
    def add(self, coord, val):
        origVal = self.get(coord)
        newVal = origVal + val
        self.set(coord, newVal)
        return(newVal)
    
    def printGrid(self, style=0):
        print("GRID: ({} x {})".format(self.width, self.height))
        for y in range(self.height):
            #print("y={}".format(y))
            for x in range(self.width):
                if(style==0):
                    sys.stdout.write("{} ".format(self.get([x,y])))
                else:
                    if(self.get([x,y]) == 0):
                        sys.stdout.write("  ")
                    else:
                        sys.stdout.write("{} ".format(self.get([x,y])))  
            sys.stdout.flush()
            print("")
    
    def print2(self):
        print(self.grid)
            
if __name__=='__main__':
    testGrid = Grid(5,10)
    testGrid.set([0,2], 22)
    testGrid.set([4,0], 44)
    testGrid.print2()
    testGrid.printGrid()
    
    