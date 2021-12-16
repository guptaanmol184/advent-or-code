# Advent of code Year 2021 Day 16 solution
# Author = Anmol Gupta
# Date = December 2021

import packet as pkt
import functools

input = list()
with open("input.txt", "r") as input_file:
    input = input_file.readlines()

hex_packet = input[0]

# Packet conversion
# Prepend 1 and remove 1 to not miss leading zeros during conversion
bin_packet = bin(int("1" + hex_packet, 16))[3:]  # .rstrip("0")


# Get the literal value of a packet
def get_literal_value(bin_literal_data, start_index):

    bin_data_str = ""
    index = start_index
    while True:
        bin_data_str = bin_data_str + bin_literal_data[index + 1 : index + 5]
        if bin_literal_data[index] == "0":
            break
        else:
            index += 5

    return (int(bin_data_str, 2), index + 5 - 1)


# Packet Parsing
def parse_packet(bin_packet, start_index):
    packet_ver = int(bin_packet[start_index : start_index + 3], 2)
    type_id = int(bin_packet[start_index + 3 : start_index + 6], 2)

    if type_id == 4:
        # literal packet
        literal_value_start_index = start_index + 6
        value, end_index = get_literal_value(bin_packet, literal_value_start_index)
        return (pkt.Literal(packet_ver, type_id, value), end_index)
    else:
        length_type_id_index = start_index + 6
        # operator packet
        length_type_id = bin_packet[length_type_id_index]
        if length_type_id == "0":
            # next 15 bits represent total length of sub-packets
            length_start_index = length_type_id_index + 1
            subpackets_bit_length = int(
                bin_packet[length_start_index : length_start_index + 15],
                2,
            )
            sub_packet_start_index = length_start_index + 15
            next_sub_packet_start_index = sub_packet_start_index
            sub_packets = []
            end_index = 0
            while True:
                packet_tree, end_index = parse_packet(
                    bin_packet, next_sub_packet_start_index
                )
                sub_packets.append(packet_tree)
                next_sub_packet_start_index = end_index + 1
                if end_index - sub_packet_start_index + 1 == subpackets_bit_length:
                    break
            return (pkt.Operator(packet_ver, type_id, sub_packets), end_index)
        elif length_type_id == "1":
            # next 11 bits represent number of sub-packets contained
            subpackets_count_start_index = length_type_id_index + 1
            subpackets_count = int(
                bin_packet[
                    subpackets_count_start_index : subpackets_count_start_index + 11
                ],
                2,
            )
            sub_packet_start_index = subpackets_count_start_index + 11
            next_sub_packet_start_index = sub_packet_start_index
            sub_packets = []
            end_index = 0
            while True:
                packet_tree, end_index = parse_packet(
                    bin_packet, next_sub_packet_start_index
                )
                sub_packets.append(packet_tree)
                next_sub_packet_start_index = end_index + 1
                if len(sub_packets) == subpackets_count:
                    break
            return (pkt.Operator(packet_ver, type_id, sub_packets), end_index)


packet_tree, end_index = parse_packet(bin_packet, 0)

# Get Sum of all packet versions
def get_packet_version_sum(packet_tree: pkt.Packet):

    if packet_tree.type_id == 4:
        # literal
        return packet_tree.packet_version
    else:
        # operator
        return (
            sum([get_packet_version_sum(tree) for tree in packet_tree.data])
            + packet_tree.packet_version
        )


ans1 = get_packet_version_sum(packet_tree)

# 1
"""
Solution to Part 1
"""
print("Part One : " + str(ans1))

# Evaluate the packet expression
def evaluate_packet_tree(packet_tree: pkt.Packet):
    if packet_tree.type_id == 4:
        # literal
        return packet_tree.data
    else:
        children_evaluations = [evaluate_packet_tree(tree) for tree in packet_tree.data]
        if packet_tree.type_id == 0:
            return sum(children_evaluations)
        elif packet_tree.type_id == 1:
            return functools.reduce(lambda x, y: x * y, children_evaluations)
        elif packet_tree.type_id == 2:
            return min(children_evaluations)
        elif packet_tree.type_id == 3:
            return max(children_evaluations)
        elif packet_tree.type_id == 5:
            assert (
                len(children_evaluations) == 2
            ), "Greater than packet with more than 2 childer"
            return 1 if children_evaluations[0] > children_evaluations[1] else 0
        elif packet_tree.type_id == 6:
            assert (
                len(children_evaluations) == 2
            ), "Less than packet with more than 2 childer"
            return 1 if children_evaluations[0] < children_evaluations[1] else 0
        elif packet_tree.type_id == 7:
            assert (
                len(children_evaluations) == 2
            ), "Less than packet with more than 2 childer"
            return 1 if children_evaluations[0] == children_evaluations[1] else 0


ans2 = evaluate_packet_tree(packet_tree)

# 2
"""
Solution to Part 2
"""
print("Part Two : " + str(ans2))
