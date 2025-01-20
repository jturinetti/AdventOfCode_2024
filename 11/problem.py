import time
import logging
from my_utils import *

def process_blink(stones, next_stones, index, cache):
    digits = len(str(stones[index]))
    if stones[index] == 0:
        next_stones.append(1)
       
    elif digits % 2 == 0:
        midway = int(digits / 2)
        sval = str(stones[index])
        split_left = sval[0:midway]
        split_right = sval[midway:len(sval)]
        next_stones.append(int(split_left))
        next_stones.append(int(split_right))
    
    else:
        next_stones.append(stones[index] * 2024)
        
# solution functions
def part_a(input):
    stones = [int(n) for n in input[0].split()]   
    sindex = 0
    blinks = 75
    cache = {}
    
    for blink in range(blinks):
        next_stones = []
        print('blink {}'.format(blink))
        while sindex < len(stones):        
            process_blink(stones, next_stones, sindex, cache)            
            sindex = sindex + 1
        stones = next_stones
        sindex = 0

    return len(stones)

def part_b(input):
    # TODO
    pass

def execute():
    input_data = read_aoc_data(11, 2024)    # replace with correct day and year
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