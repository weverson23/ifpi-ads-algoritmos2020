def main():
    # entrada
    a,b = map(int, input().split())
    
    # processamento e saída
    if a % b == 0 or b % a == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')


main()