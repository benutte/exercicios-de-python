# -*- coding: utf-8 -*-

num = int(input(" Digite um número:"))

for a in range(2, num):
    while num % a == 0:
        print (a)
        num /= a
    
