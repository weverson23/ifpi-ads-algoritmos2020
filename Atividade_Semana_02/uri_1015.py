def main():
    # entrada
    x1,y1 = input().split(' ')
    x2,y2 = input().split(' ')

    # processamento
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
    distancia = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1/2)

    # saída
    print('{:.4f}'.format(distancia))    


main()