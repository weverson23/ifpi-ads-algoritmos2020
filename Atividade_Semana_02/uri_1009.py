def main():
    # entrada
    a = input()
    b = float(input())
    c = float(input())

    # processamento
    salario = b + (c * 15/100)

    # saída
    print('TOTAL = R$ {:.2f}'.format(salario))


main()