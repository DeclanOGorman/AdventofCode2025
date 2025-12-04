with open('./4/input.txt', 'r') as f:
    grid = [list(line.strip()) for line in f]

rows, cols, accessible, total_removed = len(grid), len(grid[0]), 0, 0

def is_accessible(g):
    to_remove = []
    r_len, c_len = len(g), len(g[0])
    for r in range(r_len):
        for c in range(c_len):
            if c < len(g[r]) and g[r][c] == '@':
                count = sum(
                    1 for dr in [-1, 0, 1] for dc in [-1, 0, 1]
                    if (dr, dc) != (0, 0)
                    and 0 <= r + dr < r_len and 0 <= c + dc < c_len
                    and c + dc < len(g[r + dr]) and g[r + dr][c + dc] == '@'
                )
                if count < 4:
                    to_remove.append((r, c))
    return to_remove

print(f'Part A: answer = {len(is_accessible(grid))}')

# Part B: Repeatedly remove accessible rolls until none remain
while True:
    to_remove = is_accessible(grid)   

    if not to_remove:
        break
    
    for r, c in to_remove:
        grid[r][c] = '.'
    total_removed += len(to_remove)

print(f'Part B: answer = {total_removed}') #test assert = 