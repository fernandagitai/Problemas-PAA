

def escolher_convidados(pares):
    total_pessoas = len(pares)
    convidados = [1]*total_pessoas

    for pessoa in pares:
        conhecidos = len(pares[pessoa])
        desconhecidos = total_pessoas - conhecidos
        
        if conhecidos < 5 or desconhecidos < 5:
            identificador = int(pessoa)
            convidados[identificador] = 0
    
    return convidados


def entrada():
    print("\nDigite apenas numeros...\n")

    qtd_pessoas = int(input("Digite quantas pessoas serao analisadas: "))
    print("O identificador ira comecar no ZERO.\n")
    pares = {}

    for i in range(qtd_pessoas):
        identificador = str(i)
        pares[identificador] = []

    while True:
        linha_par = input("Digite <id1> <id2> dos pares ou '0' para finalizar: ")
        if linha_par == "0": break

        linha_par = linha_par.split()
        pares[linha_par[0]].append(linha_par[-1])
        pares[linha_par[-1]].append(linha_par[0])

    return pares

def printar_convidados(convidados):
    saida_convidados = "Convidados: "
    saida_nao_convidados = "Nao convidados: "

    for i in range(len(convidados)):

        if convidados[i]:
            if saida_convidados != "Convidados: ":
                saida_convidados += ", "
            saida_convidados += str(i)
        else:
            if saida_nao_convidados != "Nao convidados: ":
                saida_nao_convidados += ", "
            saida_nao_convidados += str(i)

    print("\n" + saida_convidados)
    print(saida_nao_convidados + "\n")

def main():
    pares = entrada()
    convidados = escolher_convidados(pares)
    printar_convidados(convidados)


if __name__ == "__main__":
    main()
