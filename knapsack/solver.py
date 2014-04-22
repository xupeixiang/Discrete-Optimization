#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
import sys
import copy

sys.setrecursionlimit(100000000)
Item = namedtuple("Item", ['index', 'value', 'weight', 'ratio'])
goal = 0
taken = []
best_taken = []

def solve_it(input_data):
    global taken
    global best_taken

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1]), float(int(parts[0]) * 1.0 / int(parts[1]))))

    sorted_items = sorted(items, key = lambda x: x[3], reverse = True)
    goal = 0
    taken = [0] * item_count
    best_taken = [0] * item_count

    def dfs(index, cnt_capacity, cnt_value):
        global goal
        global best_taken

        if index == item_count or cnt_capacity == 0:
            if cnt_value > goal:
                goal = cnt_value
                best_taken = copy.copy(taken)
        else:
            item = sorted_items[index]
            if cnt_value + item[3] * cnt_capacity <= goal:
                return
            if item[2] <= cnt_capacity:
                taken[index] = 1
                dfs(index + 1, cnt_capacity - item[2], cnt_value + item[1])
            taken[index:] = [0] * (item_count - index)
            dfs(index + 1, cnt_capacity, cnt_value)

    dfs(0, capacity, 0)

    original_taken = [0] * item_count
    for i in range(item_count):
        original_taken[sorted_items[i][0]] = best_taken[i]

    # prepare the solution in the specified output format
    output_data = str(goal) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, original_taken))
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

