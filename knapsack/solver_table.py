#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    table = [[0] * (capacity + 1) for i in range(item_count + 1)]
    mark = [[0] * (capacity + 1) for i in range(item_count + 1)]

    for i in range(1, item_count + 1):
        item_i = items[i - 1]
        for j in range(1, capacity + 1):
            old_value = table[i - 1][j]
            new_value = item_i.value + table[i - 1][j - item_i.weight] if j >= item_i.weight else 0
            table[i][j], mark[i][j] = (new_value, 1) if new_value > old_value else (old_value, 0)

    value = table[item_count][capacity]
    taken = [0] * item_count

    # backtrace
    cap, count = capacity, item_count
    while(cap > 0 and count > 0):
        taken[count - 1] = mark[count][cap]
        cap -= items[count - 1].weight if mark[count][cap] == 1 else 0
        count -= 1

    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

