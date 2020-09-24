def multiplo(a):
    aux = 9
    for i in range(0,9):
        if a % aux == 0:
            print(aux)
        aux = aux - 1


def main():
    n = int(input('Digite um valor para saber seus múltiplos: '))
    multiplo(n)


main()  