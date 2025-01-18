import logging
import itertools
from aocd import get_data   # to retrieve puzzle inputs
from shapely.geometry import Point
from shapely.geometry import Polygon

# wrapper to call aocd api to retrieve input for day and year
def read_aoc_data(day, year):
    problem_data = get_data(day=day, year=year)
    return problem_data.splitlines()

# file parsing utilities
def read_input_file(filename):
    input_file = open(filename, 'r')
    return input_file.readlines()

def parse_multi_line_input(input: str):
    return list(filter(str.strip, input.splitlines()))

# grid utilities
def generate_empty_grid(row_count, col_count, char):
    return [[char for x in range(col_count)] for y in range(row_count)]

# ['123','456'] -> [[1,2,3],[4,5,6]]
def expand_grid_rows(grid):
    return [list(row) for row in grid]

# [[1,2,3],[4,5,6]] -> ['123','456']
def flatten_grid_rows(grid):
    return [''.join(row) for row in grid]

def grid_string(grid):
    return '\n' + '\n'.join([''.join([item for item in row]) for row in grid])

def get_grid_value(input, coordinate, typef = None):
    v = input[coordinate[0]][coordinate[1]]
    if typef != None:
        return typef(v)
    return v

def up_x(coordinate, x):
    return (max(coordinate[0] - x, 0), coordinate[1])

def up_one(coordinate):
    return up_x(coordinate, 1)

def down_x(coordinate, row_count, x):
    return (min(coordinate[0] + x, row_count - 1), coordinate[1])

def down_one(coordinate, row_count):
    return down_x(coordinate, row_count, 1)

def left_x(coordinate, x):
    return (coordinate[0], max(coordinate[1] - x, 0))

def left_one(coordinate):
    return left_x(coordinate, 1)

def right_x(coordinate, col_count, x):
    return (coordinate[0], min(coordinate[1] + x, col_count - 1))

def right_one(coordinate, col_count):
    return right_x(coordinate, col_count, 1)

def upleft_x(coordinate, x):
    l = left_x(coordinate, x)
    return up_x(l, x)

def upright_x(coordinate, col_count, x):
    r = right_x(coordinate, col_count, x)
    return up_x(r, x)

def downleft_x(coordinate, row_count, x):
    l = left_x(coordinate, x)
    return down_x(l, row_count, x)

def downright_x(coordinate, row_count, col_count, x):
    r = right_x(coordinate, col_count, x)
    return down_x(r, row_count, x)

# shape utilities
# determines corner coordinates around an arbitrary shape from a list of coordinates
# TODO: use existing function in shapely or pandas?
def draw_bounding_box(path):
    min_x = None
    min_y = None
    max_x = None
    max_y = None
    for point in path:
        if min_x is None or point[0] < min_x:
            min_x = point[0]
        if min_y is None or point[1] < min_y:
            min_y = point[1]
        if max_x is None or point[0] > max_x:
            max_x = point[0]
        if max_y is None or point[1] > max_y:
            max_y = point[1]
    bounding_box_points = [(min_x, min_y), (min_x, max_y), (max_x, max_y), (max_x, min_y)]
    logging.debug(bounding_box_points)
    return bounding_box_points

# determines number of coordinates within an arbitrary enclosed shape defined by list of coordinates by iterating and evaluating each coordinate one at a time
def calculate_inner_area(path):
    polygon = Polygon(path)
    bounding_box = draw_bounding_box(path)
    area = 0

    for r in range(min(bounding_box, key=lambda x: x[0])[0], max(bounding_box, key=lambda x: x[0])[0]):
        for c in range(min(bounding_box, key=lambda x: x[1])[1], max(bounding_box, key=lambda x: x[1])[1]):
            if (r, c) in path:
                continue

            point = Point(r, c)
            if point.within(polygon):
                area += 1
    return area

# shoelace formula: https://en.wikipedia.org/wiki/Shoelace_formula
def shoelace(path):
  area = 0
  for (x0, y0), (x1, y1) in itertools.pairwise(path):
    area += (x0 * y1) - (y0 * x1)
  return area / 2.0

# pick's thereom https://en.wikipedia.org/wiki/Pick's_theorem
# returns i + b from equation
def picks(path, perimeter):
  return shoelace(path) + (perimeter / 2.0) + 1