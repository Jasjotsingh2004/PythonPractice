import heapq
import math
import sys

STUDENT_ID = 'a1234567'
DEGREE = 'UG'

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

def parse_map(file_path):
    """Parse the input map file."""
    with open(file_path, 'r') as file:
        rows, cols = map(int, file.readline().split())
        start_row, start_col = map(int, file.readline().split())
        end_row, end_col = map(int, file.readline().split())
        grid = [line.split() for line in file]
        return rows, cols, (start_row-1, start_col-1), (end_row-1, end_col-1), grid

def is_valid_move(grid, row, col):
    """Check if the position is within bounds and not an obstacle."""
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != 'X'

def get_neighbors(row, col):
    """Generate neighboring positions based on 4-connectivity."""
    for drow, dcol in DIRECTIONS:
        yield row + drow, col + dcol

def euclidean_distance(current, goal):
    """Euclidean heuristic."""
    return math.sqrt((current[0] - goal[0]) ** 2 + (current[1] - goal[1]) ** 2)

def manhattan_distance(current, goal):
    """Manhattan heuristic."""
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def bfs(start, end, grid):
    """Breadth-First Search implementation."""
    from collections import deque
    queue = deque([start])
    parent_map = {start: None}
    visited = {start}

    while queue:
        current = queue.popleft()
        if current == end:
            return reconstruct_path(parent_map, current)
        for neighbor in get_neighbors(*current):
            if is_valid_move(grid, *neighbor) and neighbor not in visited:
                visited.add(neighbor)
                parent_map[neighbor] = current
                queue.append(neighbor)
    return None

def ucs(start, end, grid):
    """Uniform Cost Search implementation."""
    priority_queue = [(0, start)]  # (cost, position)
    parent_map = {start: None}
    cost_map = {start: 0}
    visited = set()

    while priority_queue:
        current_cost, current = heapq.heappop(priority_queue)
        if current == end:
            return reconstruct_path(parent_map, current)
        if current in visited:
            continue
        visited.add(current)

        for neighbor in get_neighbors(*current):
            if is_valid_move(grid, *neighbor):
                elevation_cost = 1 if int(grid[neighbor[0]][neighbor[1]]) <= int(grid[current[0]][current[1]]) else 1 + abs(int(grid[neighbor[0]][neighbor[1]]) - int(grid[current[0]][current[1]]))
                new_cost = current_cost + elevation_cost
                if neighbor not in visited or new_cost < cost_map.get(neighbor, float('inf')):
                    cost_map[neighbor] = new_cost
                    heapq.heappush(priority_queue, (new_cost, neighbor))
                    parent_map[neighbor] = current
    return None

def a_star(start, end, grid, heuristic):
    """A* Search implementation."""
    priority_queue = [(heuristic(start, end), 0, start)]  # (f, cost, position)
    parent_map = {start: None}
    cost_map = {start: 0}
    visited = set()

    while priority_queue:
        _, current_cost, current = heapq.heappop(priority_queue)
        if current == end:
            return reconstruct_path(parent_map, current)
        if current in visited:
            continue
        visited.add(current)

        for neighbor in get_neighbors(*current):
            if is_valid_move(grid, *neighbor):
                elevation_cost = 1 if int(grid[neighbor[0]][neighbor[1]]) <= int(grid[current[0]][current[1]]) else 1 + abs(int(grid[neighbor[0]][neighbor[1]]) - int(grid[current[0]][current[1]]))
                new_cost = current_cost + elevation_cost
                f_score = new_cost + heuristic(neighbor, end)
                if neighbor not in visited or new_cost < cost_map.get(neighbor, float('inf')):
                    cost_map[neighbor] = new_cost
                    heapq.heappush(priority_queue, (f_score, new_cost, neighbor))
                    parent_map[neighbor] = current
    return None

def reconstruct_path(parent_map, current):
    """Reconstruct the path from the parent map."""
    path = []
    while current:
        path.append(current)
        current = parent_map.get(current)
    return path[::-1]

def print_path(path, grid):
    """Print the path in the required format."""
    for i, j in path:
        grid[i][j] = '*'
    for row in grid:
        print(' '.join(row))

def main():
    if len(sys.argv) < 4:
        print("Usage: python script.py <mode> <map_file> <algorithm> [heuristic]")
        return
    mode = sys.argv[1]
    map_path = sys.argv[2]
    algorithm = sys.argv[3]
    heuristic = sys.argv[4] if len(sys.argv) > 4 else None

    rows, cols, start, end, grid = parse_map(map_path)

    if algorithm == 'bfs':
        path = bfs(start, end, grid)
    elif algorithm == 'ucs':
        path = ucs(start, end, grid)
    elif algorithm == 'astar':
        heuristic_func = euclidean_distance if heuristic == 'euclidean' else manhattan_distance
        path = a_star(start, end, grid, heuristic_func)
    else:
        print("Invalid algorithm.")
        return

    if path:
        print_path(path, grid)
    else:
        print('path: null')

if __name__ == '__main__':
    main()
