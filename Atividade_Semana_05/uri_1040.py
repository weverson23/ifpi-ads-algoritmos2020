def main():
    # entrada
    n1,n2,n3,n4 = map(float, input().split())
    
    # processamento e saída
    media = (n1*2 + n2*3 + n3*4 + n4*1) / 10
    exame = 0
    media_final = 0

    if media >= 7:
        print('Media: {:.1f}'.format(media))
        print('Aluno aprovado.')
    elif media < 5:
        print('Media: {:.1f}'.format(media))
        print('Aluno reprovado.')
    else:
        print('Media: {:.1f}'.format(media))
        print('Aluno em exame.')
        exame = float(input())
        media_final = (media + exame) / 2
        if media_final < 5:
            print('Nota do exame: {:.1f}'.format(exame))
            print('Aluno reprovado.')
            print('Media final: {:.1f}'.format(media_final))
        else:
            print('Nota do exame: {:.1f}'.format(exame))
            print('Aluno aprovado.')
            print('Media final: {:.1f}'.format(media_final))


main()