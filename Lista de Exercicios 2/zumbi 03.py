# -*- coding: utf-8 -*-
regulamento = 50
multa = 4
excesso = 0
peixe = int(input(" Digite a quantidade de peixe: "))
if peixe > regulamento:
    excesso =  peixe - regulamento
    multa = multa * excesso
    print (" João pagará: R$ %.2f" %multa)
else:
    print (" João não ultrapassou o excesso portanto pagará: R$ %.2f" % excesso)
