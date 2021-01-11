def main():
    # entrada
    a = int(input())
    b = int(input())

    # processamento
    litros = (a * b) / 12.0

    # saída
    print('{:.3f}'.format(litros))    


main()