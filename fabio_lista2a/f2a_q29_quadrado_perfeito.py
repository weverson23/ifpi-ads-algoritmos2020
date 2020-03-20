# Lê um número de 4 dígitos e diz se é ou não um quadrado perfeito
def quad_perf(a):
    m = a // 1000
    c = (a % 1000) // 100
    d = ((a % 1000) % 100) // 10
    u = ((a % 1000) % 100) % 10

    quad = a ** (1/2)

    d1 = (m * 10) + c
    d2 = (d * 10) + u

    if quad == (d1 + d2):
        return True
    else:
        return False


def main():
    n = int(input('Digite um número de 4 dígitos: '))

    if quad_perf(n) == True:
        print(f'O número {n} é um quadrado perfeito')
    else:
        print(f'O número {n} não é um quadrado perfeito')


main()
