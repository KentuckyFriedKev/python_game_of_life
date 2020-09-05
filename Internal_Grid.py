class Grid:
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._grid = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(0)
            self._grid.append(row)

    def set_status(self, x, y):
        if self._grid[x][y] == 1:
            self._grid[x][y] = 0
        else:
            self._grid[x][y] = 1

    def get_status(self, x, y):
        return self._grid[x][y]

    def update(self):
        neighbours = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        for i in range(self._rows):
            for j in range(self._cols):
                live_neighbours = 0
                for neighbour in neighbours:
                    r = i + neighbour[0]
                    c = j + neighbour[1]
                    if 0 <= r < self._rows and 0 <= c < self._cols and abs(self._grid[r][c]) == 1:
                        live_neighbours += 1
                if (live_neighbours < 2 or live_neighbours > 3) and self._grid[i][j] == 1:
                    self._grid[i][j] = -1
                if live_neighbours == 3 and self._grid[i][j] == 0:
                    self._grid[i][j] = 2
        for i in range(self._rows):
            for j in range(self._cols):
                if self._grid[i][j] > 0:
                    self._grid[i][j] = 1
                else:
                    self._grid[i][j] = 0
