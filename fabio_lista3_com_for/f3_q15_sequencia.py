def sequen(x):
    a = 1
    b = 2
    for i in range(0,x):
        print(a)
        a = a + b
        b = b + 1


def main():
    n = int(input('Digite o tamanho da sequencia: '))
    sequen(n)


main()