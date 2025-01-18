import time
import logging
from utils import *
from my_utils import *

def score_trailhead(input, current_coord, starting_coord, cache):
    current_val = get_grid_value(input, current_coord, int)

    # check up/right/left/down  
    funcs = [up_one, down_one, right_one, left_one]
    args = [None, len(input), len(input[0]), None]
    next_step_coords = []
    for f_index in range(len(funcs)):
        f = funcs[f_index]
        f_args = args[f_index]
        next_coord = ()
        if f_args == None:
            next_coord = f(current_coord)
        else:
            next_coord = f(current_coord, f_args)
        val_being_checked = get_grid_value(input, next_coord)
        if val_being_checked != '.' and int(val_being_checked) == current_val + 1:
            next_step_coords.append(next_coord)
    
    # if none match check_for_val, return 0
    # if one matches check_for_val, return score_trailhead(input, coord of match)
    # if two or more match, return sum of all score_trailhead(input, coord of match)
    sum = 0
    for c in next_step_coords:
        if get_grid_value(input, c, int) == 9 and (cache == None or (starting_coord, c) not in cache):
            if cache != None:
                cache.append((starting_coord, c))
            sum = sum + 1
        else:
           sum = sum + score_trailhead(input, c, starting_coord, cache)
    
    return sum

# solution functions
def part_a(input):
    score = 0
    for row in range(len(input)):
        for i in range(len(input[row])):
            digit = (input[row][i])
            if digit == '0':
                score = score + score_trailhead(input, (row, i), (row, i), [])
    return score

def part_b(input):
    score = 0
    for row in range(len(input)):
        for i in range(len(input[row])):
            digit = (input[row][i])
            if digit == '0':
                score = score + score_trailhead(input, (row, i), (row, i), None)
    return score

def execute():
    input_data = read_aoc_data(10, 2024)    # replace with correct day and year
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