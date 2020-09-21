def eleicao(e):
    i = 0
    a = 0
    b = 0
    c = 0
    brancos = 0
    nulos = 0
    maioria = 0

    while i < e:
        print(f'Eleitor Nº {i + 1}')
        print('1 = candidato A , 2 = candidato B, 3 = candidato C, 9 = nulo, 0 = branco')
        v = int(input('Digite o número do candidato: '))
        if v == 1:
           a = a + 1
        elif v == 2:
            b = b + 1
        elif v == 3:
            c = c + 1
        elif v == 9:
            nulos = nulos + 1
        elif v == 0:
            brancos = brancos + 1
        i = i + 1

    maioria = a
    vencedor = 'Vencedor foi o candidato A'

    if b > maioria and b > c:
        vencedor = 'Vencedor foi o candidato B'
    elif c > maioria and c > b:
        vencedor = 'Vencedor foi o candidato C'
    elif c == maioria == b:
        vencedor = 'Empate'
    
    print('----------RESULTADO-----------')
    print(f'{a} votos para o Candidato A')
    print(f'{b} votos para o Candidato B')
    print(f'{c} votos para o Candidato C')
    print(f'{nulos} Nulos')
    print(f'{brancos} Brancos')
    print(vencedor)
    

def main():
    e = int(input('Digite o numero de eleitores: '))
    eleicao(e)


main() 