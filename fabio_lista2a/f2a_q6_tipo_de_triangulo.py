# recebe os valores de três ângulos e retorna o tipo de triângulo
def tipo_triangulo(a,b,c):
    if((a + b + c) > 180) or ((a + b + c) == 0):
        return False
    elif(a < 90) and (b < 90) and (c < 90):
        return 'Triângulo acutângulo'
    elif(a == 90) or (b == 90) or (c == 90):
        return 'Triângulo retângulo'
    elif(a > 90) or (b > 90) or (c > 90):
        return 'Triângulo obtusângulo'


def main():
    a = float(input('Primeiro ângulo: '))
    b = float(input('Segundo ângulo: '))
    c = float(input('Terceiro ângulo: '))

    print(tipo_triangulo(a,b,c))


main() 