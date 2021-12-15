
def virar_panqueca(panqueca, tamanho, n):
    maior_em_cima = list(reversed(panqueca[:tamanho])) + panqueca[tamanho:]
    print("Virando panqueca:", maior_em_cima)

    maior_em_baixo = list(reversed(maior_em_cima[:n]))

    return maior_em_baixo


def espatula(panqueca, n):
    
    if n == 1:
        return

    maior_pedaco = panqueca[0]
    tamanho = 0

    for i in range(n):
        if maior_pedaco < panqueca[i]:
            maior_pedaco = panqueca[i]
            tamanho = i + 1

    panqueca[:n] = virar_panqueca(panqueca, tamanho, n)
    print("Virando panqueca:", panqueca)
    print()

    espatula(panqueca, n-1)


def entrada():
    entrada_str = input("Digite uma sequencia de numeros separados por ESPACO: ").split()
    print()
    return [int(i) for i in entrada_str]


def main():
    panqueca = entrada()
    print("Panqueca:", panqueca)
    print()

    espatula(panqueca, len(panqueca))

if __name__ == "__main__":
    main()