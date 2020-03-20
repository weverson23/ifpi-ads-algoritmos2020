# Lê duas notas e pela media exibe se o aluno foi aprovado ou não.
# Caso não seja aprovado e tenha nota maior ou igual a 5 o aluno será aprovado por exame final
def notas(a,b):
    media = (a + b)/2
    return media


def exame_final(a,b):
    media = (a + b) / 2
    if media >= 5:
        return '\nAprovado'
    else:
        return '\nReprovado'


def main():
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    m = notas(n1,n2)
    if m >= 7:
        print('Aprovado')
    elif m >= 5:
        print('Aluno de exame final')
        exame = float(input('\nNota do exame final: '))
        print(exame_final(exame,m))
    else:
        print('Reprovado')


main()