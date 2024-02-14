name = 'sakib\'s khan' # escape kortechi ekhane ... otherwise  's' ta show korbena
name2= "sakib khan"
# multiline string 
name3 = """
        Sakib khan
        number one
        """
print(name)
# string is a sequence of character 

for char in name2:
    print(char)

print(name2[3]) # i
print(name2[1:6]) #akib
print(name2[-3]) # h ..sesh theke 3 no index print korbe
print(name2[::-1]) # nahk bikas

# mutable  means changeable ... string
#immutable means you can not change it 


# name2[0]='R'

print(name2)
if 'khan' in name2:
    print('exists')

print(name2.upper())

# geeks for geeks e ...python string method e porasona kora