# recebe o salário e retorna salário rejustado e as especificações do ajuste
def reajuste(a):
    aumento = 0
    novo_salario = 0
    percen = 0
    if a <= 280:
        percen = 20
        aumento = a * (percen/100)
        novo_salario = a + aumento
    elif a > 280 and a <= 700:
        percen = 15
        aumento = a * (percen/100)
        novo_salario = a + aumento
    elif a > 700 and a <= 1500:
        percen = 10
        aumento = a * (percen/100)
        novo_salario = a + aumento
    else:
        percen = 5
        aumento = a * (percen/100)
        novo_salario = a + aumento
    
    print(f'O salário antes do reajuste: R$ {a}')
    print(f'O percentual de aumento aplicado: {percen}%')
    print(f'O valor do aumento: R$ {aumento}')
    print(f'O novo salário: R$ {novo_salario}')


def main():
    s = float(input('Digite o valor do salário: '))
    reajuste(s)


main()
    