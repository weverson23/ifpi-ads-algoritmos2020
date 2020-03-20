# recebe 3 valores e retonar o valor correspondente a opção escolhida. 
def opcao(o,a,b,c):
    if o == 1:
        return a
    elif o == 2:
        return b
    elif o == 3:
        return c
    else:
        return False



def main():
    o = int(input('Escolha a opção 1, 2 ou 3: '))
    print('-----------------------------------------------')
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    n3 = float(input('Digite o terceiro número: '))

    v = opcao(o,n1,n2,n3)
    if  v != False:
        print(v)
    else:
        print('Opção inválida!')


main()