with open('./5/input.txt', 'r') as f:
    input = f.read()
    parts = input.strip().split('\n\n')
    ranges = parts[0].strip().split('\n')

def count_fresh_ingredients(parts, ranges):
    ids = list(map(int, parts[1].strip().split('\n')))
    
    # Parse and sort ranges
    fresh_ranges = sorted([tuple(map(int, r.split('-'))) for r in ranges])
    
    # Merge overlapping ranges
    merged = []
    for start, end in fresh_ranges:
        if merged and start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    
    # Count IDs in merged ranges using binary search
    available_ingredients = sum(1 for id in ids if any(start <= id <= end for start, end in merged))
    total_ingredients = sum(end - start + 1 for start, end in merged)
    return available_ingredients, total_ingredients

pA, pB = count_fresh_ingredients(parts, ranges)
print(f'Part A: answer = { pA }') #test assert = 3
print(f'Part B: answer = { pB }') #test assert = 14