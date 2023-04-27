import random
a=random.randint(1,100)
attempt=int(input('enter the total number of attempt'))
while attempt:
    n=int(input('enter number'))
    if n<a:
        print('your guess is smaller')
    elif n>a:
        print('your guess is larger')
    else:
        print('your guess is right')
        break
    attempt-=1
else:
    print("your attempt is over")10
