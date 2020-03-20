# Lê um número de 4 dígitos e retorna se a soma das duas dezenas ao quadrado é igual ao valor oroginal
def expressao(a):
    m = a // 1000
    c = (a % 1000) // 100
    d = ((a % 1000) % 100) // 10
    u = ((a % 1000) % 100) % 10

    d1 = (m * 10) + c
    d2 = (d * 10) + u
    x = (d1 + d2) ** 2

    if x == a:
        return True
    else:
        return False


def main():
    print('Existem números que obedecem a característica \n2025 -> dividindo: 20 e 25 -> somando temos 45 -> 452 = 2025')
    n = int(input('\nDigite um valor entre 1000 e 9999: '))
    
    if expressao(n) == True:
        print(f'o valor {n} obedece a característica')
    else:
        print(f'o valor {n} não obedece a característica')


main()
