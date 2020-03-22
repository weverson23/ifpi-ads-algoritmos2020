# Lê a quantidade de horas e o valor da hora e retorna a folha de pagamento
def folha_pag(h,v):
    sal_bruto = h * v
    porc_ir = 0
    ir = 0
    inss = sal_bruto * (10 / 100)
    fgts = sal_bruto * (11 / 100)
    total_des = 0
    sal_liq = 0
    if sal_bruto <= 900:
        ir = 0
        total_des = ir + inss
        sal_liq = sal_bruto - total_des
    elif sal_bruto <= 1500:
        porc_ir = 5
        ir = sal_bruto * (porc_ir / 100)
        total_des = ir + inss
        sal_liq = sal_bruto - total_des
    elif sal_bruto <= 2500:
        porc_ir = 10
        ir = sal_bruto * (porc_ir / 100)
        total_des = ir + inss
        sal_liq = sal_bruto - total_des
    else:
        porc_ir = 20
        ir = sal_bruto * (porc_ir / 100)
        total_des = ir + inss
        sal_liq = sal_bruto - total_des

    print('-----------------------------------------------------------')
    print(f'Salário Bruto ({v} * {h})     : R$ {sal_bruto}')
    print(f'(-) IR({porc_ir})          : R$ {ir}')
    print(f'(-) INSS(10%)          : R$ {inss}')
    print(f'FGTS(11%)          : R$ {fgts}')
    print(f'Total de descontos          : R$ {total_des}')
    print(f'Salário líquido          : R$ {sal_liq}')
    print('------------------------------------------------------------')



def main():
    print('Digite a quantidade de horas e o valor da hora ')
    h = int(input('Horas: '))
    v = float(input('Valor: '))
    folha_pag(h,v)


main()
