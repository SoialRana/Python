
# list ,array, collection is same(simple terms)

#index=   0 1 2 3 4 5 6 7 8 9   jekono programming language e evabe index ache 
numbers=[23,3,4,5,6,7,84,23,12,233]
#index  -10 -9 -8 -7 -6 -5 -4 -3 -2 -1( python index) eta hocche reverse index jodi amra reversely print korte chay
print(numbers[-3],numbers[3])

# list er khetre access korar jonno first e start then last index dewa lage [] er moddhe
#list (start: end) # start from start index and stops before the end index
print(numbers[2:6]) # 2 index theke 6 index er age porjonto print korbe 
print(numbers[1:7])

# list(start:end:step) koto step kore skip korbo seta bole dewa lagbe
print(numbers[1:7:1])
print(numbers[1:7:2]) # 1,3,5 index print korbe... 2 ta kore index skip korbe
print(numbers[2:7:-1])# 2 to 7 e jabo abar bolchi reverse order e jabo eta possible na ashole
print("this is before")
print(numbers[7:2:-1]) # 2 index er age porjonoto print korbe 
print(numbers[7:2:-2])

print(numbers[4:]) # 4 index theke last porjonto print korbe 
print(numbers[:7]) # suru ta na dile first theke 7 index porjonto print korbe
print(numbers[:]) # shortcut to copy a list 
# jodi suru theke sesh konotai mention na kori taile list ta full copy hobe 

print(numbers[::-1]) # shortcut to reverse a list



# python list method..... niye porasona kora 