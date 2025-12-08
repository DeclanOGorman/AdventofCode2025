from math import prod

with open('./6/input.txt', 'r') as f:
    raw_lines = f.read().splitlines()

transposed = list(zip(*[ln.strip().split() for ln in raw_lines if ln.strip()]))
total_a, total_b = 0, 0
for col in transposed:
    op = col[-1]
    nums = list(map(int, col[:-1]))
    total_a += sum(nums) if op == "+" else prod(nums)

w = max(map(len, raw_lines))
grid = [ln.ljust(w) for ln in raw_lines]
rows = len(grid)
data_rows = rows - 1  # all but last row are digit rows
sep = [all(grid[r][c] == ' ' for r in range(rows)) for c in range(w)]

segs, c = [], 0
while c < w:
    if sep[c]:
        c += 1; continue
    s = c
    while c < w and not sep[c]:
        c += 1
    segs.append((s, c))

for s, e in segs:
    nums = []
    # read columns right-to-left inside the segment; digits top->bottom
    for col in range(e - 1, s - 1, -1):
        digits = ''.join(grid[r][col] for r in range(data_rows)).replace(' ', '')
        if digits:
            nums.append(int(digits))
    op = grid[-1][s:e].strip()[0]
    total_b += sum(nums) if op == '+' else (prod(nums) if nums else 0)

print(f'Part A: answer = { total_a }')
print(f'Part B: answer = { total_b }')