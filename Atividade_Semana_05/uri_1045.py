def main():
    # entrada
    a,b,c = map(float, input().split())

    # processamento e saída
    aux = 0

    if a < b:
        aux = a
        a = b
        b = aux
    
    if b < c:
        aux = b
        b = c
        c = aux

    if a < b:
        aux = a
        a = b
        b = aux

    if a >= b + c:
        print('NAO FORMA TRIANGULO')
    else:
        if a * a == (b * b) + (c * c):
            print('TRIANGULO RETANGULO')

        if a * a > (b * b) + (c * c):
            print('TRIANGULO OBTUSANGULO')

        if  a * a < (b * b) + (c * c):
            print('TRIANGULO ACUTANGULO')
        
        if a == b and b == c:
            print('TRIANGULO EQUILATERO')
        elif a == b or a == c or b == c:
            print('TRIANGULO ISOSCELES')


main()