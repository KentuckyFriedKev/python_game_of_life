class Grid:

    """
    Create a grid object with the specified number of rows and columns

    INPUTS
    rows (int) - number of rows in the grid
    cols (int) - number of columns in the grid
    """

    def __init__(self, rows, cols):
        # Set the number of rows and columns in the grid
        self._rows = rows
        self._cols = cols
        # Set to store the coordinates (tuples) of all alive cells
        self._alive = set()
        # Create the 2D array of cells
        self._grid = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(0)
            self._grid.append(row)

    """
    Set the status of the cell at x and y, if the cell is alive (1), make it dead (0) and vice versa
    
    INPUTS
    x (int) - x-coordinate of the cell to update
    y (int) - y-coordinate of the cell to update
    OUTPUTS
    N/A - self_grid is updated in-place
    """

    def set_status(self, x, y):
        if self._grid[x][y] == 1:
            self._grid[x][y] = 0
            self._alive.remove((x, y))
        else:
            self._grid[x][y] = 1
            self._alive.add((x, y))

    """
    Return the status of the cell at x and y
    INPUTS
    x (int) - x-coordinate of the cell
    y (int) - y-coordinate of the cell
    OUTPUT
    self._grid[x][y] (int) the status of the cell (0 for dead), (1 for alive)
    """

    def get_status(self, x, y):
        return self._grid[x][y]

    """
    Update the cells in the grid by one generation, the rules are as follows:
    If a live cell has less than 2 live neighbours, it dies due to lack of resource
    If a live cell has more than 3 live neighbours, it dies due to overpopulation
    If a live cell has 2-3 live neighbours, it lives on to the next generation
    If a dead cell has exactly 3 live neighbours, it becomes live as through reproduction
    INPUTS
    N/A
    OUTPUTS
    N/A - self._grid is updated in-place
    """

    def update(self):
        # neighbours: an array of tuples to assist in getting a cell's neighbours
        neighbours = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        # Create a set that keeps track of all the cells that we updated
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

    """
    Apply the game rules to the cell specified, used in conjunction with update()
    INPUTS
    board (int[][]) - grid that contains the status of each cell
    x (int) - x coordinate of the cell to update
    y (int) - y coordinate of the cell to update
    checked (set<(int,int)>) - set to store the coordinates (as a tuple) of all cells we have updated
    OUTPUTS
    N/A - board is updated in-place
    """

    def _apply_rules(self, board, x, y, checked):
        # neighbours: an array of tuples to assist in getting a cell's neighbours
        neighbours = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        # Count the number of live neighbours
        live_neighbours = 0
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
        # Add the cell to the checked set so we can update it later in the update function
        checked.add((x, y))

    """
    Clear the grid by setting all cells to be dead (0)
    INPUTS
    N/A
    OUTPUTS
    N/A - self._grid is updated inplace
    """

    def clear(self):
        for i in range(self._rows):
            for j in range(self._cols):
                self._grid[i][j] = 0
