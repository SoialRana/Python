try:
    result=45/0
except:
    print('error happened')
finally:
    print('finally here')
print('done')


try:
    result =20//5
except:
    print("error happened")
finally: #jodi code e error thake taile finally use kore thaki 
    print("finally here")


num = lambda a:a*a
print(num(2**2))