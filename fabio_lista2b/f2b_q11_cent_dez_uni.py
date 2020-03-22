# Lê um número inteiro menor que 1000 mostra a quantidade de centenas, dezenas e unidades do número.
def cen_dez_uni(a):
    c = a // 100
    d = (a % 100) // 10
    u = (a % 100) % 10

    if a > 1000:
        print('Valor inválido') 
    if c == 1 and d == 1 and u == 1:
        print(f'{a} = {c} centena , {d} dezena e {u} unidade')
    elif c > 1 and d == 1 and u == 1:
        print(f'{a} = {c} centenas , {d} dezena e {u} unidade')
    elif c > 0 and c > 1 and d > 1 and u == 1:
        print(f'{a} = {c} centenas , {d} dezenas e {u} unidade')
    elif c > 0 and c > 1 and d > 1 and u > 1:
        print(f'{a} = {c} centenas , {d} dezenas e {u} unidades')
    elif c == 0 and d == 1 and u == 1:
        print(f'{a} = {d} dezena e {u} unidade')
    elif c == 0 and d > 1 and u == 1:
        print(f'{a} = {d} dezenas e {u} unidade')
    elif c == 0 and d > 1 and u > 1:
        print(f'{a} = {d} dezenas e {u} unidades')
    elif c == 0 and d == 0 and u == 1:
        print(f'{a} = {u} unidade')
    elif c == 0 and d == 0 and u > 1:
        print(f'{a} = {u} unidades')


def main():
    n = int(input('\nDigite um valor menor que 1000: '))
    cen_dez_uni(n)


main()