# Lê 5 números e retorna o maior e o menor deles.
def maior(a,b,c,d,e):
    maior = 0
    if a > b and a > c and a > d and a > e:
        maior = a
    elif b > a and b > c and b > d and b > e:
        maior = b
    elif c > a and c > b and c > d and c > e:
        maior = c
    elif d > a and d > b and d > c and d > e:
        maior = d
    else:
        maior = e
    return maior


def menor(a,b,c,d,e):
    menor = 0
    if a < b and a < c and a < d and a < e:
        menor = a
    elif b < a and b < c and b < d and b < e:
        menor = b
    elif c < a and c < b and c < d and c < e:
        menor = c
    elif d < a and d < b and d < c and d < e:
        menor = d
    else:
        menor = e
    return menor


def main():
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    n3 = int(input('Digite o terceiro número: '))
    n4 = int(input('Digite o quarto número: '))
    n5 = int(input('Digite o quinto número: '))

    me = menor(n1,n2,n3,n4,n5)
    ma = maior(n1,n2,n3,n4,n5)

    print(f'O menor valor é {me} e o maior valor é {ma}')


main()


