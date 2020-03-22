# Lê o preço de 3 produtos e retorna o de menor preço
def preco(a,b,c):
    menor = a
    if b < a:
        menor = b
    elif c < a:
        menor = c
    return menor


def main():
    n1 = float(input('Digite o preço do primeiro produto: '))
    n2 = float(input('Digite o preço do segundo produto: '))
    n3 = float(input('Digite o preço do terceiro produto: '))

    p = preco(n1,n2,n3)
    print(f'O menor preço é {p}')


main()

    