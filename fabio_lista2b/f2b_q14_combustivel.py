# Lê o a quantidade de litros e o tipo de gasolina e retorna o valor a ser pago
def combustivel(c,l):
    total = 0
    if c == 'a' or c == 'A':
        if l > 20:
            total = l * 1.90 - (1.90 * (5 / 100))
        else:
            total = l * 1.90 - (1.90 * (3 / 100))
    elif c == 'g' or c == 'G':
        if l > 20:
            total = l * 2.50 - (2.50 * (6 / 100))
        else:
            total = l * 2.50 - (2.50 * (4 / 100))
    
    return total


def main():
    c = input('Digite o tipo de combustível\nG - Gasolina      A - Alcool: ')
    l = int(input('Quantidade de litros: '))
    
    print('O preço a pagar é R$',combustivel(c,l))


main()
