import time
import logging
from utils import *
from my_utils import *
import copy

def turn_right(current_direction):
    if current_direction == '^':
        return '>'        
    elif current_direction == '>':
        return 'v'
    elif current_direction == '<':
        return '^'
    elif current_direction == 'v':
        return '<'
    
def traverse_position(grid, coordinate):
    temp = list(grid[coordinate[0]])
    temp[coordinate[1]] = 'X'
    grid[coordinate[0]] = "".join(temp)

# solution functions
def part_a(orig_input):
    input = copy.deepcopy(orig_input)
    rows = len(input)
    cols = len(input[0])
    current = (0,0)
    for x in range(rows - 1):
        if input[x].find('^') > -1:
            current = (x, input[x].find('^'))
            break
    
    # start traversing!
    current_direction = '^'
    inside_grid = True
    counter = 1
    traverse_position(input, current)
    while (inside_grid):
        next = ()
        if current_direction == '^':
            # go up
            next = up_one(current)            
        elif current_direction == '>':
            # go right
            next = right_one(current, cols)            
        elif current_direction == '<':
            # go left
            next = left_one_unsafe(current)
        elif current_direction == 'v':
            # go down
            next = down_one(current, rows)        
        
        if (next[0] < 0 or next[0] >= rows or next[1] < 0 or next[1] >= cols):
            print('done!')
            inside_grid = False
        elif input[next[0]][next[1]] == '#':
            # turn right
            current_direction = turn_right(current_direction)
            print('turning right; new direction is {}'.format(current_direction))
        else:
            print('moving {} from {} to {}'.format(current_direction, current, next))
            current = next
            if (input[current[0]][current[1]] != 'X'):
                counter = counter + 1
                traverse_position(input, current)

    return counter

def part_b(orig_input):
    input = copy.deepcopy(orig_input)
    rows = len(input)
    rows = len(input)
    cols = len(input[0])
    current = (0,0)
    for x in range(rows - 1):
        if input[x].find('^') > -1:
            current = (x, input[x].find('^'))
            break
    
    # start traversing!
    current_direction = '^'
    inside_grid = True
    counter = 1
    loop_counter = 0
    traverse_position(input, current)
    while (inside_grid):
        next = ()
        if current_direction == '^':
            # go up
            next = up_one(current)            
        elif current_direction == '>':
            # go right
            next = right_one(current, cols)            
        elif current_direction == '<':
            # go left
            next = left_one_unsafe(current)
        elif current_direction == 'v':
            # go down
            next = down_one(current, rows)        
        
        if (next[0] < 0 or next[0] >= rows or next[1] < 0 or next[1] >= cols):
            print('done!')
            inside_grid = False
        elif input[next[0]][next[1]] == '#':
            # turn right
            current_direction = turn_right(current_direction)
            print('turning right; new direction is {}'.format(current_direction))
        else:
            print('moving {} from {} to {}'.format(current_direction, current, next))
            current = next
            if (input[current[0]][current[1]] != 'X'):
                counter = counter + 1
                traverse_position(input, current)
            else:
                loop_counter = loop_counter + 1

    return loop_counter

def execute():
    input_data = read_aoc_data(6, 2024)    # replace with correct day and year
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