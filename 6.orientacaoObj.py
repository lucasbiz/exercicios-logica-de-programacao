#fatorialOrientada

class numero:
    def __init__(self,num):
        self.num = num

    def fat(self):
        if self.num == 0 or self.num == 1:
            return 1
        else:
            soma = 1
            for n in range(1,self.num+1):
                soma = soma*n
            return soma        

#cria um objeto com o atributo número com valor desejado 
num1 = numero(4)
num2 = numero(5)
#utiliza o método fat para obter o fatorial desse número
num1.num = num1.fat()
num2.num = num2.fat()

print(num1.num)
print(num2.num)

    