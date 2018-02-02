# -*- coding: utf-8 -*-
valor = float(input(" Digite quanto você ganha por hora: "))
hora = float(input(" Digite o número de horas trabalhadas no mês: "))
total = valor * hora
ir = 0.11 * total
inss = 0.08 * total
sindicato = 0.05 * total
liquido = total - ir - inss - sindicato
print " + Salário Bruto é: R$ %.2f" %total
print " - IR (11%): R$", ir
print " - INSS (8%): R$ ", inss
print " - Sindicato (5%): R$", sindicato
print " = Salário Liquido: R$", liquido





