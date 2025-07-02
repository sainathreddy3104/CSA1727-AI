class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.position = (0, 0)

    def clean(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1:  # 1 represents dirt
                    self.position = (i, j)
                    self.grid[i][j] = 0  # Clean the dirt

grid = [[0, 1, 0], [1, 0, 1], [0, 0, 0]]
vacuum = VacuumCleaner(grid)
vacuum.clean()
print(grid)  # Output: [[0, 0, 0], [0, 0, 1], [0, 0, 0]]
