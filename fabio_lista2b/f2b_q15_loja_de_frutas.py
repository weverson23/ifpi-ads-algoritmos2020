# Lê o a quantidade de quilos que o cliente quer em frutas e retonar o valor total
def frutas(a,b):
    moran = 0
    maca = 0
    total = 0
    total_final = 0
    if a > 5:
        moran = 2.20 * a
    else:
        moran = 2.50 * a
    
    if b > 5:
        maca = 1.50 * b
    else:
        maca = 1.80 * b

    total = moran + maca
    
    if a + b > 8 or total > 25:
        total_final = total - (total * 10/100)
    else:
        total_final = total

    return total_final


def main():
    m1 = float(input('Digite o quantidade de quilos de morango: '))
    m2 = float(input('Digite o quantidade de quilos de maça: '))
    
    print('O valor total a pagar é R$',frutas(m1,m2))


main()

