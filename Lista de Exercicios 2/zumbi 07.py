# -*- coding: utf-8 -*-
lata = 18
valor_lata = 80
area = float(input(" Digite o tamanho da area em metros: "))
total_area = area / 3
while total_area >= lata:
    lata = lata + 18
total_lata = lata / 18
valor_total = total_lata * valor_lata
print "Você vai usar: %d latas" % total_lata
print "Você vai gastar: R$", valor_total
