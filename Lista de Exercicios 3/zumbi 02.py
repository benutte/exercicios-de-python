# -*- coding: utf-8 -*-


nome = raw_input(" Digite o nome de usuário: ")
senha = raw_input(" Digite a senha de usuário: ")
   
while nome in senha:
    print (" Ops.. senha igual a nome de usuário, digite novamente!!")
    nome = raw_input(" Digite o nome de usuário: ")
    senha = raw_input(" Digite a senha de usuário: ")

    
