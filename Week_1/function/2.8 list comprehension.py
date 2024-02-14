numbers=[45,23,43,65,42,76]
odds=[]
for num in numbers:
    if num % 2 == 1 and num%5==0:
        odds.append(num)
print(odds)
#odd_nums=[num for num in numbers if num % 2 ==1]
odd_nums=[num for num in numbers if num % 2 ==1 if num % 5 ==0] #ager for loop er shortcut eta 
         # this is not readable num or sohoje pora jai na 
print(odd_nums)

players=['sakib','musfiq','mustafiz']
ages=[23,44,13]
age_comb=[]
for player in players:
    print('player: ',player)
    for age in ages: # sakibier jonno sobgula age print korbe then musfiq er jonno sobgula age print korbe ...
        print(player,age)
        age_comb.append([player,age]) # age take se ekta list of list akare print korbe 
print(age_comb)

# uporer for loop k amra evabe short cut e likhte pari etake bola hoi list er comprehension but
# eta meaningful na ...uporer niyomei amra likhbo..sudhu jane rakha valo
age_comb2=[(player,age) for player in players for age in ages] # ekhane ()dewate list of tuple banay felbe ...
# jodi amra [] ditam taile list of list banay felto ..jemon ta ager khetre list of list banayche
print(age_comb2) # same age combination tai abar print korbe 


