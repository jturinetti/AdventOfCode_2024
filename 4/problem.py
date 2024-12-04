import time
import logging
from my_utils import *

def check_letter(grid, coord, letter):
    return grid[coord[0]][coord[1]] == letter

def check_xmas(grid, coord):
    row = coord[0]
    col = coord[1]

    if grid[row][col] != 'X':
        return 0
    
    row_count = len(grid)
    col_count = len(grid[0])
    
    xmas_count = 0
    # check all directions
    # X -> right
    if check_letter(grid, right_x(coord, col_count, 1), 'M') and check_letter(grid, right_x(coord, col_count, 2), 'A') and check_letter(grid, right_x(coord, col_count, 3), 'S'):
        xmas_count = xmas_count + 1
    # left <- X
    if check_letter(grid, left_x(coord, 1), 'M') and check_letter(grid, left_x(coord, 2), 'A') and check_letter(grid, left_x(coord, 3), 'S'):
        xmas_count = xmas_count + 1
    # X ^ up
    if check_letter(grid, up_x(coord, 1), 'M') and check_letter(grid, up_x(coord, 2), 'A') and check_letter(grid, up_x(coord, 3), 'S'):
        xmas_count = xmas_count + 1
    # X down
    if check_letter(grid, down_x(coord, row_count, 1), 'M') and check_letter(grid, down_x(coord, row_count, 2), 'A') and check_letter(grid, down_x(coord, row_count, 3), 'S'):
        xmas_count = xmas_count + 1
    # 4 diagonal checks
    # upleft
    if row >= 3 and col >= 3:                
        if check_letter(grid, upleft_x(coord, 1), 'M') and check_letter(grid, upleft_x(coord, 2), 'A') and check_letter(grid, upleft_x(coord, 3), 'S'):
            xmas_count = xmas_count + 1
    # upright
    if row >= 3 and col < col_count - 3:
        if check_letter(grid, upright_x(coord, col_count, 1), 'M') and check_letter(grid, upright_x(coord, col_count, 2), 'A') and check_letter(grid, upright_x(coord, col_count, 3), 'S'):
            xmas_count = xmas_count + 1
    # downleft
    if row < row_count - 3 and col >= 3:
        if check_letter(grid, downleft_x(coord, row_count, 1), 'M') and check_letter(grid, downleft_x(coord, row_count, 2), 'A') and check_letter(grid, downleft_x(coord, row_count, 3), 'S'):
            xmas_count = xmas_count + 1
    # downright
    if row < row_count - 3 and col < col_count - 3:
        if check_letter(grid, downright_x(coord, row_count, col_count, 1), 'M') and check_letter(grid, downright_x(coord, row_count, col_count, 2), 'A') and check_letter(grid, downright_x(coord, row_count, col_count, 3), 'S'):
            xmas_count = xmas_count + 1

    return xmas_count

def check_mas(grid, coord):
    row = coord[0]
    col = coord[1]

    if grid[row][col] != 'A':
        return 0
    
    row_count = len(grid)
    col_count = len(grid[0])

    mas_count = 0
    if row >= 1 and row < row_count - 1 and col >= 1 and col < col_count - 1:
        # stupid, yet effective
        if check_letter(grid, upleft_x(coord, 1), 'S') and check_letter(grid, downleft_x(coord, row_count, 1), 'S'):
            # check right side for M
            if check_letter(grid, upright_x(coord, col_count, 1), 'M') and check_letter(grid, downright_x(coord, row_count, col_count, 1), 'M'):
                mas_count = mas_count + 1
        
        if check_letter(grid, upleft_x(coord, 1), 'S') and check_letter(grid, upright_x(coord, col_count, 1), 'S'):
            # check bottom for M
            if check_letter(grid, downleft_x(coord, row_count, 1), 'M') and check_letter(grid, downright_x(coord, row_count, col_count, 1), 'M'):
                mas_count = mas_count + 1                
        
        if check_letter(grid, upright_x(coord, col_count, 1), 'S') and check_letter(grid, downright_x(coord, row_count, col_count, 1), 'S'):
            # check left side for M
            if check_letter(grid, upleft_x(coord, 1), 'M') and check_letter(grid, downleft_x(coord, row_count, 1), 'M'):
                mas_count = mas_count + 1
        
        if check_letter(grid, downleft_x(coord, row_count, 1), 'S') and check_letter(grid, downright_x(coord, row_count, col_count, 1), 'S'):
            # check top for M
            if check_letter(grid, upleft_x(coord, 1), 'M') and check_letter(grid, upright_x(coord, col_count, 1), 'M'):
                mas_count = mas_count + 1
    
    return mas_count

# solution functions
def part_a(input):
    grid = expand_grid_rows(input)    
    
    xmas_count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            coord = (row, col)
            xmas_count = xmas_count + check_xmas(grid, coord)
            
    return xmas_count

def part_b(input):
    grid = expand_grid_rows(input)

    counter = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            coord = (row, col)
            counter = counter + check_mas(grid, coord)
            
    return counter

def execute():
    input_data = read_aoc_data(4, 2024)    # replace with correct day and year
    start_time = time.perf_counter()
    logging.info('part_a answer: {}'.format(part_a(input_data)))
    end_time = time.perf_counter()
    logging.info(f"part_a perf: {(end_time - start_time):02f}s")
    start_time = time.perf_counter()
    logging.info('part_b answer: {}'.format(part_b(input_data)))
    end_time = time.perf_counter()
    logging.info(f"part_b perf: {(end_time - start_time):02f}s")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, 
                        format='[%(asctime)s][%(levelname)-5s] : %(message)s', 
                        handlers=[logging.StreamHandler()])
    execute()
