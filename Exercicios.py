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

    def ateDig(self):
        for self.i in range(1, self.num1 + 1):
            print(self.i)

    def somaAteDig(self):
        self.soma = 0
        for self.i in range(1, self.num1 + 1):
            self.soma += self.i
        return f"\nA soma dos números de 1 até {self.num1} é: {self.soma}"

    def imprimirPrimos(self):
        primos = []

        for num in range(1, 21):
            eh_primo = True
            for i in range(2, num):
                if num % i == 0:
                    eh_primo = False
                    break
            if eh_primo:
                primos.append(num)

        return f"Os números primos de 1 à 20 são: {primos}"

    def verificandoPrimo(self):
        if self.num1 <= 1:
            return f"{self.num1} não é primo."
        elif self.num1 == 2:
            return f"{self.num1} é primo."
        else:
            for self.i in range(2, self.num1):
                if self.num1 % self.i == 0:
                    return f"{self.num1} não é primo."
            return f"{self.num1} é primo."

    def calcularFatorial(self):
        if self.num1 < 0:
            return "O fatorial de números negativos não está definido."
        elif self.num1 == 0:
            return 1
        else:
            self.fatorial = 1
            for self.i in range(1, self.num1 + 1):
                self.fatorial *= self.i
            return f"O número fatorial de {self.num1} é {self.fatorial}"

    def sequenciaFibonacci(self):
        # Inicializando os dois primeiros termos da sequência
        self.termo1 = 0
        self.termo2 = 1

        # Imprimindo os dois primeiros termos
        print(self.termo1)
        print(self.termo2)

        # Loop para calcular os próximos termos e imprimi-los
        for self.i in range(2, 10):  # Vamos até o décimo termo, começando a contar a partir do zero
            self.proximoTermo = self.termo1 + self.termo2
            print(self.proximoTermo)

            # Atualizando os valores dos termos para os próximos cálculos
            self.termo1 = self.termo2
            self.termo2 = self.proximoTermo

    def verificarFibonacci(self):
        a, b = 0, 1
        while b < self.num1:
            a, b = b, a + b
        if b == self.num1:
            return f"{self.num1} é um número de Fibonacci."
        else:
            return f"{self.num1} não é um número de Fibonacci."

    def calcularSomaDigitos(self):
        self.soma = 0
        while self.num1:
            self.digito = self.num1 % 10
            self.soma += self.digito
            self.num1 //= 10
        return f"A soma dos digitos do número digitado é: {self.soma}"

    def DigParesImpares(self):
        pares = []
        impares = []

        for self.i in range(1, self.num1 + 1):
            if self.i % 2 == 0:
                pares.append(self.i)
            else:
                impares.append(self.i)

        return pares, impares

    def DigPrimosAte(self):
        primos = []

        for self.i in range(2, self.num1 + 1):
            eh_primo = True
            for j in range(2, int(self.i ** 0.5) + 1):
                if self.i % j == 0:
                    eh_primo = False
                    break
            if eh_primo:
                primos.append(self.i)

        return primos

    def sequenciaCollatz(self):
        # Função para imprimir a sequência de Collatz de um número
        collatz_seq = [self.num1]
        while self.num1 != 1:
            if self.num1 % 2 == 0:
                self.num1 //= 2
            else:
                self.num1 = self.num1 * 3 + 1
            collatz_seq.append(self.num1)
        return collatz_seq

    def somaParesImpares(self):
        # Função para calcular a soma dos números pares e ímpares até um número dado
        soma_pares = 0
        soma_impares = 0
        for num in range(1, self.num1 + 1):
            if num % 2 == 0:
                soma_pares += num
            else:
                soma_impares += num
        return soma_pares, soma_impares

    def numeroPerfeito(self):
        # Função para verificar se um número é perfeito
        soma_divisores = sum([i for i in range(1, self.num1) if self.num1 % i == 0])
        if soma_divisores == self.num1:
            return f"O número {self.num1} é um número perfeito."
        else:
            return f"O número {self.num1} não é um número perfeito."








