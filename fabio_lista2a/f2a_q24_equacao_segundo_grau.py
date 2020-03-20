# Lê A, B e C da equação do segundo grau e retorna as raízes
def equacao_quad(a,b,c):
    x1 = 0
    x2 = 0
    delta = 0
    if a == 0:
        print('Não é uma equação quadrádica')
    else:
        delta = (b ** 2) - 4 * a * c
        x1 = (-b + (delta ** (1/2))) / 2 * a
        x2 = (-b - (delta ** (1/2))) / 2 * a
    
    print(f'as raizes são x1 = {x1} e x2 = {x2}')


def main():
    print('Digite os valores de da equação quadrática')
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    c = int(input('Digite C: '))

    equacao_quad(a,b,c)


main()