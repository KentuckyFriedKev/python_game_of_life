class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(0)
            self.grid.append(row)

    def set_status(self, x, y):
        if self.grid[x][y] == 1:
            self.grid[x][y] = 0
        else:
            self.grid[x][y] = 1

    def update(self):
        neighbours = [0, 1, -1]
        for i in range(self.rows):
            for j in range(self.cols):
                live_neighbours = 0
                for k in range(3):
                    for l in range(3):
                        if not(neighbours[k] == 0 and neighbours[l] == 0):
                            r = i + neighbours[k]
                            c = j + neighbours[l]
                            if 0 <= r < self.rows and 0 <= c < self.cols and abs(self.grid[i][j] == 1):
                                live_neighbours += 1
                if (live_neighbours < 2 or live_neighbours > 3) and self.grid[i][j] == 1:
                    self.grid[i][j] = -1
                if live_neighbours == 3 and self.grid[i][j]:
                    self.grid[i][j] = 2
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] > 0:
                    self.grid[i][j] = 1
                else:
                    self.grid[i][j] = 0
