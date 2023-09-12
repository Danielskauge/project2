from sokoban import find_2D_iterator

def taboo_cells(warehouse):
        '''  
    Identify the taboo cells of a warehouse. A cell inside a warehouse is 
    called 'taboo' if whenever a box get pushed on such a cell then the puzzle 
    becomes unsolvable.  
    When determining the taboo cells, you must ignore all the existing boxes, 
    simply consider the walls and the target cells.  
    Use only the following two rules to determine the taboo cells;
     Rule 1: if a cell is a corner inside the warehouse and not a target, 
             then it is a taboo cell.
     Rule 2: all the cells between two corners inside the w]arehouse along a 
             wall are taboo if none of these cells is a target.
    
    @param warehouse: a Warehouse object

    @return
       A string representing the puzzle with only the wall cells marked with 
       an '#' and the taboo cells marked with an 'X'.  
       The returned string should NOT have marks for the worker, the targets,
       and the boxes.  
    '''
        max_x, max_y = get_warehouse_dims(warehouse)

        warehouse_grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
        
        for (x,y) in warehouse.walls:
                warehouse_grid[y][x] = '#'


        for x in range(max_x+1):
                for y in range(max_y+1):
                        if is_corner(x,y,warehouse_grid) and (x,y) not in warehouse.targets:
                                warehouse_grid[y][x] = 'X'
                        elif is_between_corners_without_targets(x,y, warehouse.targets, warehouse_grid):
                                warehouse_grid[y][x] = 'X'

        return warehouse_grid_to_string(warehouse_grid)

def get_taboo_cells_positions(warehouse):
    taboo_cells_string = taboo_cells(warehouse)
    taboo_cells_lines = taboo_cells_string.split('\n')
    positions_generator = find_2D_iterator(taboo_cells_lines, 'X')
    return tuple(positions_generator)


     
def is_corner(x, y, warehouse_grid):
    if not is_within_grid(x, y, warehouse_grid):
        return False
    if warehouse_grid[y][x] == '#':
        return False

    top = is_within_grid(
        x, y-1, warehouse_grid) and warehouse_grid[y-1][x] == '#'
    bottom = is_within_grid(
        x, y+1, warehouse_grid) and warehouse_grid[y+1][x] == '#'
    left = is_within_grid(
        x-1, y, warehouse_grid) and warehouse_grid[y][x-1] == '#'
    right = is_within_grid(
        x+1, y, warehouse_grid) and warehouse_grid[y][x+1] == '#'

    return (top and left) or (top and right) or (bottom and left) or (bottom and right)


def is_between_corners_without_targets(x, y, targets, warehouse_grid):
    horizontal_taboo = vertical_taboo = False

    # Vertical checks
    if between_vertical_corners(x, y, warehouse_grid):
        y_range = range_between_corners(x, y, 'y', warehouse_grid)
        continuous_wall_left = is_continuous_wall_left(x, y, y_range, warehouse_grid)  
        continuous_wall_right = is_continuous_wall_right(x, y, y_range, warehouse_grid)
        no_targets_vertical = is_no_targets_vertical(x, y_range, targets)
        vertical_taboo = (continuous_wall_left or continuous_wall_right) and no_targets_vertical

    # Horizontal checks
    if between_horizontal_corners(x, y, warehouse_grid):
        x_range = range_between_corners(x, y, 'x', warehouse_grid)
        continuous_wall_top = is_continuous_wall_top(x,y, x_range, warehouse_grid)
        continuous_wall_bottom = is_continuous_wall_bottom(x,y, x_range, warehouse_grid)
        no_targets_horizontal = is_no_targets_horizontal(y, x_range, targets)
        horizontal_taboo = (continuous_wall_top or continuous_wall_bottom) and no_targets_horizontal

    return horizontal_taboo or vertical_taboo


def range_between_corners(x, y, axis, warehouse_grid):
    left_corner = None
    right_corner = None
    top_corner = None
    bottom_corner = None

    if axis == 'x':
        for dx in range(x, -1, -1):
            if not is_within_grid(dx, y, warehouse_grid):
                break
            if is_corner(dx, y, warehouse_grid):
                left_corner = dx
                break

        for dx in range(x, len(warehouse_grid[0])):
            if not is_within_grid(dx, y, warehouse_grid):
                break
            if is_corner(dx, y, warehouse_grid):
                right_corner = dx
                break

    elif axis == 'y':
        for dy in range(y, -1, -1):
            if not is_within_grid(x, dy, warehouse_grid):
                break
            if is_corner(x, dy, warehouse_grid):
                top_corner = dy
                break

        for dy in range(y, len(warehouse_grid)):
            if not is_within_grid(x, dy, warehouse_grid):
                break
            if is_corner(x, dy, warehouse_grid):
                bottom_corner = dy
                break

    if axis == 'x':
        if left_corner is None or right_corner is None:
            return None
        return range(left_corner, right_corner + 1)

    elif axis == 'y':
        if top_corner is None or bottom_corner is None:
            return None
        return range(top_corner, bottom_corner + 1)


def between_horizontal_corners(x, y, warehouse_grid):
    left_corner, right_corner = False, False
    for dx in range(x, -1, -1):
        if is_corner(dx, y, warehouse_grid):
            left_corner = True
            break
        if warehouse_grid[y][dx] == '#':
            break
    for dx in range(x, len(warehouse_grid[0])):
        if is_corner(dx, y, warehouse_grid):
            right_corner = True
            break
        if warehouse_grid[y][dx] == '#':
            break
    return left_corner and right_corner


def between_vertical_corners(x, y, warehouse_grid):
    top_corner, bottom_corner = False, False
    for dy in range(y, -1, -1):
        if is_corner(x, dy, warehouse_grid):
            top_corner = True
            break
        if warehouse_grid[dy][x] == '#':
            break
    for dy in range(y, len(warehouse_grid)):
        if is_corner(x, dy, warehouse_grid):
            bottom_corner = True
            break
        if warehouse_grid[dy][x] == '#':
            break
    return top_corner and bottom_corner


def is_continuous_wall_top(x,y, x_range, warehouse_grid):
    if not is_within_grid(x,y-1,warehouse_grid): 
        return False
    else:
        return all(warehouse_grid[y-1][dx] == '#' for dx in x_range)


def is_continuous_wall_bottom(x,y, x_range, warehouse_grid):
    if not is_within_grid(x,y+1,warehouse_grid): 
        return False
    else:
        return all(warehouse_grid[y+1][dx] == '#' for dx in x_range)


def is_continuous_wall_left(x,y,y_range, warehouse_grid):
    if not is_within_grid(x-1,y,warehouse_grid): 
        return False
    else:
        return all(warehouse_grid[dy][x-1] == '#' for dy in y_range)


def is_continuous_wall_right(x,y,y_range, warehouse_grid):
    if not is_within_grid(x+1,y,warehouse_grid): 
        return False
    else:
        return all(warehouse_grid[dy][x+1] == '#' for dy in y_range)


def is_no_targets_vertical(x,y_range, targets):
    return all((x, dy) not in targets for dy in y_range)


def is_no_targets_horizontal(y, x_range, targets):
    return all((dx, y) not in targets for dx in x_range)


def get_warehouse_dims(warehouse):
    max_x = max(wall[0] for wall in warehouse.walls)
    max_y = max(wall[1] for wall in warehouse.walls)
    return max_x, max_y


def warehouse_grid_to_string(warehouse_grid):
    row_strings = [''.join(row) for row in warehouse_grid]
    warehouse_string = '\n'.join(row_strings)
    return warehouse_string


def is_within_grid(x, y, warehouse_grid):
    return 0 <= x < len(warehouse_grid[0]) and 0 <= y < len(warehouse_grid)
