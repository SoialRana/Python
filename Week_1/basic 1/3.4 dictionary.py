# dictonary hocche key value pair 
numbers= [12,56,98,78,56,12,6,98]
person1=['kala chan','kalitola',23,'student']
# ekahne amra sure bolte parbo na eta dara ki bujacche .. eta dara onek kisu bujhte pare jemon

# key value pair
# dictionary
# object
# hash table
# overlap with set


# ekhane amra value gulo joray joray rakhbo 
person= {'name':'kala pakhi','address':'kalitola','age':23,'job':'bekar'}
print(person)
print(person['job'])
print(person.keys()) # ekhane name,address,age egula hocche key ..(,)comma er pore jeta thake seta hocche value 
print(person.values()) # value gulo print korbe ekhane 
person['language']='python' # dictionary mutable tie amra change korte parbo
person['name']='sada pakhi' 
del person['age']
print(person)

# sudhu key gulo pabo nicher for loop er help e 
for item in person:
    print(item)

# special dictionary looping 
print(" print key and values ")
for key,value in person.items(): # kee and value joray joray asbe tie key value 2 tai nibo
    print(key, value) # sudhu ki pawa jabe 