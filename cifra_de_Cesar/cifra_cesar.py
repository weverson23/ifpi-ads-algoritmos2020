def rotate_word(c,r):
    cifra = c
    aux1 = 0
    aux2 = 0
    for letra in cifra:
        aux1 = (ord(letra) + r)
        aux2 = chr(aux1)
        print(aux2,end='')


    


def main():
    
    cifra = input('Digite a palavra cifrada: ')
    rotacao = int(input('Digite a rotação: '))
    rotate_word(cifra,rotacao)


main()