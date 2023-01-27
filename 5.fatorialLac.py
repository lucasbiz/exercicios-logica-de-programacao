def fatorial(num):
    if num == 1 or num == 0:
        print(1)
    else:
        soma = 1
        while num > 1:
            soma *= num
            num -= 1
        print(soma)

fatorial(6)
    
