""" This is a very classic problem, wherein we guess a number and the computer guesses a number too! If the numbers match, you win! """

from random import randint
p  = input("Enter a number :")
val = int(p)
x = randint(0,9)
#x = 6
if val == x :
    print ('CORRECT!')
elif val < x :
    print ('Your guess is less than the number.')
elif val > x :
    print ('Your guess is larger than the number.')
else :
    print ('Invalid Parameters!')
