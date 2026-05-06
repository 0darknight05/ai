import heapq

class AStar:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.rows = len(grid)
        self.cols = len(grid[0])

    # -------------------------------
    # Heuristic (Manhattan Distance)
    # -------------------------------
    def heuristic(self, node):
        return abs(node[0] - self.goal[0]) + abs(node[1] - self.goal[1])

    # -------------------------------
    # Get valid neighbors
    # -------------------------------
    def neighbors(self, node):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []

        for d in directions:
            neighbor = (node[0] + d[0], node[1] + d[1])

            if (
                0 <= neighbor[0] < self.rows and
                0 <= neighbor[1] < self.cols and
                self.grid[neighbor[0]][neighbor[1]] == 0
            ):
                result.append(neighbor)

        return result

    # -------------------------------
    # A* Search Algorithm
    # -------------------------------
    def a_star_search(self):
        open_list = []
        heapq.heappush(open_list, (0, self.start))

        came_from = {}
        g_score = {self.start: 0}
        f_score = {self.start: self.heuristic(self.start)}

        while open_list:
            current = heapq.heappop(open_list)[1]

            if current == self.goal:
                return self.reconstruct_path(came_from, current)

            for neighbor in self.neighbors(current):
                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor)

                    heapq.heappush(open_list, (f_score[neighbor], neighbor))

        return []

    # -------------------------------
    # Reconstruct Path
    # -------------------------------
    def reconstruct_path(self, came_from, current):
        path = [current]

        while current in came_from:
            current = came_from[current]
            path.append(current)

        return path[::-1]


# -------------------------------
# Grid (0 = free, 1 = blocked)
# -------------------------------
grid = [
    [0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0]
]

# Start and Goal
start = (0, 0)
goal = (5, 5)

# Run A*
a_star = AStar(grid, start, goal)
path = a_star.a_star_search()

print("Path from start to goal:")
print(path)
