def data_recente(d1,m1,a1,d2,m2,a2):
    if a1 > a2:
        print(f'A data mais recente é: {d1}/{m1}/{a1}')
    elif a1 < a2:
        print(f'A data mais recente é: {d2}/{m2}/{a2}')
    elif a1 == a2 and m1 > m2:
        print(f'A data mais recente é: {d1}/{m1}/{a1}')
    elif a1 == a2 and m1 < m2:
        print(f'A data mais recente é: {d2}/{m2}/{a2}')
    elif a1 == a2 and m1 == m2 and d1 > d2:
        print(f'A data mais recente é: {d1}/{m1}/{a1}')
    else:
        print(f'A data mais recente é: {d2}/{m2}/{a2}')


def main():
    print('Digite a primeira data: ')
    d1 = int(input('Dia: '))
    m1 = int(input('Mês: '))
    a1 = int(input('Ano: '))
    print('Digite a segunda data: ')
    d2 = int(input('Dia: '))
    m2 = int(input('Mês: '))
    a2 = int(input('Ano: '))

    data_recente(d1,m1,a1,d2,m2,a2)


main()