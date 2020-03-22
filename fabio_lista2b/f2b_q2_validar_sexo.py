# Lê uma letra e verifica se letra é "F" ou "M" , sendo F - Feminino, M - Masculino
def sexo(a):
    if a == 'F' or a == 'f':
        return 'Feminino'
    elif a == 'M' or a == 'm':
        return 'Masculino'
    else:
        return 'Sexo Inválido'


def main():
    s = input('Digite F para feminino  e M para masculino: ')
    print(sexo(s))


main()