def soma_int(a):
    c = 0
    for i in range(1,a+1):
        c = c + i
    return c


def main():
    n = int(input('Digite um valor inteiro:  '))
    x = soma_int(n)
    print(f'A soma dos valores de 1 até {n} é {x}')


main()