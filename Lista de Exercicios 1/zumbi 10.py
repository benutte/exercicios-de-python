# -*- coding: utf-8 -*-

quantidades = int(input(" Quantos cigarros são fumados por dia: "))
anos = int(input("Quantos anos já fumou: "))
total = anos * 365 * quantidades
dias = total / 144
print "Voce perdeu %.2f dias" % dias
