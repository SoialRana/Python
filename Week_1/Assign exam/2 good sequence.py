n = int(input())
a = list(map(int, input().split()))

frq = {}
r = 0

for num in a:
    if num in frq:
        frq[num] += 1
    else:
        frq[num] = 1

for num, freq in frq.items():
    if freq > num:
        r += freq - num

print(r)
