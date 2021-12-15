def potencia(a, n, contador):
    resultado = 1

    for i in range(n):
        resultado = resultado * a
        contador += 1

    return resultado, contador

def main():
    a = int(input("Digite o valor de a: "))
    n = int(input("Digite o valor de n: "))

    resultado = potencia(a, n, 0)

    print("Resultado:", resultado[0])
    print("No de execucoes:", resultado[-1])

if __name__ == "__main__":
    main()
