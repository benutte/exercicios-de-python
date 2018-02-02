# -*- coding: utf-8 -*-

ano = int(input(" Digite o ano, para saber se ele é bissexto: "))
if (ano % 4 == 0 and ano % 100 != 0):
    print (" O ano é bissexto")
elif (ano % 400 == 0):
    print (" O ano é bissexto")
else:
    print (" O ano não é bissexto")
