# -*- coding: utf-8 -*-

primeiro = int(input(" Digite o primeiro valor: "))
segundo = int(input(" Digite o segundo valor: "))
terceiro = int(input(" Digite o terceiro valor: "))

if (primeiro == segundo == terceiro):
    print (" Você fez um triângulo Equilátero")
elif (primeiro != segundo == terceiro):
    print (" Você fez um triângulo isósceles")
elif (primeiro == segundo != terceiro):
    print (" Você fez um triângulo isósceles")
elif (primeiro == terceiro != segundo):
    print (" Você fez um triângulo isósceles")
else:
    (primeiro != segundo != terceiro)
    print (" Você fez um triângulo escaleno")
