# Faz uma séria de perguntas e retorna a situação do interrogado
def interroga(a,b,c,d,e):
    s = a + b + c + d + e
    if a != 1 and  a != 0 and b != 1 and b != 0 and c != 1 and c != 0 and d != 1 and d != 0 and e != 1 and e != 0:
        return 'número inválido' 
    elif s == 2:
        return 'Suspeito'
    elif s == 3 or s == 4:
        return 'Cúmplice'
    elif s == 5:
        return 'Assassino'
    else:
        return 'Inocente'


def main():
    print('Responda a série de perguntas sobre um crime./nTecle 1 - Sim      0 - Não')
    a = int(input('Telefonou para a vítima ?  '))
    b = int(input('Esteve no local do crime ?  '))
    c = int(input('Mora perto da vítima ?  '))
    d = int(input('Devia para a vítima ?  '))
    e = int(input('Já trabalhou com a vítima ?   '))
    print(interroga(a,b,c,d,e))


main()

