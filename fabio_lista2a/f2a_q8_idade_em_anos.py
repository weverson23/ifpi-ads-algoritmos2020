# Lê a data atual e a de nascimento e retorna a idade em anos
def data_atual(d,m,a):
    total_dias = d + (m * 30) + (a * 365)
    anos = total_dias // 365
    return anos


def idade_anos(d,m,a):
    total_dias = d + (m * 30) + (a * 365)
    anos = total_dias // 365
    return anos
    

def main():
    print('Digite a data de nascimento: ')
    d = int(input('Dia: '))
    m = int(input('Mês: '))
    a = int(input('Ano: '))
    print('-----------------------------------')
    print('Digite a data atual: ')
    d2 = int(input('Dia: '))
    m2 = int(input('Mês: '))
    a2 = int(input('Ano: '))
    data_atual(d2,m2,a2)
    print(data_atual(d2,m2,a2) - idade_anos(d,m,a))

main()