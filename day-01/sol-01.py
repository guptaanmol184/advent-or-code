
entries = []
with open ('input.txt', 'r') as depths:
    entries = [int(line) for line in depths.readlines()]

# Answer 1
print(sum( a < b for a, b in zip(entries, entries[1:])))

# Answer 2
print(sum( a < b for a, b in zip(entries, entries[3:])))