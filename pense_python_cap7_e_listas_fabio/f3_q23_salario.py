def salario(x):
    iden = 0
    cont = 1
    bruto = 0
    liquido = 0
    while cont <= x:
        iden = int(input('Código do funcionário: '))
        horas = int(input('Horas trabalhadas: '))
        depen = int(input('Numero de dependentes: '))
        bruto = horas * 12 + (depen * 40)
        inss = bruto * 8.5/100
        ir = bruto * 5/100
        liquido = bruto - ir - inss
        print('Contra Cheque')
        print('------------------------------')
        print(f'Funcionário {iden}')
        print('------------------------------')
        print(f'Bruto --------- {bruto} R$')
        print(f'INSS -------- {inss} R$')
        print(f'IR -------- {ir} R$')
        print(f'Líquido-------- {liquido} R$')
        print('------------------------------')
        cont = cont + 1




def main():
    n = int(input('digite a quantidade de funcionários: '))
    salario(n)


main()