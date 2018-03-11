# -*- coding: utf-8 -*-

a = int(input(" Digite um número: "))
b = 0

while b * (b + 1) * (b + 2) < a:
    b += 1
if  b * (b + 1) * (b + 2) == a:
    print ("O número é triangular")
else:
    print (" O número não é triangular")
