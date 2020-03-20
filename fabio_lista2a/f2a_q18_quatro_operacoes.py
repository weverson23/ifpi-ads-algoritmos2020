# recebe dois valores e de acordo e retorna uma das quatro operações fundamentais
def quatro_op(a,b,c):
    if a == 1:
        return b + c
    elif a == 2:
        return b - c
    elif a == 3:
        return b * c
    elif a == 4:
        return b / c
    else:
        return False


def main():
    print('Digite dois valores e depois escolha uma das operações/n1-Adição  2-Subtração  3-Multiplicação  4-Divisão:/n')
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    op = int(input('Opção:  '))

    q = quatro_op(op,n1,n2)

    if q == False:
        print('Opção inválida!')
    else:   
        print(q)

        
main()