def main():
    # entrada
    entrada = input().split()
    hora_inicio = int(entrada[0])
    hora_fim = int(entrada[1])

    # processamento
    if hora_inicio == hora_fim:
        tempo = 24
    elif hora_fim > hora_inicio:
        tempo = hora_fim - hora_inicio
    else:
        tempo = (24 - hora_inicio) + hora_fim - 0

    # saída
    print('O JOGO DUROU {} HORA(S)'.format(tempo))


main()