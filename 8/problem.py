import time
import logging
from utils import *
from my_utils import read_aoc_data

# solution functions
def part_a(input):
    signal_map = {}
    for row_index in range(len(input)):
        for col_index in range(len(input[row_index])):
            cur_val = input[row_index][col_index]
            if cur_val != '.':
                if cur_val in signal_map:
                    signal_map[cur_val].append((row_index, col_index))
                else:
                    signal_map[cur_val] = [(row_index, col_index)]
    
    print(signal_map)
    return

def part_b(input):
    # TODO
    return

def execute():
    input_data = read_aoc_data(8, 2024)    # replace with correct day and year
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