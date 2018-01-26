# -*- coding: utf-8 -*-
mercadoria = float(input(" Digite o valor da mercadoria: "))
porcento = float(input(" Digite o desconto em porcentagem: "))
desconto = porcento * (100 / mercadoria)
total = desconto - mercadoria
print 'O valor do desconto é R$: %2.f' % desconto
print 'O valor total com desconto é R$: %2.f'% total


