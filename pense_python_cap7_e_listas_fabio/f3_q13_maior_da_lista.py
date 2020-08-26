def maior_valor(a):
    maior = 0
    for i in range(0,a):
        i = int(input(f'Digite o {i+1}º valor: '))
        if i > maior:
            maior = i

    print(f'O maior valor é {maior}')


def main():
    n = int(input('Digite o tamanho da lista: '))
    maior_valor(n)


main()


