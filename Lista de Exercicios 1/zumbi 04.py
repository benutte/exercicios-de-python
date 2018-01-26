# -*- coding: utf-8 -*-
salario = float(input(" Digite seu salario: "))
aumento = float(input(" Digite a porcentagem do aumento: "))
resul1 = salario / 100
resul2 = resul1 * aumento
novo_salario = resul2 + salario
print 'O valor do aumento é R$ %.2f:' % resul2
print 'O novo salário é R$ %.2f:' % novo_salario
