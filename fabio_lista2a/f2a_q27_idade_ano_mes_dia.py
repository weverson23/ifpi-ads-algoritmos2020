# Retorna a idade atual pela data de nascimento
def data_total(d1,m1,a1,d2,m2,a2):
    total_dias_atual = d1 + (m1 * 30) + (a1 * 365)
    total_dias_nasc = d2 + (m2 * 30) + (a2 * 365)
    total_dias = total_dias_atual - total_dias_nasc

    a3 = total_dias // 365
    m3 = (total_dias % 365) // 12
    d3 = (total_dias % 365) % 12

    print(f'ano: {a3}\nmes: {m3}\ndia: {d3}')


def main():
    print('Data atual')
    d1 = int(input('Dia: '))
    m1 = int(input('Mês: '))
    a1 = int(input('Ano: '))
    print('--------------------------------------')
    print('Data Nascimento')
    d2 = int(input('Dia: '))
    m2 = int(input('Mês: '))
    a2 = int(input('Ano: '))

    data_total(d1,m1,a1,d2,m2,a2)


main()