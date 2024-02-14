# list---> []
#tuple...> ()
#set---> {}
# set hocche muitable but unique 
# set: unique items collection, no duplicate

numbers= [12,56,98,78,56,12,6,98]
print(numbers)
numbers_set=set(numbers) # list take set e convert korbe and {} er moddhe value gulo thakbe 
print(numbers_set)

numbers_set.add(55)#set er khetre add or remove korle order or sequence main korbo na 
# jodi amra same value more than 1 bar add kori taile se same value add na kore 1 bario add korbe 
print(numbers_set)
numbers_set.remove(6)
print(numbers_set)
# numbers_set[1]=5  # position wise amra kawke add korte parbo na set e ...kintu emnite add korte parbo
for item in numbers_set:
    print(item)

if 9 in numbers_set:
    print('9 exists')
elif 98 in numbers_set:
    print('98 exists')

A={1,3,5}
B={1,2,3,4,5}
print(A&B)
print(A|B) # A U B
