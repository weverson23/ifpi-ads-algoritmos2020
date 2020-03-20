# recebe uma data e confirma se é ou não uma data válida
def valida_data(d,m,a):
    if m > 12 or m < 1:
        return False
    elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if d <= 31:
            return True
    elif m == 4 or m == 6 or m == 9 or m == 11:
        if d <= 30:
            return True
    elif m == 1:
        if(a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
            if d <= 29:
                return True
            elif d <= 28:
                return True
    else:
        return False


def main():
    print('Digite a data ')
    d = int(input('Dia: '))
    m = int(input('Mês: '))
    a = int(input('Ano: '))

    data = valida_data(d,m,a)
    
    if data == True:
        print('Data válida')
    else:
        print('Data inválida')


main()
    