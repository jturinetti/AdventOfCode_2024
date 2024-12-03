import time
import logging
import re
from my_utils import read_aoc_data

def algo(input, regex):
    sum = 0
    do = True
    for s in input:
        results = re.findall(regex, s)
        for match in results:
            if match == "do()":
                do = True
                continue
            if match == "don't()":
                do = False
                continue
            if do:
                sm = match.split(',')
                sum = sum + int(sm[0].split('(')[1]) * int(str(sm[1][:-1]))
    return sum

# solution functions
def part_a(input):
    return algo(input, r"mul\([0-9]+,[0-9]+\)")

def part_b(input):
    return algo(input, r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)")

def execute():
    input_data = read_aoc_data(3, 2024)    # replace with correct day and year
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