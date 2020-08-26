def impar_entre_limite(a,b):
    for i in range(a+1,b):
        if i % 2 != 0:
            print(i)


def main():
    li = int(input('Digite o limite inferior: '))
    ls = int(input('Digite o limite superior: '))
    impar_entre_limite(li,ls)


main()   