from collections import deque
# bare en test om d funka, ez ekstra marks i såfall
# innser at dette ikke e verdt å pursuit

def flood_fill(grid, start_x, start_y, target_color, replacement_color):
    """
    Perform a flood fill operation on a grid starting from a given point.
    
    Args:
    - grid: A 2D grid representing the game board.
    - start_x: The x-coordinate of the starting point.
    - start_y: The y-coordinate of the starting point.
    - target_color: The color or value to be replaced.
    - replacement_color: The new color or value to replace the target_color.
    
    Returns:
    - The updated grid after flood fill.
    """
    def is_valid(x, y):
        # Check if the coordinates are within the bounds of the grid
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    # Check if the starting point is valid and if it has the target color
    if not is_valid(start_x, start_y) or grid[start_x][start_y] != target_color:
        return grid

    # Create a queue for the flood fill
    queue = deque([(start_x, start_y)])

    # Define possible moves (up, down, left, right)
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        x, y = queue.popleft()

        # Replace the color at the current position
        grid[x][y] = replacement_color

        # Check adjacent cells
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy

            if is_valid(new_x, new_y) and grid[new_x][new_y] == target_color:
                queue.append((new_x, new_y))

    return grid
