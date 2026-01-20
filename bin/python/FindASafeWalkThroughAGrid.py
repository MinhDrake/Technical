from typing import List
from collections import deque


class Solution:
    """
    def findSafeWalk(Self, grid: List[List[int]], health: int) -> bool:
        # check if the grid is empty or the first row is empty ([[]])
        if not grid or not grid[0]:
            return False

        # get the dimensions of the grid
        m, n = len(grid), len(grid[0])

        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Initialize visited matrix with -1
        visited = [[-1 for _ in range(n)] for _ in range(m)]

        # Initialize health after stepping in grid
        initial_health = health - grid[0][0]
        if initial_health <= 0:
            return False
        visited[0][0] = initial_health

        # Initialize the queue and add the starting point
        queue = deque()
        queue.append((0, 0, initial_health))

        while queue:
            # get the current cell
            x, y, current_health = queue.popleft()

            # If reached the end
            if x == m-1 and y == n-1:
                return True

            # Loop all directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # Check boundaries
                if 0 <= nx < m and 0 <= ny < n:
                    # Calculate new health
                    new_health = current_health - grid[nx][ny]

                    if new_health <= 0:
                        continue
                    # If we have not visited this cell, or have more health than before then go to the cell 
                    # must be aware you can't have more health than you before ( only if -1 )
                    if new_health > visited[nx][ny]:
                        visited[nx][ny] = new_health
                        queue.append((nx, ny, new_health))

        return False
    """

    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        if not grid or not grid[0]:
            return False

        m, n = len(grid), len(grid[0])

        # up, down , left, right
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # visited (store pos - current health, check visited or not)
        visited = [[-1 for _ in range(n)] for _ in range(m)]

        # step the first position
        queue = deque()
        queue.append((0, 0, health-grid[0][0]))
        visited[0][0] = health-grid[0][0]

        while queue:
            x, y, current_health = queue.popleft()

            if x == m-1 and y == n-1:
                return True

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    new_health = current_health - grid[nx][ny]

                    if new_health <= 0:
                        continue

                    if new_health > visited[nx][ny]:
                        visited[nx][ny] = new_health
                        queue.append((nx, ny, visited[nx][ny]))

        return False


# Test
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0]
]
health = 1
solution = Solution()
print(solution.findSafeWalk(grid, health))  # True
