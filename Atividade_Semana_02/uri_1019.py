def main():
    # entrada
    n = int(input())

    # processamento
    hora = n // 3600
    minutos = (n % 3600) // 60
    segundos = (n % 3600) % 60

    # saída
    print('{}:{}:{}'.format(hora,minutos,segundos))


main()