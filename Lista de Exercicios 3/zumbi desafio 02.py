# -*- coding: utf-8 -*-

valorconta = int(input(" Digite o Valor da conta a ser paga: "))
valorpagamento = int(input(" Digite o valor do pagamento efetuado: "))
troco = [50, 20, 10, 5, 2, 1]
sub = (valorpagamento- valorconta)
for nota in troco:
    while sub >= nota:
        print ("Uma nota %d" %nota)
        sub -= nota

    
    

