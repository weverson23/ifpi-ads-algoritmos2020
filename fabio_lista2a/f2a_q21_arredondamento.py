# recebe um valor e faz o arredondamento
def arredonda(a):
    b = a % 2
    c = int(a)
    if c % 2 == 0:
        if b >= 0.5:
            return a + (1 - b)
        else:
            return a - b
    else:
        if b >= 1.5:
            return a + (2 - b)
        else:
            return c


def main():
    n = float(input('Digite um valor: '))
    print('O valor arredondado é: ',arredonda(n))


main()