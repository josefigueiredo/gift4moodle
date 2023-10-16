#!/usr/bin/python3
#-*- coding: utf-8 -*-

#
# O objetiv é gerar um arquivo texto contendo uma lista de números binários gerados aleatorioamente
# o arquivo resutlado deve estar no formato GIFT para ser imprtado pelo moodle

from random import randint
#abre um arquivo vazio para escrita
rndrnd2bin = open('arithmetics/rnd+rnd2bin.gift','w')
binbin2bin = open('arithmetics/bin+bin2bin.gift','w')
Compl2binbin2bin = open('arithmetics/Compl2_bin+bin2bin.gift','w')

for i in range(50):
    # gera numeros aleatorios 
    oper1 = randint(0,32)
    oper2 = randint(0,31)

    #converte os operadores aleatoriamente para uma das 4 bases
    opr1 = randint(1,4)
    if opr1 == 1:
        oper1Conv = '0x'+format(oper1, "02x")
    elif opr1 == 2:
        oper1Conv = '0b'+format(oper1, "03b")
    elif opr1 == 3:
        oper1Conv = '0o'+format(oper1, "03o")
    elif opr1 == 4:
        oper1Conv = '0d'+str(oper1)

    opr2 = randint(1,4)
    if opr2 == 1:
        oper2Conv = '0x'+format(oper2, "02x")
    elif opr2 == 2:
        oper2Conv = '0b'+format(oper2, "08b")
    elif opr2 == 3:
        oper2Conv = '0o'+format(oper2, "03o")
    elif opr2 == 4:
        oper2Conv = '0d'+str(oper2)


    #converte para binario no formato de 8 bits (preenche com zero a esquerda)
    resDec = oper1 + oper2
    resBin = format(resDec % (1<<6), "06b")
    
    linhas = []
    linhas.append('Convenção: 0x indica hexadecimal; 0b indica binário; 0o indica octal e 0d indica decimal; resposta em binário com 6 bits.\n')
    linhas.append('Resolver a operação aritmética:\n')
    linhas.append(''+oper1Conv+' + '+oper2Conv+'=')
    linhas.append(' {='+str(resBin)+'}\n\n')

    # grava no arquivo no formato GIFT
    rndrnd2bin.writelines(linhas)

rndrnd2bin.close()


for i in range(50):
    # gera numeros aleatorios entre 0 a 31
    oper1 = randint(0,31)
    oper2 = randint(0,32)
    resDec = oper1 + oper2

    #converte para binario no formato de 6 bits (preenche com zero a esquerda)
    bOper1 = format(oper1 % (1 << 6), "06b")
    bOper2 = format(oper2 % (1 << 6), "06b")
    resBin = format(resDec % (1 << 6), "06b")
    
    linhas = []
    #     Qual é o valor de pi (até 3 casas decimais)? {#3.1415:0.0005}.
    linhas.append('Convenção: resposta em binário com 6 bits.\n')
    linhas.append('Resolver a operação aritmética:\n')
    linhas.append(''+str(bOper1)+' + '+str(bOper2)+'=')
    linhas.append(' {='+str(resBin)+'}\n\n')

    # grava no arquivo no formato GIFT
    binbin2bin.writelines(linhas)

binbin2bin.close()


for i in range(50):
    # gera numeros aleatorios entre -15 a 15
    oper1 = randint(-15,16)
    oper2 = randint(-16,15)
    resDec = oper1 + oper2

    #converte para binario no formato de 6 bits (preenche com zero a esquerda)
    bOper1 = format(oper1 % (1 << 6), "06b")
    bOper2 = format(oper2 % (1 << 6), "06b")
    resBin = format(resDec % (1 << 6), "06b")
    
    linhas = []
    #     Qual é o valor de pi (até 3 casas decimais)? {#3.1415:0.0005}.
    linhas.append('Convenção: Utilizando Complemento de 2; resposta em binário com 6 bits.\n')
    linhas.append('Resolver a operação aritmética:\n')
 
    linhas.append(''+str(bOper1)+' + '+str(bOper2)+'=')
    linhas.append(' {='+str(resBin)+'}\n\n')

    # grava no arquivo no formato GIFT
    Compl2binbin2bin.writelines(linhas)

Compl2binbin2bin.close()
