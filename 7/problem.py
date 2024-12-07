import time
import logging
from my_utils import *

def mult(x, y):
    return x * y

def add(x, y):
    return x + y

def concatenate(x, y):
    return int(str(x) + str(y))

def eval_nums_recursive(next_num, nums, results, operands):
    if not nums:
        results.append(next_num)
        return
    
    for o in operands:
        eval_nums_recursive(o(next_num, nums[0]), nums[1:], results, operands)
    
    return results

def eval_nums(expected_result, nums, operands):
    evaluated_nums = eval_nums_recursive(nums[0], nums[1:], [], operands)
    # print(evaluated_nums)
    return expected_result in evaluated_nums

# solution functions
def part_a(input):
    sum = 0
    for equation in input:
        num_list = equation.split(': ')
        result_val = int(num_list[0])        
        nums = [int(x) for x in num_list[1].split(' ')]
        # print(nums)
        if eval_nums(result_val, nums, [add, mult]):
            sum = sum + result_val
    return sum

def part_b(input):
    sum = 0
    for equation in input:
        num_list = equation.split(': ')
        result_val = int(num_list[0])        
        nums = [int(x) for x in num_list[1].split(' ')]
        # print(nums)
        if eval_nums(result_val, nums, [add, mult, concatenate]):
            sum = sum + result_val
    return sum

def execute():
    input_data = read_aoc_data(7, 2024)    # replace with correct day and year
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