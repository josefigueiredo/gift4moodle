#!/usr/bin/python
#-*- coding: utf-8 -*-

#
# O objetivo é gerar um arquivo texto contendo uma lista de números binários gerados aleatorioamente
# o arquivo resutlado deve estar no formato GIFT para ser imprtado pelo moodle


from random import randint
#abre um arquivo vazio para escrita
arqB2D = open('baseConversion/bin2dec.gift','w')
arqD2B = open('baseConversion/dec2bin.gift','w')
arqB2H = open('baseConversion/bin2hex.gift','w')
arqH2B = open('baseConversion/hex2bin.gift','w')
arqB2O = open('baseConversion/bin2oct.gift','w')
arqO2B = open('baseConversion/oct2bin.gift','w')
arqD2H = open('baseConversion/dec2hex.gift','w')
arqD2O = open('baseConversion/dec2oct.gift','w')
arqH2D = open('baseConversion/hex2dec.gift','w')
arqO2D = open('baseConversion/oct2dec.gift','w')

tamanho = 50
#bin 2 dec
for i in range(tamanho):
    # gera numeros aleatorios entre 0 e 255
    decimal = randint(0,255)

    #converte para binario no formato de 8 bits (preenche com zero a esquerda)
    binario = format(decimal, "08b")

    linhas = []
    #     Qual é o valor de pi (até 3 casas decimais)? {#3.1415:0.0005}.
    linhas.append('De binário para decimal: '+binario+'?')
    linhas.append(' {#'+str(decimal)+'}\n\n')

    # grava no arquivo no formato GIFT
    arqB2D.writelines(linhas)

arqB2D.close()

#dec 2 bin
for i in range(tamanho):
    # gera numeros aleatorios entre 0 e 255
    decimal = randint(0,255)

    #converte para binario no formato de 8 bits (preenche com zero a esquerda)
    binario = format(decimal, "08b")

    linhas = []
    #     Qual é o valor de pi (até 3 casas decimais)? {#3.1415:0.0005}.
    linhas.append('De decimal para binário: '+str(decimal)+'?')
    linhas.append(' {#'+binario+'}\n\n')

    # grava no arquivo no formato GIFT
    arqD2B.writelines(linhas)
arqD2B.close()

#bin 2 hex
for i in range(tamanho):
    # gera numeros aleatorios entre 0 e 255
    decimal = randint(0,255)

    #converte para binario no formato de 8 bits (preenche com zero a esquerda)
    binario = format(decimal, "08b")
    hexadecimal = format(decimal, "02x")

    linhas = []
    #     Qual é o valor de pi (até 3 casas decimais)? {#3.1415:0.0005}.
    linhas.append('De binário para hexadecimal: '+binario+'?')
    linhas.append(' {='+hexadecimal+'}\n\n')

    # grava no arquivo no formato GIFT
    arqB2H.writelines(linhas)
arqB2H.close()

#hex 2 bin
for i in range(tamanho):
    # gera numeros aleatorios entre 0 e 255
    decimal = randint(0,255)

    #converte para binario no formato de 8 bits (preenche com zero a esquerda)
    binario = format(decimal, "08b")
    hexadecimal = format(decimal, "02x")

    linhas = []
    #     Qual é o valor de pi (até 3 casas decimais)? {#3.1415:0.0005}.
    linhas.append('De hexadecimal para binário: '+hexadecimal+'?')
    linhas.append(' {#'+binario+'}\n\n')

    # grava no arquivo no formato GIFT
    arqH2B.writelines(linhas)
arqH2B.close()

#bin 2 oct
for i in range(tamanho):
    # gera numeros aleatorios entre 0 e 255
    decimal = randint(0,255)

    #converte para binario no formato de 8 bits (preenche com zero a esquerda)
    binario = format(decimal, "08b")
    octal = format(decimal, "03o")

    linhas = []
    #     Qual é o valor de pi (até 3 casas decimais)? {#3.1415:0.0005}.
    linhas.append('De binário para octal: '+binario+'?')
    linhas.append(' {#'+octal+'}\n\n')

    # grava no arquivo no formato GIFT
    arqB2O.writelines(linhas)
arqB2O.close()

#oct 2 bin
for i in range(tamanho):
    # gera numeros aleatorios entre 0 e 255
    decimal = randint(0,255)

    #converte para binario no formato de 8 bits (preenche com zero a esquerda)
    binario = format(decimal, "08b")
    octal = format(decimal, "03o")

    linhas = []
    #     Qual é o valor de pi (até 3 casas decimais)? {#3.1415:0.0005}.
    linhas.append('De octal para binário: '+octal+'?')
    linhas.append(' {#'+binario+'}\n\n')

    # grava no arquivo no formato GIFT
    arqO2B.writelines(linhas)
arqO2B.close()

#dec 2 hex
for i in range(tamanho):
    # gera numeros aleatorios entre 0 e 255
    decimal = randint(0,255)

    #converte para binario no formato de 8 bits (preenche com zero a esquerda)
    hexadecimal = format(decimal, "02x")

    linhas = []
    #     Qual é o valor de pi (até 3 casas decimais)? {#3.1415:0.0005}.
    linhas.append('De decimal para hexadecimal: '+str(decimal)+'?')
    linhas.append(' {='+hexadecimal+'}\n\n')

    # grava no arquivo no formato GIFT
    arqD2H.writelines(linhas)
arqD2H.close()

#dec 2 oct
for i in range(tamanho):
    # gera numeros aleatorios entre 0 e 255
    decimal = randint(0,255)

    #converte para binario no formato de 8 bits (preenche com zero a esquerda)
    octal = format(decimal, "02o")

    linhas = []
    #     Qual é o valor de pi (até 3 casas decimais)? {#3.1415:0.0005}.
    linhas.append('De decimal para octal: '+str(decimal)+'?')
    linhas.append(' {='+octal+'}\n\n')

    # grava no arquivo no formato GIFT
    arqD2O.writelines(linhas)
arqD2O.close()

#hex 2 dec
for i in range(tamanho):
    # gera numeros aleatorios entre 0 e 255
    decimal = randint(0,255)

    #converte para binario no formato de 8 bits (preenche com zero a esquerda)
    hexadecimal = format(decimal, "02x")

    linhas = []
    #     Qual é o valor de pi (até 3 casas decimais)? {#3.1415:0.0005}.
    linhas.append('De hexadecimal para decimal: '+hexadecimal+'?')
    linhas.append(' {#'+str(decimal)+'}\n\n')

    # grava no arquivo no formato GIFT
    arqH2D.writelines(linhas)
arqH2D.close()

#oct 2 dec
for i in range(tamanho):
    # gera numeros aleatorios entre 0 e 255
    decimal = randint(0,255)

    #converte para binario no formato de 8 bits (preenche com zero a esquerda)
    octal = format(decimal, "02o")

    linhas = []
    #     Qual é o valor de pi (até 3 casas decimais)? {#3.1415:0.0005}.
    linhas.append('De octal para decimal: '+octal+'?')
    linhas.append(' {#'+str(decimal)+'}\n\n')

    # grava no arquivo no formato GIFT
    arqO2D.writelines(linhas)
arqO2D.close()
