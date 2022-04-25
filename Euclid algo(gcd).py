// LCM*GCD = product of two numbers


def gcd(a,b):
    if b==0:
        return a
    else:
	    return gcd(b,a%b)
a,b=map(int,input().split())
print(gcd(a,b))




"""

a,b=map(int,input().split())
while(b):
    x=a
    a=b
    b=x%b
print(a)
"""
