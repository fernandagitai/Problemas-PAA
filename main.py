class Tabuleiro():

    def __init__(self, no_discos, no_torres):
        self.lista_torres = list(range(no_torres))

        self.torre_de_hanoi(no_discos)
        

    def torre_de_hanoi(self, n):
        # lista_polos = [torre_origem, torre_destino, torre_aux1, torre_aux2, ... , torre_auxN]

        if (n == 0):
            return
        
        if (n == 1):
            print(f'Mover o disco {n} da TORRE {self.lista_torres[0]}, para a TORRE {self.lista_torres[1]}')
            return

        for i in range(len(self.lista_torres)):
            if i == 0:
                var_aux = self.lista_torres[i]

            if i == len(self.lista_torres)-1:
                self.lista_torres[-1] = var_aux

            else: self.lista_torres[i] = self.lista_torres[i+1]
        

        print(f'Mover o disco {n - 1} da TORRE {self.lista_torres[0]}, para a TORRE {self.lista_torres[3]}')

        print(f'Mover o disco {n} da TORRE {self.lista_torres[0]}, para a TORRE {self.lista_torres[1]}')

        print(f'Mover o disco {n - 1} da TORRE {self.lista_torres[3]}, para a TORRE {self.lista_torres[1]}')

        for i in range(len(self.lista_torres)):
            if i == 0:
                var_aux = self.lista_torres[i]

            if i == len(self.lista_torres)-1:
                self.lista_torres[-1] = var_aux

            else: self.lista_torres[i] = self.lista_torres[i+1]

        self.torre_de_hanoi(int(n) - 2)



def main():
    print("\n")

    no_torres = int(input("Digite a quantidade de Torres: "))
    no_discos = int(input("Digite a quantidade de Discos: "))

    print("\n")
    novo_jogo = Tabuleiro(no_discos, no_torres)
    print("\n")


if __name__ == "__main__":
    main()

