def main():
    # entrada
    cod, quant = map(int, input().split())
    
    # processamento
    total = 0
    if cod == 1:
        total = 4.00 * quant
    elif cod == 2:
        total = 4.50 * quant
    elif cod == 3:
        total = 5.00 * quant
    elif cod == 4:
        total = 2.00 * quant
    elif cod == 5:
        total = 1.50 * quant

    # saída
    print('Total: R$ {:.2f}'.format(total))


main()