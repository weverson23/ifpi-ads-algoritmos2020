# Lê um número e diz se é positivo ou negativo
def pos_neg(a):
    if a >= 0:
        return 'Positivo'
    else:
        return 'Negativo'


def main():
    n = float(input('Digite um número: '))
    print(pos_neg(n))


main()
    