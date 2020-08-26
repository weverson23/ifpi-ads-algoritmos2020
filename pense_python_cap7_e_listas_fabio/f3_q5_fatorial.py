def fatorial(a):
    f = 1
    c = 1
    while c <= a:
        f = f * c
        c = c + 1
    return f



def main():
    n = int(input('Digite um número inteiro: '))
    x = fatorial(n)
    print(f'O fatorial de {n} é {x}')


main()