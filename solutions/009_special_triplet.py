#Failed attempt to generate a pythagorean triple 
#It failed because i coudlnt generate every single triple
'''
import random
import math
#generates a complex number x in the form x + iy
#This complex number z is then squared and the real part is a
#and the imaginary part is b
x = random.randint(1, 10)
y = random.randint(1,10)
print(x, y)
a = abs(x**2 - (y**2))
b = 2* x*y
#c is calculated using standard pythogaros theorem
c = math.sqrt(a**2 + b**2)
print(a,b,c)  
#generates a,b,c a pythagorean triple

#(ka, kb, kc) is a triple fo rany nymber
#starting from 3 4 5
a,b,c = 3,4,5
for i in range(2,15):
    print(a*i, b*i, c*i)
    if (a*i + b*i + c*i == 100):
        print(a*i, b*i, c*i)
        break 
'''


#Real Solution
#a = m2 - n2, b = 2mn, c = m2 + n2
triple = [] #stores the triple that adds to 1000
for m in range(2,25):
    for n in range(1, m):
        a = m**2 - n**2
        b = 2*m*n
        c= m**2 + n**2
        print(a,b,c)
        if a+b+c == 1000:
            triple.append([a,b,c])
            break

product = 1

for i in triple[0]:
    product *= i
print(product)
