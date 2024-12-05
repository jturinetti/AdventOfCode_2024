import time
import logging
from utils import *
from my_utils import read_aoc_data

# solution functions
def part_a(input):
    rules = []
    valid_pages = []
    i = 0
    while '|' in input[i]:
        split_val = input[i].split('|')
        rules.append((int(split_val[0]), int(split_val[1])))
        i = i + 1
    i = i + 1
    valid = True
    while i < len(input):
        pages = [int(x) for x in input[i].split(',')]
        valid = True
        for pi in range(len(pages) - 1):
            # for each page, check that it doesn't break any rules or return
            # get all rules for number
            # loop over remaining pages
            # ensure that (x,y) page pairings do not conflict with all rules for page p
            page = pages[pi]
            other_pages = pages[pi+1:]
            
            # 75|47 should either be found, or 47|75 should NOT be found, or it should not exist
            for page_to_check in other_pages:
                rule = (page_to_check, page)
                if rule in rules:
                    print('NOT VALID due to rule {}'.format(rule))
                    valid = False
                    break
        
        if (valid):
            valid_pages.append(pages)
        
        i = i + 1

    sum = 0
    for vp in valid_pages:
        middle = vp[int(len(vp) / 2)]
        sum = sum + middle
    return sum

def part_b(input):
    rules = []
    invalid_pages = []
    i = 0
    while '|' in input[i]:
        split_val = input[i].split('|')
        rules.append((int(split_val[0]), int(split_val[1])))
        i = i + 1
    i = i + 1
    valid = True
    while i < len(input):
        pages = [int(x) for x in input[i].split(',')]
        valid = True
        for pi in range(len(pages) - 1):
            # for each page, check that it doesn't break any rules or return
            # get all rules for number
            # loop over remaining pages
            # ensure that (x,y) page pairings do not conflict with all rules for page p
            page = pages[pi]
            other_pages = pages[pi+1:]
            
            for page_to_check in other_pages:
                rule = (page_to_check, page)
                if rule in rules:
                    print('NOT VALID due to rule {}'.format(rule))
                    valid = False
                    break        
        
        if (not valid):
            invalid_pages.append(pages)
        
        i = i + 1

    sum = 0
    # TODO: reorder invalid pages to work with rules
    for vp in invalid_pages:
        middle = vp[int(len(vp) / 2)]
        sum = sum + middle
    return sum

def execute():
    input_data = read_aoc_data(5, 2024)    # replace with correct day and year
    start_time = time.perf_counter()
    logging.info('part_a answer: {}'.format(part_a(input_data)))
    end_time = time.perf_counter()
    logging.info(f"part_a perf: {(end_time - start_time):02f}s")
    # start_time = time.perf_counter()
    # logging.info('part_b answer: {}'.format(part_b(input_data)))
    # end_time = time.perf_counter()
    # logging.info(f"part_b perf: {(end_time - start_time):02f}s")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, 
                        format='[%(asctime)s][%(levelname)-5s] : %(message)s', 
                        handlers=[logging.StreamHandler()])
    execute()