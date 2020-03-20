# Lê as coordenadas x e y de dois pontos e retorna a área do retangulo
def area_retan(x1,y1,x2,y2):
    base = 0
    altura = 0
    if x1 < 0 or x2 < 0 or y1 < 0 or y2 < 0:
        return False
    else:
        base = x2 - x1
        altura = y2 - y1
        return base * altura


def main():
    print('Digite as coordenadas do primeiro ponto: ')
    x1 = float(input('X: '))
    y1 = float(input('Y: '))
    print('\nDigite as coordenadas do segundo ponto: ')
    x2 = float(input('X: '))
    y2 = float(input('Y: '))

    a = area_retan(x1,y1,x2,y2)
    if a == False:
        print('Não aceita valor negativo!')
    else:
        print(f'A área do retângulo é {a}')


main()