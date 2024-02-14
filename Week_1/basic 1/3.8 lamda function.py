# lambda

# def doubled(x):
#     return 2*x

doubled=lambda num:num*2
squared=lambda num: num*num

result=doubled(44)
output=squared(9)
# print(result,output)
add=lambda x,y: x+y
sum=add(11,22)
print(sum)

numbers= [12,56,98,78,56,12,6,98]

# doubled_nums=map(doubled,numbers)
doubled_nums=map(lambda x: x*2, numbers)
squared_nums=map(lambda x: x*x, numbers)
print(numbers)
# print(list(doubled_nums))
print(list(squared_nums))


actors=[
    {'name': 'sabana', 'age':34},
    {'name': 'jui', 'age':31},
    {'name': 'nipu', 'age':35},
    {'name': 'setu', 'age':12}
]

juniors= filter(lambda actor: actor['age']>30, actors)
Fivers= filter(lambda actor: actor['age']%5==0, actors)
print(list(juniors))
print(list(Fivers))


person_info = {"name": "Sakib", "salary": 80000}
value = person_info.get("salary")
print(value)