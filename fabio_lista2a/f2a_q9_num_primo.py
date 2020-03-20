# Lê um número entre 0 e 100 e retorna se é um número primo
def primo(a):
    if a < 0 or a > 100:
        return 'Fora do escopo'
    elif a == 1:
        return 'Não é primo'
    elif a == 2:
        return 'É primo'
    elif(a != 2) and (a % 2 != 0) and (a % a == 0):
        return 'É primo'
    else:
        return 'Não é primo'


def main():
    n = int(input('Digite um valor entre 0 e 100: '))
    print(primo(n))


main()