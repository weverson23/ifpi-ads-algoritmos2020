# de acordo com valor do resto retorna o resultado de diferentes expressões
def expressoes(a,b):
    if a % b == 1:
        print('A soma dos dois valores com o resto é:\n',a + b + (a % b))
    elif a % b == 2:
        if a % 2 == 0:
            print('O primeiro valor é par')
        else:
            print('O primeiro valor é impar')
        if b % 2 == 0:
            print('O segundo valor é par')
        else:
            print('O segundo valor é impar')
    elif a % b == 3:
        print('A soma dos valores multiplicados pelo primeiro valor é:\n',(a + b) * a)
    elif a % b == 4:
        print('A soma dos valores divididos pelo segundo é:\n',(a + b) / b)
    else:
        print('Quadrado do primeiro valor: ',a ** 2)
        print('Quadrado do segundo valor: ',b ** 2)


def main():
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))

    expressoes(n1,n2)


main()

