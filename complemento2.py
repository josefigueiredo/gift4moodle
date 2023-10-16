#!/usr/bin/python3
#-*- coding: utf-8 -*-

#
# O objetiv é gerar um arquivo texto contendo uma lista de exercícios de conversão para complemento de 2
# o arquivo resutlado deve estar no formato GIFT para ser imprtado pelo moodle

from random import randint
#abre um arquivo vazio para escrita
dec2bin = open('complemento2/complemento2dec2bin.gift','w')
bin2dec = open('complemento2/complemento2bin2dec.gift','w')

### decimal para binario 
for i in range(60):
	# gera numeros aleatorios entre -32 e 31	
	numero = randint(-32,31)

	#converte para binario no formato de 6 bits (preenche com zero a esquerda)
	resBin = format(numero % (1 << 6), "06b")
        	
	linhas = []
	linhas.append('Convenção: em Complemento de 2; 6bits.\n')
	linhas.append('Escreva '+str(numero)+' em binário:')
	linhas.append(' {='+str(resBin)+'}\n\n')

    # grava no arquivo no formato GIFT
	dec2bin.writelines(linhas)

dec2bin.close()


### binario para decimal
for i in range(60):
	# gera numeros aleatorios entre -32 e 31
	emDec = randint(-32,31)
	emBin = format(emDec % (1 << 6), "06b")
    	
	linhas = []
	linhas.append('Converter '+str(emBin)+' (em Complemento de 2) para decimal?')
	linhas.append(' {#'+str(emDec)+'}\n\n')
	
	# grava no arquivo no formato GIFT
	bin2dec.writelines(linhas)

bin2dec.close()

