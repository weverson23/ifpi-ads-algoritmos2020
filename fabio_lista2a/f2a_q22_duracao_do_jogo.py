# Recebe as entradas e hora e min do inicio e fim do jogo e retorna o tempo total de jogo
def tempo_jogo(a,b,c,d):
    if a == 0:
        a = 24 
        min_total1 = (a * 60) + b
    else:
        min_total1 = (a * 60) + b
    
    if c == 0:
        c = 24
        min_total2 = (c * 60) + d
    else:
        min_total2 = (c * 60) + d
    
    tempo_somado = min_total2 - min_total1
    tempo_hora = tempo_somado // 60
    tempo_min = tempo_somado % 60

    if tempo_hora >= 24 and tempo_min > 0:
        print('Jogo ultrapassou o tempo permitido')
    else:
        print(f'O jogo durou {tempo_hora} horas e {tempo_min} minutos')


def main():
    h1 = int(input('Digite a hora inicial: '))
    m1 = int(input('Digite a minuto inicial: '))
    print('-----------------------------------------------')
    h2 = int(input('Digite a hora final: '))
    m2 = int(input('Digite o minuto final: '))

    tempo_jogo(h1,m1,h2,m2)


main()

    