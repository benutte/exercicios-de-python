# -*- coding: utf-8 -*-

n = int(input(" Digite o Número: "))
a, b = 1,1
k = 1

while k <= n - 2:
    a, b = b, a + b
    k = k + 1
print ("Fib(%d) = %d" %(n,b))
    
