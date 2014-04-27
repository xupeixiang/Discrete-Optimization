#!/usr/bin/python
# -*- coding: utf-8 -*-
import copy

candidate_colors = set()
colors = []
best_colors = []
neighbor_colors = []
baseline = 0

def solve_it(input_data):
    global best_colors
    global baseline
    global neighbor_colors
    global colors

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges = []
    neighbors = [set() for i in range(node_count)]
    neighbor_colors = [set() for i in range(node_count)]
    colors = [0] * node_count
    best_colors = []
    baseline = node_count

    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))
        neighbors[int(parts[0])].add(int(parts[1]))
        neighbors[int(parts[1])].add(int(parts[0]))

    def get_neighbor_colors(vertex, ordered = True):
        neighbor_colors_v = set()
        for neighbor in neighbors[vertex]:
            if not ordered or neighbor < vertex:
                neighbor_colors_v.add(colors[neighbor])
        return neighbor_colors_v

    # use dp
    def dfs(index, color):
        global candidate_colors
        global best_colors
        global baseline
        global neighbor_colors
        global colors

        if index >= node_count: # won't happen internally
            return
        already_color_count = len(candidate_colors)
        neighbor_colors[index] = get_neighbor_colors(index)
        # print index, color, neighbor_colors[index], candidate_colors
        if color in neighbor_colors[index] or (color not in candidate_colors and
                already_color_count >= baseline - 1) or already_color_count >= baseline: # can't be better
            return
        else:
            candidate_colors.add(color)
            colors[index] = color
            cnt_color_count = len(candidate_colors)
            if index == node_count - 1:
                if cnt_color_count < baseline: # better
                    print 'Baseline: %d -> %d' % (baseline, cnt_color_count)
                    best_colors = copy.copy(colors)
                    baseline = cnt_color_count
                return
            for color in (list(candidate_colors) + [len(candidate_colors)]):
                dfs(index + 1, color)
                # restore index + 1 status
                colors[index + 1:] = [-1] * (node_count - index - 1)
                candidate_colors = set([color for color in colors if color > -1])
    dfs(0, 0)
    # check
    for v1,v2 in edges:
        if best_colors[v1] == best_colors[v2]:
            print 'Error: colors of %s = colors of %s.' %(v1, v2)

    # prepare the solution in the specified output format
    output_data = str(len(set(best_colors))) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, best_colors))

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

