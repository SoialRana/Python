def multiple():
    return 3,4
print(multiple()) # tuple print korbe 

things= 'pen','tripod','water bolltle','charger','phone','webcam'
print(type(things))
#print(type(things)) #print korbe type  
print(things[0])
print(things[-2])
print(things[3:6]) # etake slice bole ..ekhetre 3 theke 6 porjonto show korbe

if 'phone' in things:
    print('exists')
for item in things:
    print(item)
print(len(things))
# things[0]='wagon'  # tuple er moddhe amra jinish gulo change korte parbo na 
# print(things)


# normally tuple amra change korte parbo na kintu tuple jodi mutable(List) jinish contain kore taile change korte parbo 
# jemon List ekta muitable ... ekhane amra list er value change korte pari tei ekhetre tuple changeable 


mega=([2,3,4],[6,8,9,5])
# print(type(mega)) # mega er class hocche tuple 
print(mega[0]) # ekhane first array ta print korbe
mega[0][1]=666 # mega er first j tuple item ta ache seta to ekta list ami seta change korbo na ...sei list er j 1 no index
# ta ache sekhane rakhbo 666 ..
print(mega)


# python tuple methods ....porasona 