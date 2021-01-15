def main():
    # entrada
    s = float(input())

    # processamento
    novo_salario = 0
    rejuste = 0
    porcentagem = 0

    if s >= 0 and s <= 400:
        porcentagem = 15
        rejuste = s * porcentagem / 100
        novo_salario = s + rejuste
    elif s > 400 and s <= 800:
        porcentagem = 12
        rejuste = s * porcentagem / 100
        novo_salario = s + rejuste
    elif s > 800 and s <= 1200:
        porcentagem = 10
        rejuste = s * porcentagem / 100
        novo_salario = s + rejuste
    elif s > 1200 and s <= 2000:
        porcentagem = 7
        rejuste = s * porcentagem / 100
        novo_salario = s + rejuste
    else:
        porcentagem = 4
        rejuste = s * porcentagem / 100
        novo_salario = s + rejuste

    # saída
    print('Novo salario: {:.2f}'.format(novo_salario))
    print('Reajuste ganho: {:.2f}'.format(rejuste))
    print('Em percentual: {} %'.format(porcentagem))


main()