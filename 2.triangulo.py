def triangulos(ladoA,ladoB,ladoC):
    #verificação de existência:
    #Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra: um de seus #lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a #soma dos outros dois lados.

    #calculando a diferença entre os lados e colocando em módulo
    difAB = ladoA - ladoB
    difBC = ladoB - ladoC
    difAC = ladoA - ladoC
    lista = [difAB,difBC,difAC]
    n = 0
    while n < len(lista):
        if lista[n]<0:
            lista[n]*=-1
        n+=1
    print(lista)
    if ladoA > difBC and ladoB > difAC and ladoC > difAB:
        #próxima verificação é se a soma de dois lados é maior que o outro lado: 
        if ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:  
            #verificação de qual tipo de triângulo é:     
            if ladoA == ladoB and ladoB == ladoC:
                print('É um triângulo equilátero')
            elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
                print('É um triângulo isósceles')
            elif ladoA != ladoB and ladoB!= ladoC:
                print('É um triângulo escaleno')
        else: 
            print('Esses lados não formam um trângulo válido')
    else:
        print('Esses lados não formam um trângulo válido')


l1 = float(input('Informe o primeiro lado: '))
l2 = float(input('Informe o segundo lado: '))
l3 = float(input('Informe o terceiro lado: '))
if l1 > 0 and l2 > 0 and l3 > 0:
    triangulos(l1,l2,l3)
else:
    print('Os lados de um triângulo devem ser positivos!')