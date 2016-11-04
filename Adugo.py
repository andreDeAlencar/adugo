

class Adugo:
    
    C_EMPTY = 0
    C_JAGUAR = 1
    C_DOG = 2

    C_WAIT_JAGUAR = "WAITING JAGUAR"
    C_WAIT_DOG = "WAITING DOG"
    C_NOT_INIT = "NOT_INITIALIZED"

    DOGS_INIT_POS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15]
    JAGUAR_INIT_POS = 13

    BOARD_ROUTES = [
                                [1, [2, 6, 7]],
                                [2, [1, 3, 7]],
                                [3, [2, 4, 7, 8, 9]],
                                [4, [3, 5, 9]],
                                [5, [4, 9, 10]],
                                [6, [1, 7, 11]],
                                [7, [1, 2, 3, 6, 8, 11, 12, 13]],
                                [8, [3, 7, 9, 13]],
                                [9, [3, 4, 5, 8, 10, 13, 14, 15]],
                                [10, [5, 9, 15]],
                                [11, [6, 7, 12, 16, 17]],
                                [12, [7, 11, 13, 17]],
                                [13, [7, 8, 9, 12, 14, 17, 18, 19]],
                                [14, [9, 13, 15, 19]],
                                [15, [9, 10, 14, 19, 20]],
                                [16, [11, 17, 21]],
                                [17, [11, 12, 13, 16, 18, 21, 22, 23]],
                                [18, [13, 17, 19, 23]],
                                [19, [13, 14, 15, 18, 20, 23, 24, 25]],
                                [20, [15, 19, 25]],
                                [21, [16, 17, 22]],
                                [22, [17, 21, 23]],
                                [23, [17, 18, 19, 22, 24, 26, 27, 28]],
                                [24, [19, 23, 25]],
                                [25, [19, 20, 24]],
                                [26, [23, 27, 29]],
                                [27, [23, 26, 28, 30]],
                                [28, [23, 27, 31]],
                                [29, [26, 30]],
                                [30, [27, 29, 31]],
                                [31, [28, 30]]
                            ]

    
    def __init__(self):
        self.board = []
        self.status = Adugo.C_NOT_INIT
        
    def getBoard(self):
        return self.board

    def getBoardRoutes(self):
        return Adugo.BOARD_ROUTES

    def setPositionContent(self, position, content):
        for pos in self.board:
            if pos[0] == position:
                pos[1] = content

    def getPositionContent(self, position):
        for pos in self.board:
            if pos[0] == position:
                return pos[1]

    def getJaguarPosition(self):
        for pos in self.board:
            if pos[1] == Adugo.C_JAGUAR:
                return pos[0]

    def getDogsPositions(self):
        lst = []
        for pos in self.board:
            if pos[1] == Adugo.C_DOG:
                lst.append(pos[0])
        return lst

    def getDogsQuantity(self):
        return len(self.getDogsPositions())

    def getStatus(self):
        return self.status

    def newBoard(self):
        self.board = [[x, 0] for x in range(1, 32)]
        for pos in Adugo.DOGS_INIT_POS:
            self.setPositionContent(pos, Adugo.C_DOG)
        self.setPositionContent(Adugo.JAGUAR_INIT_POS, Adugo.C_JAGUAR)
        self.status = Adugo.C_WAIT_JAGUAR

    def getPossibleWalk(self, actualPos):
        for pos in Adugo.BOARD_ROUTES:
            if pos[0] == actualPos:
                return pos[1]

    def canWalk(self, actualPos, newPos):
        return newPos in self.getPossibleWalk(actualPos)

    def dogPlay(self, actualPos, newPos):
        if self.getPositionContent(actualPos) == Adugo.C_DOG and self.getPositionContent(newPos) == Adugo.C_EMPTY and self.canWalk(actualPos, newPos) and self.status == Adugo.C_WAIT_DOG:
            self.setPositionContent(actualPos, Adugo.C_EMPTY)
            self.setPositionContent(newPos, Adugo.C_DOG)
            self.status = Adugo.C_WAIT_JAGUAR                
            return True
        else:
            return False

    def jaguarWalk(self, newPos):
        if self.getPositionContent(newPos) == Adugo.C_EMPTY and self.canWalk(self.getJaguarPosition(), newPos) and self.status == Adugo.C_WAIT_JAGUAR:
            self.setPositionContent(self.getJaguarPosition(), Adugo.C_EMPTY)
            self.setPositionContent(newPos, Adugo.C_JAGUAR)                
            self.status = Adugo.C_WAIT_DOG            
            return True
        else:
            return False