str=input()

L1=0 
R1=0
split=[]

for i, char in enumerate(str):
    if char == 'L':
        L1+=1
    else:
        R1+=1

    if L1==R1:
        split.append(i)

a=0
balance=[]
for index in split:
    balance.append(str[a:index+1])

print(len(balance))
for string in balance:
    print(string)