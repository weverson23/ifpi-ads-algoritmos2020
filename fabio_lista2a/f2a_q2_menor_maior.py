def maior_menor(a,b):
    maior = 0
    menor = 0
    if (a > b):
        maior = a
        menor = b
        print(f'Maior: {maior} \nMenor: {menor}')
    elif(b > a):
        maior = b
        menor = a
        print(f'Maior: {maior} \nMenor: {menor}')
    else:
        print('Os valores são iguais')


def main():
    n1 = float(input('Digite o primeiro valor: ')) 
    n2 = float(input('Digite o segundo valor: '))
    maior_menor(n1,n2)


main()