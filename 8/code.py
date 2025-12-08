import itertools, heapq
from collections import Counter
from math import prod

with open('./8/input.txt', 'r') as f:
    input = [tuple(map(int, a.split(','))) for a in f]

def solve(pts, size=1000):
    n = len(pts)
    if n == 0:
        return 0, 0

    def d2(a,b): return (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2

    total_pairs = n*(n-1)//2
    k = min(size, total_pairs)

    # Union-Find with size
    parent = list(range(n))
    size = [1]*n
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a,b):
        ra, rb = find(a), find(b)
        if ra == rb: return False
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        return True

    # first answer: connect the k globally-closest pairs
    smallest = heapq.nsmallest(k, ((d2(pts[i],pts[j]), i, j) for i,j in itertools.combinations(range(n),2)))
    smallest.sort()
    # fresh UF
    parent = list(range(n)); size = [1]*n
    for _, i, j in smallest:
        union(i, j)
    roots = [find(i) for i in range(n)]
    sizes = sorted(Counter(roots).values(), reverse=True)
    first_ans = prod((sizes + [1,1,1])[:3])

    # second answer: track last connected pair
    edges = sorted(((d2(pts[i],pts[j]), i, j) for i,j in itertools.combinations(range(n),2)))
    parent = list(range(n)); size = [1]*n
    comps = n
    last_pair = None
    for _, i, j in edges:
        if union(i, j):
            comps -= 1
            last_pair = (i, j)
            if comps == 1:
                break
    if last_pair is None:
        second_ans = 0
    else:
        a, b = last_pair
        second_ans = pts[a][0] * pts[b][0]

    return first_ans, second_ans

ans = solve(input)
print(f'Part A: answer = { ans[0] }') #test assert = 40
print(f'Part B: answer = { ans[1] }') #test assert = 