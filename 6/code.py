with open('./6/input.txt', 'r') as f:
    input = [a.strip().split() for a in f]
    transposed_input = list(zip(*input))

total = 0
for f in transposed_input:
    op, result = f[-1], 1
    if op =="+":
        result = sum(map(int, f[:-1]))
    elif op == "*":
        for num in map(int, f[:-1]):
            result *= num
    total += result
    
print(f'Part A: answer = { total }') #test assert = 4277556
print(f'Part B: answer = { 0+0 }') #test assert = 3263827