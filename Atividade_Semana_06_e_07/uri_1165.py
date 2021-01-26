def main():
    # entrada da quantidade de casos
    n = int(input())

    # função de entrada e saída respectiva ao número de casos
    for i in range(n):
        x = int(input())
        total = 0
        for j in range(1,x+1):
             if x % j == 0:
                 total = total + 1
        if total == 2:
            print('{} eh primo'.format(x))
        else: 
            print('{} nao eh primo'.format(x))


main()