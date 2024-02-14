numbers=[12,34,45,56]
numbers.append(54) # list er last e add korbe
print(numbers)

numbers.insert(2,41)# insert 2 position at 41
print(numbers)
numbers.insert(0,32)
print(numbers)

numbers.remove(45) # check the value is already exist or not
print(numbers)
if 8 in numbers: # jodi 8 numbers e thake taile remove korbe otherwise remove korbe na 
    numbers.remove(8)
print(numbers) # kono kisu remove korbena 


print("this is next")
last=numbers.pop()
print(last,numbers)


index=numbers.index(32)
print(index)
#index=numbers.index(5)
#print(index)

""" if 5 in numbers:
    index= numbers.index(5)
    print(index) """

sorted=numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)