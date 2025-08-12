"""
A = P[1 + R/100]

compound interest = A -P
ehere
A is amount
P is the principal amount
R is the rate and
T ins the time span
"""

def compound_interest(principal, rate, time):
    #calculates compount interest
    Amount = principal * ( pow ((1 + rate / 100),time))
    CI = Amount - principal
    print ("compount interest is", CI)

#driver Code
#Taking input from user
principal = int(input("enter the principal amount:"))
rate = float(input("enter rate of interest: "))
time = int(input("Enter the time in years:"))
#function Call
compound_interest(principal,rate,time)


##Compount interest using for loop
def compound_interest (principal, rate, time):
    Amount = principal
    for i in range (time):
        Amount = Amount * (1 +rate/100)
    CI = Amount - principal
    print("compount Interes is: ", CI)
    #driver Code
compound_interest(1200,5.4,2)


