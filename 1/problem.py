import time
import logging
from my_utils import read_aoc_data

def prepare_lists(input):
    list1 = []
    list2 = []
    for n in range(len(input)):
        splitnums = input[n].split('  ')
        list1.append(int(splitnums[0]))
        list2.append(int(splitnums[1]))    
    list1.sort()
    list2.sort()
    return list1, list2

# solution functions
def part_a(input):
    list1, list2 = prepare_lists(input)
    sum = 0
    for n in range(len(input)):
        sum = sum + abs(list1[n] - list2[n])

    return sum

def part_b(input):
    list1, list2 = prepare_lists(input)

    sum = 0
    for n in range(len(input)):
        count = 0
        # brute force =/
        for k in range(len(input)):
            if list1[n] == list2[k]:
                count = count + 1
        sum = sum + list1[n] * count

    return sum

def execute():
    input_data = read_aoc_data(1, 2024)
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