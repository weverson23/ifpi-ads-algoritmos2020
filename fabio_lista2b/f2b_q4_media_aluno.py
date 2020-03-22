# Lê duas notas, faz a média e retorna se foi aprovado ou não
def media(a,b):
    m = (a + b) / 2
    return m


def main():
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))

    m = media(n1,n2)
    
    if m > 10 or m < 0:
        print('Fora do escopo')
    elif m == 10:
        print('Aprovado com distinção')
    elif m >= 7 and m < 10:
        print('Aprovado')
    elif m < 7:
        print('Reprovado')


main()