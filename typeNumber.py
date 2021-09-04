#type number
#so nguyen
# a = 6clc
# print(type(a))
#so thuc
# b = 2.1
# print(type(b))

#decimal
# import thu vien decimal 
from decimal import *
# lay toi da 20 chu so phan nguyen va thap phan
getcontext().prec = 20
print(Decimal(1) / Decimal(7))

# Kieu phan so
from fractions import *
frac = Fraction(1,3)
print(type(frac))
print(frac)

#kieu so phuc
c = complex(2,2)
print(c)
print(c.real)
print(c.imag)

