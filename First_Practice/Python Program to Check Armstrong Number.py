"""
abcd =  pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ...

example:
input: 153
output: yes
153 is a armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153

input:120
output: No
120 is not a armstrong number.
"""
from operator import truediv


#python program to determine whether
#the number is Armstrong number or not

#Function to calculate x raised to the power y

def power(x,y):

    if y == 0:
        return 1
    if y % 2 == 0:
        return power(x, y // 2) * power(x, y // 2)
    return x * power(x, y // 2 )* power(x, y //2)

#fucntion to calculate order of the number
def order(x):
    #variable to store of the number
    n = 0
    while (x != 0):
        n = n + 1
        x = x // 10
    return n

# function to check whether the given
def isAmstrong(x):
    n = order(x)
    temp = x
    sum1 = 0

    while(temp != 0 ):
        r = temp % 10
        sum1 = sum1 + power(r,n)
        temp = temp //10

    return (sum1 == x)

#driver code
x = 153
print (isAmstrong(x))

x =1253
print(isAmstrong(x))


# to check whether the given number is armstrong

n = 153
s = n
b = len(str(n))
sum1 = 0
while n != 0:
    r = n % 10
    sum1 = sum1 + (r ** b)
    n = n // 10
if s == sum1:
    print("the given numer", s, "is armstrong number")
else:
    print("the given numer", s, "is not a armstrong number")
    # if conditions satisfies


def is_armstrong(num):
    num_str = str(num)
    n = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit)**n
    if sum == num:
        return True
    else:
        return False

num = 153
print(is_armstrong(num))


# digit by sum aprroach to check for Amrstromg number
import math

def insArmstrong (num):
    n = num
    numDigits = 0
    sum = 0

    #Find number of digits in num

    while n > 0:
        n//= 10
        numDigits += 1

    n = num

    #Calculate sum of digits raised to the power of numDigits
    while  n > 0:
        digit = n % 10
        sum += math.pow(digit, numDigits)
        n //= 10

    #check if num is Armstrong number or not
    if sum == num:
        return True
    return False

#example 1
num1 =  1634
if isAmstrong(num1):
    print(num1, "Is an Armstrong number")
else:
    print(num1, "Is not an Armstrong number")

#example 2
num2 =  120
if isAmstrong(num2):
    print(num2, "Is an Armstrong Number")
else:
    print(num2, "Is not an Armstrong Number")

#Python program to check if a number
# is an Armstrong number in return statement

def is_armstrong_number(number):
    return sum(int(digit)**len(str(number)) for digit in str(number)) == number

#example
num = 153
if is_armstrong_number(num):
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is not an Armstrong number")