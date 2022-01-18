import math

def ordenar_tempo_final(atividade):
    return atividade[-1]

def agendamento(atividades):
    atividades.sort(key=ordenar_tempo_final)
    tempo_final = - math.inf
    agenda = []

    for i in range(len(atividades)):
        if atividades[i][0] > tempo_final:
            agenda.append(atividades[i])
            tempo_final = atividades[i][-1]

    return agenda

def entrada():
    atividades = []
    print("\nDigite apenas numeros...\n")

    while True:
        linha = input("Digite <tempo inicial> <tempo final> ou '0' para sair: ")
        if linha == "0": break

        linha = linha.split()
        atividades.append([int(linha[0]), int(linha[-1])])

    return atividades

def printar_agenda(agenda):
    
    print()
    for i in range(len(agenda)):
        print("Atividade {}:".format(i+1))
        print("\tTempo inicial: {}".format(agenda[i][0]))
        print("\tTempo final: {}".format(agenda[i][-1]))
        print()


def main():
    atividades = entrada()
    agenda = agendamento(atividades)
    printar_agenda(agenda)


if __name__ == "__main__":
    main()
