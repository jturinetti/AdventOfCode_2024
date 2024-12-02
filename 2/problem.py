import time
import logging
from my_utils import read_aoc_data

# solution functions
def part_a(input):
    count = 0
    for r in input:
        levels = [int(x) for x in r.split(' ')]
        diff_check = True
        dec_check = True
        inc_check = True
        i = 1
       
        while i < len(levels):
            diff = abs(levels[i] - levels[i-1])
            diff_check = diff_check and (diff >= 1 and diff <= 3)
            dec_check = dec_check and (levels[i] < levels[i-1])
            inc_check = inc_check and (levels[i] > levels[i-1])
            i = i + 1
        
        if diff_check and (dec_check or inc_check):
            count = count + 1      
        
    return count

def part_b(input):
    count = 0
    for r in input:
        levels = [int(x) for x in r.split(' ')]
        diff_check = True
        dec_check = True
        inc_check = True
        i = 1
       
        while i < len(levels):
            diff = abs(levels[i] - levels[i-1])
            diff_check = diff_check and (diff >= 1 and diff <= 3)
            dec_check = dec_check and (levels[i] < levels[i-1])
            inc_check = inc_check and (levels[i] > levels[i-1])
            i = i + 1
        
        if diff_check and (dec_check or inc_check):
            count = count + 1
        else:
            # try to dampen the problem
            for di in range(len(levels)):
                new_levels = levels[:di] + levels[di + 1:]
                diff_check = True
                dec_check = True
                inc_check = True
                i = 1
            
                while i < len(new_levels):
                    diff = abs(new_levels[i] - new_levels[i-1])
                    diff_check = diff_check and (diff >= 1 and diff <= 3)
                    dec_check = dec_check and (new_levels[i] < new_levels[i-1])
                    inc_check = inc_check and (new_levels[i] > new_levels[i-1])
                    i = i + 1
                
                if diff_check and (dec_check or inc_check):
                    count = count + 1
                    break                
        
    return count
    

def execute():
    input_data = read_aoc_data(2, 2024)    # replace with correct day and year
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