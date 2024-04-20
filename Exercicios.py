class Exercicios:
    def __init__(self):
        #Construtor
        self.num1 = 0
        self.num2 = 0
        self.tabNum1 = ""
        self.tabNum2 = ""
        self.i = 0

    def somar(self):
        return f"{self.num1} + {self.num2} = {self.num1 + self.num2}"

    def subtrair(self):
        return f"{self.num1} - {self.num2} = {self.num1 - self.num2}"

    def dividir(self):
        if(self.num2 == 0):
            return "Impossível dividir por zero"
        else:
            return f"{self.num1} / {self.num2} = {self.num1 / self.num2}"

    def multiplicar(self):
        return f"{self.num1} * {self.num2} = {self.num1 * self.num2}"

    def tabuada(self):
        for self.i in range(0, 11, 1):  # Inicio, fim, contagem) | i = contador
            self.tabNum1 += f"{self.num1} * {self.i} = {self.num1 * self.i}\n"
            self.tabNum2 += f"{self.num2} * {self.i} = {self.num2 * self.i}\n"
        return f"Tabuada do {self.num1}: \n{self.tabNum1} \n\n Tabuada do {self.num2}: \n{self.tabNum2}"

    def ateDez(self):
        for self.i in range(1, 11):
            print(self.i)

    def paresUmAVinte(self):
        for self.i in range(0, 21, 2):
            print(self.i)

    def somaAteCem(self):
        self.soma = 0
        for self.i in range(1, 101):
            self.soma += self.i
        return f"\nA soma dos números de 1 a 100 é: {self.soma}"

    def multiploCinco(self):
        for self.i in range(5, 55, 5):
            print(self.i)

    def parImpar(self):
        if (self.num1 % 2 == 0):
            self.resultado1 = f"O número {self.num1} é par."
        else:
            self.resultado1 = f"O número {self.num1} é ímpar."
        if (self.num2 % 2 == 0):
            self.resultado2 = f"O número {self.num2} é par."
        else:
            self.resultado2 = f"O número {self.num2} é ímpar."
        return self.resultado1, self.resultado2

    def posNegZero(self):
        if (self.num1 == 0):
            self.resultado1 = f"O número digitado: {self.num1} é zero"
        elif (self.num1 > 0):
            self.resultado1 = f"O número digitado: {self.num1} é positivo"
        else:
            self.resultado1 = f"O número digitado: {self.num1} é negativo"
        if (self.num2 == 0):
            self.resultado2 = f"O número digitado: {self.num2} é zero"
        elif (self.num2 > 0):
            self.resultado2 = f"O número digitado: {self.num2} é positivo"
        else:
            self.resultado2 = f"O número digitado: {self.num2} é negativo"
        return self.resultado1, self.resultado2

    def somaAteDig(self):
        self.soma = 0
        for self.i in range(1, self.num1):
            self.soma += self.i
        return f"\nA soma dos números de 1 à: {self.num1} é: {self.soma}"

