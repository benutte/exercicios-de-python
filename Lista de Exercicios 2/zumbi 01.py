# -*- coding: utf-8 -*-

primeiro = int(input(" Digite o primeiro valor: "))
segundo = int(input(" Digite o segundo valor: "))
terceiro = int(input(" Digite o terceiro valor: "))

if (primeiro == segundo == terceiro):
    print (" Você fez um triângulo Equilátero")
elif (primeiro == segundo and segundo != terceiro) or (segundo == terceiro and terceiro != primeiro) or (primeiro == terceiro and terceiro != segundo):
    print (" Você fez um triângulo isósceles")
else:
    (primeiro != segundo != terceiro)
    print (" Você fez um triângulo escaleno")
