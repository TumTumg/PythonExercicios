from Exercicios import Exercicios

class Control:
    def __init__(self):
        self.opcao = -1
        self.exer = Exercicios()

    def coletar(self):
        self.exer.num1 = int(input("Informe o primeiro número: "))
        self.exer.num2 = int(input("Informe o segundo número: "))

    def coletarApenasUm(self):
        self.exer.num1 = int(input("Informe um número: "))

    def menu(self):
        self.opcao = int(input("-----Menu-----\n\n" +
                              "\n0.Sair"          +
                              "\n1. Somar"        +
                              "\n2. Subtrair"     +
                              "\n3. Dividir"      +
                              "\n4. Multiplicar"  +
                              "\n5. Tabuada"      +
                              "\n6. Contando até dez!!!!" +
                              "\n7. Pares até vinte!" +
                              "\n8. Soma dos números até cem" +
                              "\n9. Múltiplos de 5 até 50" +
                              "\n10. Número digitado é par ou impar?" +
                              "\n11. Número digitado é negativo, positivo ou zero?" +
                              "\n12. Indo até o número digitado" +
                              "\n13. Somando até o número digitado" +
                              "\n14. Números primos até 20" +
                              "\n15. Número digitado é primo?" +
                              "\n16. Fatorial do número digitado" +
                              "\n17. Imprimir Fibonacci" +
                              "\n18. Número digitado é termo Fibonacci?" +
                              "\n19. Soma dos digitos dos números" +
                              "\n20. Pares e impares até o nímero digtado" +
                              "\n21. Números primos até o nímero digitado:" +
                              "\n22. Sequência de Collatz" +
                              "\n23. Soma dos números pares e ímpares até um número" +
                              "\n24. Verificar se um número é perfeito" +
                              "\nEscolha uma das opções acima: "))

    def operacao(self):
        while(self.opcao != 0):
            self.menu() #Mostrando o menu
            if(self.opcao == 0):
                print("Obrigado!")
            elif(self.opcao == 1):
                self.coletar()
                print(self.exer.somar())
            elif(self.opcao == 2):
                self.coletar()
                print(self.exer.subtrair())
            elif(self.opcao == 3):
                self.coletar()
                print(self.exer.dividir())
            elif(self.opcao == 4):
                self.coletar()
                print(self.exer.multiplicar())
            elif(self.opcao == 5):
                self.coletar()
                print(self.exer.tabuada())
            elif (self.opcao == 6):
                print(self.exer.ateDez())
            elif (self.opcao == 7):
                print(self.exer.paresUmAVinte())
            elif (self.opcao == 8):
                print(self.exer.somaAteCem())
            elif (self.opcao == 9):
                print(self.exer.multiploCinco())
            elif (self.opcao == 10):
                self.coletar()
                print(self.exer.parImpar())
            elif (self.opcao == 11):
                self.coletar()
                print(self.exer.posNegZero())
            elif (self.opcao == 12):
                self.coletarApenasUm()
                print(self.exer.ateDig())
            elif (self.opcao == 13):
                self.coletarApenasUm()
                print(self.exer.somaAteDig())
            elif (self.opcao == 14):
                 print(self.exer.imprimirPrimos())
            elif (self.opcao == 15):
                self.coletarApenasUm()
                print(self.exer.verificandoPrimo())
            elif (self.opcao == 16):
                self.coletarApenasUm()
                print(self.exer.calcularFatorial())
            elif (self.opcao == 17):
                 print(self.exer.sequenciaFibonacci())
            elif (self.opcao == 18):
                self.coletarApenasUm()
                print(self.exer.verificarFibonacci())
            elif (self.opcao == 19):
                self.coletarApenasUm()
                print(self.exer.calcularSomaDigitos())
            elif (self.opcao == 20):
                self.coletarApenasUm()
                print(self.exer.DigParesImpares())
            elif (self.opcao == 21):
                self.coletarApenasUm()
                print(self.exer.DigPrimosAte())
            elif (self.opcao == 22):
                self.coletarApenasUm()
                print(self.exer.sequenciaCollatz())
            elif (self.opcao == 23):
                self.coletarApenasUm()
                print(self.exer.somaParesImpares())
            elif (self.opcao == 24):
                self.coletarApenasUm()
                print(self.exer.numeroPerfeito())
            else:
                print("Código escolhido não é válido!")
