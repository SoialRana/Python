text= input("Enter a string: ")
noOfDigits= 0
noOfLetter= 0
noOfWords=0
for x in text:
    x=x.lower()
    if x>='a' and x<='z':
        noOfLetter=noOfLetter+1
    elif x>='0' and x<='9':
        noOfDigits=noOfDigits+1
    elif x==' ':
        noOfWords=noOfWords+1


print("Number of digit: ",noOfDigits)
print("Number of letter: ",noOfLetter)
print("Number of words: ",noOfWords+1)

