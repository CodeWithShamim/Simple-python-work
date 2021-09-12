
value = input("Enter your text and number : ")

numOfLetters = 0
numOfWords = 0
numOfDigits = 0

for i in value:
    i = i.lower()
    if i>='a' and i<='z':
        numOfLetters =numOfLetters+1

    elif i>='0' and i<='9':
        numOfDigits =numOfDigits+1

    elif i== ' ':
        numOfWords = numOfWords+1



print("numbers of Letters : ", numOfLetters)
print("numbers of Digits : ", numOfDigits)
print("numbers of Words : ", numOfWords+1)













