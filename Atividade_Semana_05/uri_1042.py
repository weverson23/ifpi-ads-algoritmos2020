def main():
    # entrada
    a,b,c = map(int, input().split())
    
    # processamento
    maior = 0
    meio = 0
    menor = 0

    if a > b and a > c and b > c:
        maior = a
        meio = b
        menor = c
    elif a > b and a > c and c > b:
        maior = a
        meio = c
        menor = b
    elif b > a and b > c and a > c:
        maior = b
        meio = a
        menor = c
    elif b > a and b > c and c > a:
        maior = b
        meio = c
        menor = a
    elif c > a and c > b and a > b:
        maior = c
        meio = a
        menor = b
    else:
        maior = c
        meio = b
        menor = a

    # saída
    print(menor)
    print(meio)
    print(maior)
    print('\n{}'.format(a))
    print(b)
    print(c)


main()