def main():
    # entrada
    a,b,c = input().split(' ')

    # processamento
    a = int(a)
    b = int(b)
    c = int(c)
    aux1 = a - b
    maior = (a + b + abs(aux1)) / 2
    aux2 = maior - c
    maior = (maior + c + abs(aux2)) / 2

    # saída
    print('{} eh o maior'.format(int(maior)))


main()