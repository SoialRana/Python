a, b = map(int, input().split()) 
arr = list(map(int, input().split()))  

count_dict = {}

for num in arr:
    count_dict[num] = count_dict.get(num, 0) + 1

for i in range(1, b+1):
    print(count_dict.get(i, 0))
