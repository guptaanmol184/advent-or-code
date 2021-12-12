# Advent of code Year 2021 Day 12 solution
# Author = Anmol Gupta
# Date = December 2021

from collections import Counter

input = list()
with open("input.txt", "r") as input_file:
    input = input_file.readlines()

edge_list: dict[str, list[str]] = {}

for line in input:
    node1, node2 = line.strip().split("-")

    # ensure 'start' or 'end' nodes are in node1
    # NOTE: start -> end is not a valid scenario based on the input
    if node2 == "start":
        node1, node2 = node2, node1
    if node2 == "end":
        node1, node2 = node2, node1

    # edge node1 -> node2
    if node1 != "end":
        edge_list[node1] = edge_list.get(node1, [])
        edge_list[node1].append(node2)
    if node1 != "start":
        # edge node2 -> node1
        edge_list[node2] = edge_list.get(node2, [])
        edge_list[node2].append(node1)

import pprint

pprint.pprint(edge_list)

total = list()
total_path_count = 0


def traverse_all_paths_from_suffix(
    path_suffix: list[str], edge_list: dict[str, list[str]]
):
    path_last_node = path_suffix[-1]

    if path_last_node == "end":
        total.append(path_suffix)
        global total_path_count
        total_path_count += 1
        return

    # PART 1
    # for neighbour in edge_list[path_last_node]:
    #     if neighbour.isupper() or neighbour not in path_suffix:
    #         traverse_all_paths_from_suffix(path_suffix + [neighbour], edge_list)

    # PART 2
    for neighbour in edge_list[path_last_node]:
        if neighbour.isupper():
            traverse_all_paths_from_suffix(path_suffix + [neighbour], edge_list)
        elif neighbour.islower():
            lower_neighbours = filter(lambda x: x.islower(), path_suffix)
            c = Counter(lower_neighbours)

            already_exhausted_small_cave_with_2_vists = False
            for val in c.values():
                if val == 2:
                    already_exhausted_small_cave_with_2_vists = True

            if already_exhausted_small_cave_with_2_vists:
                if c[neighbour] == 0:
                    traverse_all_paths_from_suffix(path_suffix + [neighbour], edge_list)
            else:
                traverse_all_paths_from_suffix(path_suffix + [neighbour], edge_list)


traverse_all_paths_from_suffix(["start"], edge_list)

print(total_path_count)
