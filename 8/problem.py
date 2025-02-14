import time
import logging
from utils import *
from my_utils import read_aoc_data, parse_multi_line_input

def in_bounds(coord, x_max, y_max):
    return coord[0] >= 0 and coord[1] < x_max and coord[1] >= 0 and coord[1] < y_max

# solution functions
def part_a(input):

#     input = '''............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............'''

#     input = parse_multi_line_input(input)

    signal_map = {}
    for row_index in range(len(input)):
        for col_index in range(len(input[row_index])):
            cur_val = input[row_index][col_index]
            if cur_val != '.' and cur_val != '\n':
                if cur_val in signal_map:
                    signal_map[cur_val].append((row_index, col_index))
                else:
                    signal_map[cur_val] = [(row_index, col_index)]
    
    print(signal_map)

    antinodes = []
    for freq in signal_map.keys():
        coords = signal_map[freq]
        for p1_i in range(len(coords)):
            for p2_i in range(len(coords)):
                if p1_i == p2_i:
                    continue
                p1 = coords[p1_i]
                p2 = coords[p2_i]
                diff_x = p1[0] - p2[0]
                diff_y = p1[1] - p2[1]
                c = (p1[0] + diff_x, p1[1] + diff_y)
                if c != p1 and c != p2:
                    antinodes.append(c)
                c = (p2[0] - diff_x, p2[1] - diff_y)
                if c != p1 and c != p2:
                    antinodes.append(c)
                diff_x = p2[0] - p1[0]
                diff_y = p2[1] - p1[1]
                c = (p1[0] - diff_x, p1[1] - diff_y)
                if c != p1 and c != p2:
                    antinodes.append(c)
                c = (p2[0] + diff_x, p2[1] + diff_y)
                if c != p1 and c != p2:
                    antinodes.append(c)
                
    # only count antinodes that are within bounds
    valid_antinodes = [an for an in antinodes if an[0] >= 0 and an[0] < len(input) and an[1] >= 0 and an[1] < len(input[0])]
    # print(valid_antinodes)
    # print(set(valid_antinodes))    
    return len(set(valid_antinodes))

def part_b(input):
    signal_map = {}
    for row_index in range(len(input)):
        for col_index in range(len(input[row_index])):
            cur_val = input[row_index][col_index]
            if cur_val != '.' and cur_val != '\n':
                if cur_val in signal_map:
                    signal_map[cur_val].append((row_index, col_index))
                else:
                    signal_map[cur_val] = [(row_index, col_index)]
    
    print(signal_map)

    antinodes = []
    row_max = len(input)
    col_max = len(input[0])
    for freq in signal_map.keys():
        coords = signal_map[freq]
        for p1_i in range(len(coords)):
            for p2_i in range(len(coords)):
                if p1_i == p2_i:
                    continue
                p1 = coords[p1_i]
                p2 = coords[p2_i]
                diff_x = p1[0] - p2[0]
                diff_y = p1[1] - p2[1]
                next_antinode = p1
                while(in_bounds(next_antinode, row_max, col_max)):
                    antinodes.append(next_antinode)
                    temp = next_antinode
                    next_antinode = (temp[0] - diff_x, temp[1] - diff_y)
                next_antinode = p2
                while(in_bounds(next_antinode, row_max, col_max)):
                    antinodes.append(next_antinode)
                    temp = next_antinode
                    next_antinode = (temp[0] + diff_x, temp[1] + diff_y)

                
    # only count antinodes that are within bounds
    valid_antinodes = [an for an in antinodes if in_bounds(an, len(input), len(input[0]))]
    # print(valid_antinodes)
    # print(set(valid_antinodes))    
    return len(set(valid_antinodes))    

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