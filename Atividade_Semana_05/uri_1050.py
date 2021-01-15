def DDD(n):
    if n == 61:
        print('Brasilia')
    elif n == 71:
        print('Salvador')
    elif n == 11:
        print('Sao Paulo')
    elif n == 21:
        print('Rio de Janeiro')
    elif n == 32:
        print('Juiz de Fora')
    elif n == 19:
        print('Campinas')
    elif n == 27:
        print('Vitoria')
    elif n == 31:
        print('Belo Horizonte')
    else:
        print('DDD nao cadastrado')


def main():
    # entrada
    n = int(input())
    
    # função DDD processa e mostra a saída
    DDD(n)


main()