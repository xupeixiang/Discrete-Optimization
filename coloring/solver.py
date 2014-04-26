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
    neighbors = [set() for i in range(node_count)]
    neighbor_colors = [set() for i in range(node_count)]
    colors = [0] * node_count

    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))
        neighbors[int(parts[0])].add(int(parts[1]))
        neighbors[int(parts[1])].add(int(parts[0]))

    def get_color(neighbor_color):
        sorted_colors = sorted(neighbor_color)
        c = 0
        for color in sorted_colors:
            if color == c:
                c += 1
            else:
                break
        return c

    def get_neighbor_colors(vertex):
        neighbor_colors_v = set()
        for neighbor in neighbors[vertex]:
            neighbor_colors_v.add(colors[neighbor])

        return neighbor_colors_v

    neighbors_num = [(i,len(neighbor)) for i,neighbor in enumerate(neighbors)]
    orders = sorted(neighbors_num, key = lambda num:num[1], reverse = True)

    for i, _ in orders:
        color = get_color(neighbor_colors[i])
        colors[i] = color
        for neighbor in neighbors[i]:
            neighbor_colors[neighbor].add(color)

    print 'original: %d' % len(set(colors))
    changed = True
    # check optimal
    while(changed):
        changed = False
        for i in range(node_count):
            neighbor_color = neighbor_colors[i]
            if max(neighbor_color) > len(neighbor_color):
                # may replace the max
                candidate_color_small =  get_color(list(neighbor_color) + [colors[i]])
                v_c_pairs = [(neighbor, colors[neighbor]) for neighbor in neighbors[i]]
                v_big = (max(v_c_pairs, key = lambda p: p[1]))[0]
                v_color_same = -1
                for color in range(colors[v_big]):
                    if color == candidate_color_small: continue
                    replaced = True
                    color_same_new_colors = {}

                    original_color_i = colors[i]
                    original_color_big = colors[v_big]
                    colors[i] = candidate_color_small

                    for neighbor_big in neighbors[v_big]:
                        if colors[neighbor_big] == color and neighbor_big != i:
                            colors[v_big] = color
                            new_neighbor_colors = get_neighbor_colors(neighbor_big)
                            candidate_color_same = get_color(new_neighbor_colors)
                            if candidate_color_same >= colors[v_big]:
                                replaced = False
                                break
                            else:
                                color_same_new_colors[neighbor_big] = candidate_color_same

                    colors[i] = original_color_i
                    colors[v_big] = original_color_big
                    if replaced and color_same_new_colors:
                        changed = True
                        # update neighbors colors
                        need_update_vertex_set = neighbors[i].union(neighbors[v_big])
                        colors[i] = candidate_color_small
                        colors[v_big] = color
                        for v_color_same in color_same_new_colors:
                            colors[v_color_same] = color_same_new_colors[v_color_same]
                            need_update_vertex_set = need_update_vertex_set.union(neighbors[v_color_same])

                        for v in need_update_vertex_set:
                            neighbor_colors[v] = get_neighbor_colors(v)
                        break

    # check
    for v1,v2 in edges:
        if colors[v1] == colors[v2]:
            print 'Error: colors of %s = colors of %s.' %(v1, v2)

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

