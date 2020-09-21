def peso_boi(x):
    cont = 0
    magro = 0
    gordo = 0
    peso_aux1 = 0
    peso_aux2 = 10000000000000
    while cont < x:
        iden = int(input('Número de identificação: '))
        peso = float(input('Peso do boi: '))
        
        if peso > peso_aux1:
            peso_aux1 = peso
            gordo = iden
        if peso < peso_aux2:
            peso_aux2 = peso
            magro = iden
        cont = cont + 1
    print(f'Boi mais magro é {magro} que pesa {peso_aux1}')
    print(f'Boi mais gordo é {gordo} que pesa {peso_aux2}')


def main():
    n = int(input('Digite a quantidade de bois: '))
    peso_boi(n)


main()