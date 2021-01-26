def main():
    # entrada da quantidade de casos
    qtd = int(input())

    # entrada e saída respectiva ao número de casos
    for i in range(qtd):
        n1, n2, n3 = map(float, input().split())
        media_pondera = (n1 * 2 + n2 * 3 + n3 * 5) / 10
        print('{:.1f}'.format(media_pondera))


main()