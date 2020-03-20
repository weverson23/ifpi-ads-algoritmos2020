# Lê a quantidade e o valor de horas aula de dois professores e retorna o maior salário
def salario(a,b):
    return a * b


def main():
    print('Professor 1:')
    h1 = int(input('Quantidade de horas aula: '))
    v1 = float(input('Valor da hora aula: '))
    print('Professor 2:')
    h2 = int(input('Quantidade de horas: '))
    v2 = float(input('Valor da hora aula: '))

    p1 = salario(h1,v1)
    p2 = salario(h2,v2)

    if p1 > p2:
        print('O maior salário é do Professor 1')
    else:
        print('O maior salário é do Professor 2')


main()

