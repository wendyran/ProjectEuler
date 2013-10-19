#############09062013###################
# 1. Multiples of 3 and 5
ans=0
for m in range(1,1000):
    if m % 3 == 0 or m % 5 == 0:
        ans=ans+m
print(ans)

# 1. Multiples of 3 and 5
sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])

#############09272013###################
## 2. Fibonacci Numbers
sums=0
a1=1
a2=2
while(a2 <= 4000000):
    na2=a1+a2
    a1=a2
    a2=na2
    if(a1 % 2 == 0):
        sums=sums+a1
print(sums)

#######3. Largest Prime Factor
### Pyprimes
import scipy
import pyprimes
pyprimes
pyprimes.factors(600851475143)

max(pyprimes.factors(600851475143))

####
n=600851475143
i=2
while (i * i < n):
    if(n % i == 0):
        n=n/i
    i=i+1
print(n)

####### 4. Palindrome Product
list_a = ['1','2','3','4','5','6','7','8']
list_a[::-1]

int(str(311)[::-1])

#############10112013###################
z=0
for i in range(999,100,-1):
    for j in range(999,100,-1):
        if i*j==int(str(i*j)[::-1]):
            if i*j>z:
                z=i*j
z

#############10182013###################
###### 5. Smallest Multiple
#k=2520
#m=k*11*13*17*19
#while i in range(2520,m,1):
#    if i % 11 != 0:
#        i=i+1
#    elif i % 13 != 0:
#        i=i+1
#    elif i % 17 != 0:
#        i=i+1
#    elif i % 19 != 0:
#        i=i+1
#    else:
#        s=i
#print s

2*3*4*5*7*3

a=2*3*4*5*7*3*11*13*2*17*19
print a
# all(map(lambda x: a % x == 0, range(1, 21)))

##### 6. Sum square difference
dd = 0
for i in range(1, 100, 1):
    for j in range(i + 1, 101, 1):
        dd = dd + 2 * i * j
print dd

##### 7. 10001st prime
import scipy
import pyprimes
pyprimes

pyprimes.nth_prime(10001)

limit = 0
limit += 1