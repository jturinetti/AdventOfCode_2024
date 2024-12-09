import time
import logging
from utils import *
from my_utils import read_aoc_data

# solution functions
def part_a(input):
    # input = ['2333133121414131402']
    block_map = ''
    cur_id = 0
    for char_index in range(len(input[0])):
        cur_digit = int(input[0][char_index])
        if char_index % 2 == 0:
            # file
            block_map = block_map + str(cur_id) * cur_digit
            cur_id = cur_id + 1
        else:
            # free space
            block_map = block_map + '.' * cur_digit
    print(block_map)

    cur_id = cur_id - 1

    checksum_index = 0
    reverse_index = len(input[0]) - 1
    block_map_reverse_index = len(block_map) - 1
    checksum = 0
    cur_id_counter = 0
    while (checksum_index < len(block_map) and checksum_index <= block_map_reverse_index):
        cur_char = block_map[checksum_index]
        if cur_char == '.':
            # take number from end of block map
            print('checksum_index: {}'.format(checksum_index))
            print('cur_id: {}'.format(cur_id))
            r = (checksum_index * cur_id)
            print('r: {}'.format(r))
            checksum = checksum + r
            print('checksum in . part: {}'.format(checksum))
            cur_id_counter = cur_id_counter + 1
            block_map_reverse_index = block_map_reverse_index - len(str(cur_id))
            print('cur_id_counter: {}'.format(cur_id_counter))
            print('input[0][reverse_index]: {}'.format(input[0][reverse_index]))
            if cur_id_counter == int(input[0][reverse_index]):
                print('YOU ARE HERE NOW')
                cur_id = cur_id - 1
                cur_id_counter = 0
                block_map_reverse_index = block_map_reverse_index - int(input[0][reverse_index - 1])
                reverse_index = reverse_index - 2
        else:
            checksum = checksum + (checksum_index * int(cur_char))
            print('checksum in else: {}'.format(checksum))

        checksum_index = checksum_index + 1
    return checksum

def part_b(input):
    # TODO
    return

def execute():
    input_data = read_aoc_data(9, 2024)    # replace with correct day and year
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