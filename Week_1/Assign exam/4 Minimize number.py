n = int(input())
arr=list(map(int,input().split()))
i=0
while all(num%2==0 for num in arr):
    arr=[num//2 for num in arr]
    i+=1

print(i)