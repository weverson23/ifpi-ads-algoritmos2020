# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo 
# usuário e gere um cupom fiscal, contendo as informações da compra
def mercado(c,q,p):
    tipo_carne = 0
    tipo_pag = 0
    desconto = 0
    total = 0
    total_final = 0
    if c == 'F' or c == 'f':
        if q > 5:
            total = q * 5.80
            tipo_carne = 'Filé'
        else:
            total = q * 4.90
            tipo_carne = 'Filé'
    elif c == 'A' or c == 'a':
        if q > 5:
            total = q * 6.80
            tipo_carne = 'Alcatra'
        else:
            total = q * 5.90
            tipo_carne = 'Alcatra'
    elif c == 'P' or c == 'p':
        if q > 5:
            total = q * 7.80
            tipo_carne = 'Picanha'
        else:
            total = q * 6.90
            tipo_carne = 'Picanha'
    
    if p == 'C' or p == 'c':
        desconto = total * (5/100)
        total_final = total - desconto
        tipo_pag = 'Cartão'
    elif p == 'D' or p == 'd':
        desconto = 0
        total_final = total
        tipo_pag = 'Dinheiro'
    
    print('----------------------------------------------')
    print(f'Tipo de carne:      {tipo_carne}')
    print(f'Preço total:      R$ {total}')
    print(f'Tipo de pagamento:      {tipo_pag}')
    print(f'Valor do desconto:      R$ {desconto}')
    print(f'Total a pagar:      R$ {total_final}')
    print('----------------------------------------------')


def main():
    print("----------Hipermercado Tabajara---------")
    c = input('Digite o tipo da carne:\nF - Filé    A - Alcatra    P - Picanha:   ')
    q = float(input('Digite a quantidade de quilos(Kg):  '))
    p = input('Digite a forma de pagamento:\nC - Cartão     D - Dinheiro:  ')
    mercado(c,q,p)


main()