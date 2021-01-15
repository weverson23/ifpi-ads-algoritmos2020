def main():
    # entrada
    a,b,c = map(float, input().split())

    # processamento e saída
    perimetro = 0
    area = 0
    
    if a + b > c and a + c > b and b + c > a:
        perimetro = a + b + c
        print('Perimetro = {:.1f}'.format(perimetro))
    else:
        area = ((a + b) * c) / 2
        print('Area = {:.1f}'.format(area))


main()