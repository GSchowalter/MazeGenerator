class Cell:

    #Store the width and height of the plane so that I can return the neighbors from each cell
    #X and Y are position in the plane
    def __init__(x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        wall = True

    def getWall():
        return self.wall

    def getX():
        return self.x
    
    def getY():
        return self.y
    
    def getPos():
        return [getX(), getY()]

    def getNumberOfNeighbors():
        #Corners
        if (((x == width - 1) and (y == height - 1)) or ((x == 0) and (y == height - 1)) or ((x == width - 1) and (y == 0)) or ((x == 0) and (y == 0))):
            return 3
        #Sides
        elif ((x == 0) or (x == width - 1) or (y = 0) or (y == height - 1)):
            return 5
        else:
            return 8