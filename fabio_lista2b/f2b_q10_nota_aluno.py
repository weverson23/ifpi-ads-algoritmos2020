# Lê duas notas de um aluno e retorna se foi ou não aprovado de acordou com o conceito
def nota(a,b):
    c = 0
    m = (a + b) / 2
    if m > 10:
        print('Valor inválido')
    if m >= 9:
        c = 'A'
    elif m >= 7.5:
        c = 'B'
    elif m >= 6:
        c = 'C'
    elif m >= 4:
        c = 'D'
    else:
        c = 'E'

    if c == 'A' or c == 'B' or c == 'C':
        print(f'A média do aluno foi {m}\nConceito: {c}\nAPROVADO')
    else:
        print(f'A média do aluno foi {m}\nConceito: {c}\nREPROVADO') 


def main():
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a primeira nota: '))

    c = nota(n1,n2)


main()
