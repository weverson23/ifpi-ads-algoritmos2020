def soma_media(a):
    s = 0
    d = 0
    for i in range(0,a):
        i = int(input(f'Digite o {i+1}º valor: '))
        s = s + i 
        d = d + 1
    
    soma = s
    media = soma / d

    print(f'A soma dos valores é {soma}')
    print(f'Média dos valores é {media}')


def main():
    n = int(input('Digite o tamanho da lista: '))
    soma_media(n)


main()


