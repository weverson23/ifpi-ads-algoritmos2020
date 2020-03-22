# Lê o o turno e retorna uma saudação respectiva a esse turno
def turno(a):
    if a == 'M' or a == 'm':
        return 'Bom dia!'
    elif a == 'T' or a == 't':
        return 'Boa tarde!'
    elif a == 'N' or a == 'n':
        return 'Boa noite!'
    else:
        return 'Valor Inválido'


def main():
    t = input('Digite a letra do turno.\nM - manhã  T - tarde e N - noite\n')
    print(turno(t))


main()