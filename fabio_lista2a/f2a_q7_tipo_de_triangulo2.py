# Pelos ângulos retorna se o triângulo é isoseles, equilátero ou escaleno
def tipo_triangulo2(a,b,c):
    if((a + b + c) > 180) or ((a + b + c) == 0):
        return False
    elif a == b == c:
        return 'Triângulo equilátero'
    elif a != b != c:
        return 'Triângulo escaleno'
    else:
        return 'Triângulo isósceles'


def main():
    a = float(input('Primeiro ângulo: '))
    b = float(input('Segundo ângulo: '))
    c = float(input('Terceiro ângulo: '))

    print(tipo_triangulo2(a,b,c))


main()