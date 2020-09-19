# TODO: Add comments
class Grid:
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._grid = []
        self._alive = set()
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(0)
            self._grid.append(row)

    def set_status(self, x, y):
        if self._grid[x][y] == 1:
            self._grid[x][y] = 0
            self._alive.remove((x, y))
        else:
            self._grid[x][y] = 1
            self._alive.add((x, y))

    def get_status(self, x, y):
        return self._grid[x][y]

    def update(self):
        # neighbours: an array of tuples to assist in getting a cell's neighbours
        neighbours = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        # Add in all the cells we've checked into a set
        checked = set()
        # Apply the rules to each alive cell and their neighbours
        for i in self._alive:
            self._apply_rules(self._grid, i[0], i[1], checked)
            for neighbour in neighbours:
                r = i[0] + neighbour[0]
                c = i[1] + neighbour[1]
                if 0 <= r < self._rows and 0 <= c < self._cols:
                    self._apply_rules(self._grid, r, c, checked)
        # Update all the cells we have checked
        for i in checked:
            if self._grid[i[0]][i[1]] == 2:
                self._grid[i[0]][i[1]] = 1
                self._alive.add((i[0], i[1]))
            elif self._grid[i[0]][i[1]] == -1:
                self._grid[i[0]][i[1]] = 0
                self._alive.remove((i[0], i[1]))

    def _apply_rules(self, board, x, y, checked):
        neighbours = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        live_neighbours = 0
        # Count the number of neighbours
        for neighbour in neighbours:
            r = x + neighbour[0]
            c = y + neighbour[1]
            if 0 <= r < self._rows and 0 <= c < self._cols and abs(board[r][c]) == 1:
                live_neighbours += 1
        # A live cell dies if it has less than 2 live neighbours or more than 3 live neighbours
        # We use the -1 flag to represent that the cell was alive but is now dead
        if board[x][y] == 1 and (live_neighbours < 2 or live_neighbours > 3):
            board[x][y] = -1
        # A dead cell lives again if there are exactly 3 live neighbours
        # We use the 2 flag to represent that the cell was dead but is now live
        if board[x][y] == 0 and live_neighbours == 3:
            board[x][y] = 2
        # Add the cell to the checked set so we can update it later
        checked.add((x, y))
        return

    def clear(self):
        for i in range(self._rows):
            for j in range(self._cols):
                self._grid[i][j] = 0
