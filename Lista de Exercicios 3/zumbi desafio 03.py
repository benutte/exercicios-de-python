# -*- coding: utf-8 -*-

num = int(input(" Digite um número: "))
cont = 1
divi = 0
while cont <= num:
    if num % cont == 0:
        divi += 1
    cont += 1
if divi == 2:
    print (" O número é primo")
else:
    print (" O número não é primo")
print divi
