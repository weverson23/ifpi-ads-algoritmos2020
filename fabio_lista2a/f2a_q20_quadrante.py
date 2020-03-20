# Lê a medida de um ângulo (entre 0º e 360º) e retorna o quadrante
def quadrante(a):
    if a > 380:
        return 'Fora escopo'
    elif a >= 0 and a <= 90:
        return 'Primeiro quadrante'
    elif a <= 180:
        return 'Segundo quadrante'
    elif a <= 270:
        return 'Terceiro quadrante'
    else:
        return 'Quarto quadrante'

    
def main():
    a = float(input('Digite o ângulo: '))
    print(quadrante(a))


main()