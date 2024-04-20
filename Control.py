from Exercicios import Exercicios

class Control:
    def __init__(self):
        self.opcao = -1
        self.exer = Exercicios()

    def coletar(self):
        self.exer.num1 = int(input("Informe o primeiro número: "))
        self.exer.num2 = int(input("Informe o segundo número: "))


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
                              "\n12. Somando do 1 até o número digitado!" +
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
                self.coletar()
                print(self.exer.somaAteDig())
            else:
                print("Código escolhido não é válido!")