with open('./3/input.txt', 'r') as f:
    input = [list(map(int,list(a.strip()))) for a in f]

def maxVolts(batts):
    totalVolts,batt,idx = 0,[],0
    for b in input:
        max1 = max(b[:((batts-1)*-1)])
        idx = b.index(max1)
        batt.append(max1)
        for n in range(1,batts):
            max2 = max(b[idx+1:len(b)-((batts-n-1))])
            max1 = max2
            idx = b.index(max2,idx+1)
            batt.append(max1)
        
        totalVolts += int(''.join(map(str,batt)))
        batt = []
    return totalVolts

print(f'Part A: answer = { maxVolts(2) }') #test assert = 357
print(f'Part B: answer = { maxVolts(12) }') #test assert = 3121910778619