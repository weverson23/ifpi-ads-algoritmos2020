def fatorial(f):
    aux = f
    fat = 1
    for i in range(1,f):
        fat = fat * aux
        aux = aux - 1
    print(fat)

def main():
    f = int(input('Digite o valor para saber seu fatorial: '))
    fatorial(f)


main()