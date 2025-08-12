##Factorial of a number - Python

n = 5
#initialize the factorial variable to 1
fact =  1

#calculate the factorial using a for loop
for i in range(1, n + 1):
    fact *= i

print(fact)


##USING A RECURSIVE APPROACH
def fact (n):
    #single line to find factorial
    return 1 if (n ==1 or n==0) else n * fact(n-1)

#driver code
num=5
print(fact(num))


##USING MATCH.FACTORIAL()
import math
def factorial(n):
    return(math.factorial(n))

#drive code
num = 5
print(factorial(num))

#USING NUMPY.PROD()
import numpy
n = 5
x=numpy.prod([i for i in range(1,n+1)])
print(x)

##USING PRIME FACTORIZATION.
def primeFactors(n):
    factors = {}
    i = 2
    while i*i <= n:
        while n % i == 0:
            if i not in factors:
                factors[i] = 0
            factors[i] += 1
            n //= 1
        i += 1
    if n > 1:
        if n not in factors:
            factors[n] = 0
        factors[n] += 1
    return factors
#Function to find factorial of a number
def factorial (n):
    result = 1
    for i in range(2, n+1):
        factors = primeFactors(i)
        for p in factors:
            result *= p ** factors[p]
    return result

#Drive code
num = 5
print(factorial(num))
