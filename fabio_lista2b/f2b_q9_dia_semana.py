# Lê um valor e retorna o dia da semana. (1-Domingo, 2-Segunda etc)
def semana(a):
    if a < 1 or a > 7:
        return 'Valor inválido'
    elif a == 1:
        return 'Domingo'
    elif a == 2:
        return 'Segunda'
    elif a == 3:
        return 'Terça'
    elif a == 4:
        return 'Quarta'
    elif a == 5:
        return 'Quinta'
    elif a == 6:
        return 'Sexta'
    else:
        return 'Sábado'


def main():
    n = int(input('Digite um valor correspondente ao dia da semana: '))
    print(semana(n))


main()

        
