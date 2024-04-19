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
                              "\n0.Sair"         +
                              "\n1. Somar"       +
                              "\n2.Subtrair"     +
                              "\n3. Dividir"     +
                              "\n4. Multiplicar" +
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
            elif (self.opcao == 3):
                self.coletar()
                print(self.exer.dividir())
            elif (self.opcao == 4):
                self.coletar()
                print(self.exer.multiplicar())
            else:
                print("Código escolhido não é válido!")