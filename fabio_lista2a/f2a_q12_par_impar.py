# Lê um número e verifica se é par ou impar
def par_impar(a):
    if a % 2 == 0:
        return 'Número par'
    else:
        return 'Número impar'


def main():
    n = int(input('Digite um número: '))
    print(par_impar(n))


main()
