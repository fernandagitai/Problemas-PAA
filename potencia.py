def potencia(a, n):

    if a == 0 or n == 0:
        return 1

    if n % 2 == 0:
        aux = potencia(a, n/2)
        return aux * aux
    else: return a * potencia(a, n-1)


def main():
    a = int(input("Digite o valor de a: "))
    n = int(input("Digite o valor de n: "))

    resultado = potencia(a, n)

    print("Resultado:", resultado)

if __name__ == "__main__":
    main()
