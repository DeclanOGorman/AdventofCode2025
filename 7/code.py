with open('./7/input.txt', 'r') as f:
    input = [a.strip() for a in f]

def count_splits(G):
    from collections import defaultdict
    if not G: return 0, 0
    w = max(map(len, G)); G = [l.ljust(w) for l in G]
    rs = next(r for r, l in enumerate(G) if 'S' in l)
    cs = G[rs].index('S')

    splits = 0
    counts = {cs: 1}  # column -> number of timelines/beams at this row
    for r in range(rs + 1, len(G)):
        row = G[r]
        # apply splitter/propagation rules in this row until stable
        while True:
            # count splits for each column that currently hits a splitter
            splits += sum(1 for c in counts if 0 <= c < w and row[c] == '^')
            nxt = defaultdict(int)
            for c, k in counts.items():
                if 0 <= c < w and row[c] == '^':
                    if c - 1 >= 0: nxt[c - 1] += k
                    if c + 1 < w:  nxt[c + 1] += k
                else:
                    if 0 <= c < w: nxt[c] += k
            nxt = dict(nxt)
            if nxt == counts:
                break
            counts = nxt
        if not counts:
            break

    return splits, sum(counts.values())

pA, pB = count_splits(input)
print(f'Part A: answer = { pA }') #test assert = 21
print(f'Part B: answer = { pB }') #test assert = 40