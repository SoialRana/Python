def sum(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum(123, 232, 43))          
print(sum(43, 3, 23, 34,435))     
print(sum(34,22))
