""" numbers = [5,10,15,20,25]
sum=0
for num in numbers:
    print(num)
    sum=sum+num
    if sum>20:
        print('bigger values',sum)
print(sum) """

text = 'pagla hawar'
for char in text:
    print(char)

for i in range(1,10,2):
    print(i)

friends= ['nobel','rahim','abir']
for friend in friends:
    print(friend)

my_array = ['apple','banana','pineapple','watermelon']
for index,value in enumerate(my_array): # 
    print("Index:",index, "Value:",value)