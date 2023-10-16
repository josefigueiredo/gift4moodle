#!/usr/bin/python3
#-*- coding: utf-8 -*-

#
# O objetiv é gerar um arquivo texto contendo uma lista de exercícios de conversão para complemento de 2
# o arquivo resutlado deve estar no formato GIFT para ser imprtado pelo moodle

from random import uniform

def excesso3(n):
    tabExcesso3 = {-4: [0,0,0],-3:[0,0,1],-2:[0,1,0],-1: [0,1,1],0: [1,0,0],
    1: [1,0,1],2: [1,1,0],3: [1,1,1]}
    return(tabExcesso3[n])

def normlalizaNumeroBinario(n,pV):
    for i in range(len(n)):
        if(n[i] == '1'):
            p1 = i
            break
    expoente = (pV - p1)
    numNorm = {"num":n[p1::],"exp":expoente}
    return(numNorm)
    

def notacaoIEEE754(s,numNorm):
    sinal= []
    sinal.append(s)

    expoente = excesso3(numNorm["exp"])
    numero = numNorm["num"]
    
    i = 1
    f = i+4
    mantissa = [] 
    for v in numero[i:f:]:
        mantissa.append(int(v))

    return(sinal + expoente + mantissa)


#abre um arquivo vazio para escrita
arq = open('pontoFlutuante/pontoFlutuante.gift','w')

for i in range(50):
    num = round(uniform(-5,5),3)
    sinal = 0 if num > 0 else 1
    fBin = []
    iBin = []

    absNum = abs(num)
    intPart = int(absNum)
    intEmBinComB = bin(intPart) 
    binIntPart = intEmBinComB[2::]
    posVirgula = len(binIntPart)-1
    
    for e in binIntPart:
        iBin.append(e)
    

    fPart = absNum-intPart
    for e in range(8):
        if fPart>0:
            tmp = fPart*2
            i = int(tmp)
            fBin.append(str(i))
            fPart = tmp-int(tmp)
    nBinario = iBin + fBin
    emNotIEE754 = notacaoIEEE754(sinal,normlalizaNumeroBinario(nBinario,posVirgula))
    
    paraArquivo = ""
    for c in emNotIEE754:
        paraArquivo += str(c)

    linhas = []
    #Qual é o valor de pi (até 3 casas decimais)? {#3.1415:0.0005}.
    linhas.append('Convenção: Notação IEEE 754 adaptada para 8bits\n')
    linhas.append(''+str(num)+'')
    linhas.append(' {='+str(paraArquivo)+'}\n\n')

    arq.writelines(linhas)

arq.close()


