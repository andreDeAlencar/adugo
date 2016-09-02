

class Adugo:
    def __init__(self):
        self.board = []
        self.jaguar = []
        self.dogs = []
        self.dead_dogs = 0
        self.is_cornered = False

    def start(self):
        self.init_board()
        self.spawn_jaguar()
        self.spawn_dogs()

    def spawn_jaguar(self):
        self.board[18][2] = "O"
        self.jaguar.append([self.board[18][0], self.board[18][1]])

    def spawn_dogs(self):
        for i in range(16, 18):
            self.board[i][2] = "C"
            self.board[i][3] = i - 15
            self.dogs.append([i - 15, self.board[i][0], self.board[i][1]])
        for i in range(19, 31):
            self.board[i][2] = "C"
            self.board[i][3] = i - 16
            self.dogs.append([i - 16, self.board[i][0], self.board[i][1]])

    def dog_move(self, number, target):
        dog = []
        spot = []
        for d in self.dogs:
            if d[0] == number:
                dog = d
        for b in self.board:
            if b[0] == target:
                spot = b

    def init_board(self):
        self.board.append([1, (2, 4), "V", 0])
        self.board.append([2, (1, 3, 5), "V", 0])
        self.board.append([3, (2, 6), "V", 0])
        self.board.append([4, (1, 5, 7), "V", 0])
        self.board.append([5, (2, 4, 6, 7), "V", 0])
        self.board.append([6, (3, 5, 7), "V", 0])
        self.board.append([7, (4, 5, 6, 9, 10, 13, 14, 15), "V", 0])
        self.board.append([8, (9, 12, 13), "V", 0])
        self.board.append([9, (7, 8, 13), "V", 0])
        self.board.append([10, (7, 11, 15), "V", 0])
        self.board.append([11, (10, 15, 16), "V", 0])
        self.board.append([12, (8, 13, 17), "V", 0])
        self.board.append([13, (7, 8, 9, 12, 14, 17, 18, 19), "V", 0])
        self.board.append([14, (7, 13, 15, 19), "V", 0])
        self.board.append([15, (7, 10, 11, 14, 16, 19, 20, 21), "V", 0])
        self.board.append([16, (11, 15, 21), "V", 0])
        self.board.append([17, (13, 18, 21, 22, 23), "V", 0])
        self.board.append([18, (13, 17, 19, 23), "V", 0])
        self.board.append([19, (13, 14, 15, 18, 20, 23, 24, 25), "V", 0])
        self.board.append([20, (15, 19, 21, 25), "V", 0])
        self.board.append([21, (15, 16, 20, 25, 26), "V", 0])
        self.board.append([22, (17, 23, 27), "V", 0])
        self.board.append([23, (17, 18, 19, 22, 24, 27, 28, 29), "V", 0])
        self.board.append([24, (19, 23, 25, 29), "V", 0])
        self.board.append([25, (19, 20, 21, 24, 26, 29, 30, 31), "V", 0])
        self.board.append([26, (21, 25, 31), "V", 0])
        self.board.append([27, (22, 23, 28), "V", 0])
        self.board.append([28, (23, 27, 29), "V", 0])
        self.board.append([29, (23, 24, 25, 28, 30), "V", 0])
        self.board.append([30, (25, 29, 31), "V", 0])
        self.board.append([31, (25, 26, 30), "V", 0])

    def get_board(self):
        return self.board

    def set_dead_dogs(self):
        self.dead_dogs = 14 - len(self.dogs)

    def get_dead_dogs(self):
        return self.dead_dogs

    def get_dogs(self):
        return self.dogs

    def get_jaguar(self):
        return self.jaguar


j = Adugo()
j.start()
print(j.get_board())
print(j.get_dogs())
print(j.get_jaguar())
print(j.get_dead_dogs())
