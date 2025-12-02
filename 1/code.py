with open('./1/test.txt') as f: input = f.readlines()

position, count_part1, count_part2 = 50, 0, 0

for line in input:
    direction, distance = line[0], int(line[1:])
    delta = distance if direction == 'R' else -distance
        
    for _ in range(distance):
        position = (position + (1 if direction == 'R' else -1)) % 100
        count_part2 += 1 if (position == 0) else 0
    
    count_part1 += 1 if (position == 0) else 0

print(f"Part 1: {count_part1}")
print(f"Part 2: {count_part2}")