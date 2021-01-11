def main():
    # entrada
    n = int(input())

    # processamento
    ano = n // 365
    mes = (n % 365) // 30
    dia = (n % 365) % 30

    # saída
    print('{} ano(s)'.format(ano))
    print('{} mes(es)'.format(mes))
    print('{} dia(s)'.format(dia))


main()