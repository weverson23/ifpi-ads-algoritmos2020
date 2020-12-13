def main():
    # entrada
    c1,q1,v1 = input().split(' ')
    c2,q2,v2 = input().split(' ')
    c1 = int(c1)
    q1 = int(q1)
    v1 = float(v1)
    c2 = int(c2)
    q2 = int(q2)
    v2 = float(v2)

    # processamento
    total = q1 * v1 + q2 * v2

    # saída
    print('VALOR A PAGAR: R$ {:.2f}'.format(total))


main()