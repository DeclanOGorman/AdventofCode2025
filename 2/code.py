with open('./2/input.txt', 'r') as f:
    input = f.read().strip()

def is_invalid_id(n):
    s = str(n)
    l = len(s)
    return l % 2 == 0 and s[:l//2] == s[l//2:]

def is_invalid_id_repeated(n):
    s = str(n)
    l = len(s)
    for size in range(1, l // 2 + 1):
        if l % size == 0:
            part = s[:size]
            if part * (l // size) == s:
                return True
    return False

total, total_b = 0, 0
for part in input.split(','):
    if not part: continue
    start, end = map(int, part.split('-'))
    for n in range(start, end + 1):
        if is_invalid_id(n):
            total += n
        if is_invalid_id_repeated(n):
            total_b += n

print(f'Part A: answer = { total }') #test assert = 

print(f'Part B: answer = { total_b }') #test assert =