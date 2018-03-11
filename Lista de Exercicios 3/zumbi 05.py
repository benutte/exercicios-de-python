# -*- coding: utf-8 -*-

a = int(input(" Digite um  número: "))
b = int(input(" Digite outro número: "))


while a % b != 0:
    a, b = b, a % b
print b
    
