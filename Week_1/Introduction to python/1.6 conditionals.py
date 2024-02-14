# in,not, not in, is, is not

a=1
if(a>3):
    print('3 er beshi')
    print('koto beshi ke jane ')
elif a>2:
    print('2 er cheye beshi')
elif a==2:
    print('2 er soman')
else:
    print('chooto chotto rate ')

boss=False
if boss is not True:
    print('lunch er por asen')
else:
    print('tel er bakso niye aso boss re tel dimu')


# nested conditions
coin='head';
if boss!= True:
    print('boss you are joss')
    if coin=='tail':
        print('betting')
    else:
        print('bowling')
        if 5>2 and 1!=3:
            print('do something or')
else:
    print('you are loss not a boss')    