from collections import Counter

def encontrando_p(lista, i, n):
    print(f"Local atual: i {i}, n {n}, item lista {lista[i]}")
    print("Lista:",lista)

    if i == n: return i

    if i == n - 1:
        if lista[i] >= lista[n]: return i
        else: return n

    m = (i + n) / 2

    if lista[m] > lista[m-1] and lista[m] > lista[m+1]:
        return m

    if lista[m] > lista[m + 1] and lista[m] < lista[m - 1]:
        return encontrando_p(lista, i, m-1)
    else:
        return encontrando_p(lista, m+1, n)



def entrada():
    entrada_str = input("Digite uma sequencia de numeros separados por ESPACO: ").split()
    print()
    return [int(i) for i in entrada_str]


def main():

    sequencia = entrada()
    sequencia = list(Counter(sequencia).keys())
    print(encontrando_p(sequencia, 0, len(sequencia)))

if __name__ == "__main__":
    main()

