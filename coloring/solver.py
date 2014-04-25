#!/usr/bin/python
# -*- coding: utf-8 -*-


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges = []
    neighbors = [[] for i in range(node_count + 1)]
    neighbor_colors = [[-1] for i in range(node_count + 1)]
    colors = [0] * node_count

    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))
        neighbors[int(parts[0])].append(int(parts[1]))
        neighbors[int(parts[1])].append(int(parts[0]))

    def get_color(neighbor_color):
        for i, color in enumerate(neighbor_color):
            if color > i - 1:
                return i - 1
        return neighbor_color[-1] + 1

    for i in range(node_count):
        color = get_color(neighbor_colors[i])
        colors[i] = color
        map(lambda neighbor:neighbor_colors[neighbor].append(color), neighbors[i])


    # prepare the solution in the specified output format
    output_data = str(len(set(colors))) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, colors))

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
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)'

