#Leia um número e escreva se o número é inteiro ou decimal
def int_dec(a):
    aux = int(a)
    
    if a == aux:
        return 'O valor é inteiro'
    else:
        return 'O valor é decimal'


def main():
    n = float(input('Digite um valor: '))
    print(int_dec(n))


main()