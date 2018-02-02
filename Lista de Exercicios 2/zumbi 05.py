# -*- coding: utf-8 -*-

a = int(input(" Digite o primeiro número: "))
b = int(input(" Digite o primeiro número: "))
c = int(input(" Digite o primeiro número: "))
 
if a > b and a > c:
    maior = a
elif b > c:
    maior = b
else:
    maior = c

print "O número maior é:", maior

if a < b and a < c:
    menor = a
elif b < c:
    menor = b
else:
    menor = c

print "O número menor é:", menor

    
