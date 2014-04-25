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
    neighbors = [[] for i in range(node_count)]
    neighbor_colors = [set() for i in range(node_count)]
    colors = [0] * node_count

    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))
        neighbors[int(parts[0])].append(int(parts[1]))
        neighbors[int(parts[1])].append(int(parts[0]))

    def get_color(neighbor_color):
        sorted_colors = sorted(neighbor_color)
        c = 0
        for color in sorted_colors:
            if color == c:
                c += 1
            else:
                break
        return c

    neighbors_num = [(i,len(neighbor)) for i,neighbor in enumerate(neighbors)]
    orders = sorted(neighbors_num, key = lambda num:num[1], reverse = True)

    for i, _ in orders:
        color = get_color(neighbor_colors[i])
        colors[i] = color
        for neighbor in neighbors[i]:
            neighbor_colors[neighbor].add(color)
        #print i, color, neighbors[i], neighbor_colors[i]

    # check
    #for v1,v2 in edges:
    #    if colors[v1] == colors[v2]:
    #        print 'Error: colors of %s = colors of %s.' %(v1, v2)

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

