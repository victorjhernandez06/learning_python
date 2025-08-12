"""
Simple interest =  (P x T x R) / 100

P is the principal amount
T is the time period (in years)
R is the Rate of interest per annum.
"""
##USING FUNCTION
def fun (p, t, r):
    return (p*t*r)/100

#given values for principal (p), time (t) in years and rate of interest (r) per annum
p, t, r = 8, 6, 8

#function calling
res = fun(p, t, r)
print (res)

##USING LAMBDA FUNCTION
si  = lambda p,t, r:(p*t*r)/100
#given values for principal (p), time (t) in years, and rates interest (r) per annum
p,t,r = 8,6,8

res=si(p,t,r)
print(res)

##Using List comprension

#given values for principal (p), time (t) in years, and rates interest (r) per annum

p,t,r = 8,6,8
si=[p*t*r/100][0]
print(si)

