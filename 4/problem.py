import time
import logging
from my_utils import *

def check_letter(grid, coord, letter):
    return grid[coord[0]][coord[1]] == letter

# solution functions
def part_a(input):
    grid = expand_grid_rows(input)    
    # print(grid)
    
    # test input
#     input = '''
# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX'''
    # grid = parse_multi_line_input(input)
    xmas_count = 0
    row_count = len(grid)
    for row in range(len(grid)):
        col_count = len(grid[row])
        for col in range(len(grid[row])):
            if grid[row][col] == 'X':
                coord = (row, col)
                print(coord)
                # check all directions
                # X -> right
                if check_letter(grid, right_x(coord, col_count, 1), 'M') and check_letter(grid, right_x(coord, col_count, 2), 'A') and check_letter(grid, right_x(coord, col_count, 3), 'S'):
                    print('right xmas')
                    xmas_count = xmas_count + 1
                # left <- X
                if check_letter(grid, left_x(coord, 1), 'M') and check_letter(grid, left_x(coord, 2), 'A') and check_letter(grid, left_x(coord, 3), 'S'):
                    print('left xmas')
                    xmas_count = xmas_count + 1
                # X ^ up
                if check_letter(grid, up_x(coord, 1), 'M') and check_letter(grid, up_x(coord, 2), 'A') and check_letter(grid, up_x(coord, 3), 'S'):
                    print('up xmas')
                    xmas_count = xmas_count + 1
                # X down
                if check_letter(grid, down_x(coord, row_count, 1), 'M') and check_letter(grid, down_x(coord, row_count, 2), 'A') and check_letter(grid, down_x(coord, row_count, 3), 'S'):
                    print('down xmas')
                    xmas_count = xmas_count + 1
                # 4 diagonal checks
                # upleft
                if row >= 3 and col >= 3:                
                    if check_letter(grid, upleft_x(coord, 1), 'M') and check_letter(grid, upleft_x(coord, 2), 'A') and check_letter(grid, upleft_x(coord, 3), 'S'):
                        print('up left xmas')
                        xmas_count = xmas_count + 1
                # upright
                if row >= 3 and col < col_count - 3:
                    if check_letter(grid, upright_x(coord, col_count, 1), 'M') and check_letter(grid, upright_x(coord, col_count, 2), 'A') and check_letter(grid, upright_x(coord, col_count, 3), 'S'):
                        print('up right xmas')
                        xmas_count = xmas_count + 1
                # downleft
                if row < row_count - 3 and col >= 3:
                    if check_letter(grid, downleft_x(coord, row_count, 1), 'M') and check_letter(grid, downleft_x(coord, row_count, 2), 'A') and check_letter(grid, downleft_x(coord, row_count, 3), 'S'):
                        print('down left xmas')
                        xmas_count = xmas_count + 1
                # downright
                if row < row_count - 3 and col < col_count - 3:
                    if check_letter(grid, downright_x(coord, row_count, col_count, 1), 'M') and check_letter(grid, downright_x(coord, row_count, col_count, 2), 'A') and check_letter(grid, downright_x(coord, row_count, col_count, 3), 'S'):
                        print('down right xmas')
                        xmas_count = xmas_count + 1
    return xmas_count

def part_b(input):
    # TODO
    return

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
