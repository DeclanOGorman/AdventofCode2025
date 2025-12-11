from functools import lru_cache

with open('./11/input.txt', 'r') as f:
    lines = [a.strip() for a in f if a.strip()]

g = {line.split(':', 1)[0].strip(): 
     line.split(':', 1)[1].strip().split() for line in lines}

@lru_cache(None)
def paths_with_required(node, saw_dac, saw_fft):
    saw_dac = saw_dac or (node == 'dac')
    saw_fft = saw_fft or (node == 'fft')
    if node == 'out':
        return 1 if (saw_dac and saw_fft) else 0
    return sum(paths_with_required(nxt, saw_dac, saw_fft) for nxt in g.get(node, []))

print(f"Part A: answer = {paths_with_required('you', True, True)}")
print(f"Part B: answer = {paths_with_required('svr', False, False)}")