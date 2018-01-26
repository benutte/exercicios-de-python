# -*- coding: utf-8 -*-

km = float(input(" Digite os km percorridos: "))
dias = float(input(" Digite a quantidade de dias: "))
total = dias * 60 + km * 0.15

print "O preço a pagar do carro alugado é R$ %.2f " % total
