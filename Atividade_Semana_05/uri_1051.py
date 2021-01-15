def main():
    # entrada
    s = float(input())

    # processamento e saída
    desconto = 0

    if s <= 2000:
        print('Isento')
    elif s <= 3000:
        aux = s - 2000
        desconto = aux * 8/100
        print('R$ {:.2f}'.format(desconto))
    elif s <= 4500:
        aux = s - 2000
        aux2 = 1000 * 8/100
        aux3 = (s % 3000) * 18/100
        desconto = aux2 + aux3
        print('R$ {:.2f}'.format(desconto))
    elif s > 4500:
        aux = s - 2000
        aux2 = 1000 * 8/100
        aux3 = 1500 * 18/100
        aux4 = (s - 4500) * 28/100
        desconto = aux2 + aux3 + aux4
        print('R$ {:.2f}'.format(desconto))


main()