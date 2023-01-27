def fibonacci(num):
    primeiro = 0
    segundo = 1
    soma = 0
    cont = 0
    while cont < num:
        if cont == num-1:
            print(segundo, end='')
        else:
            print(segundo, end=',')
        soma = primeiro + segundo
        primeiro = segundo
        segundo = soma
        cont+=1

fibonacci(8)