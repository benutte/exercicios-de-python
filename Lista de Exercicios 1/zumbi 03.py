# -*- coding: utf-8 -*-
dias = int(input(" Digite a quantidade de dia: "))
horas = int(input(" Digite a quantidade de horas: "))
minutos = int(input(" Digite a quantidade de minutos: "))
segundos = int(input(" Digite a quantidade de segundos: "))
resul1 = dias * 24 * 60 * 60
resul2 = horas * 60 * 60
resul3 = minutos * 60
total = resul1 + resul2 + resul3 + segundos

print 'O total em seguntos é:', total
