def soma_3(x):
    aux = x
    aux2 = 1
    num = 1
    s = 0
    den = x
    while aux <= x:
        if  num % 2 != 0:
            s = s + (num/aux)
        else:
            s = s - aux/den

        aux = aux - aux2
        aux2 = aux2 + 1
    print(s)


def main():
    n = int(input('Digite o valor de N: '))
    soma_3(n)


main()
