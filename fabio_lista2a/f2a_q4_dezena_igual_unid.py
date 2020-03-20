# Lê um número de dois dígitos diz se a dezena é igual ou não a unidade
def dezena_igual_uni(a):
    d = a // 10 
    u = a % 10
    if d == u:
        return True
    else:
        return False


def main():
    n = int(input('Digite o valor: '))
    if dezena_igual_uni(n):
        print('A dezena é igual a unidade.')
    else:
        print('A dezena é diferente da unidade.')

main()