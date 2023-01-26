palavra = input('Informe a palavra: ')
tamanho = len(palavra) - 1
while tamanho >= 0:
    print(palavra[tamanho], end = '')
    tamanho -=1

