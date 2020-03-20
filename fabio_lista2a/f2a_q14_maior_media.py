# Lê 5 números, calcula a média e mostra quais são maiores que a média
def media(a,b,c,d,e):
    media = (a + b + c + d + e) / 5
    return media

''' A função compara_maior() recebe o primeiro valor e compara com os 5 próximos e retorna
os maiores que o primeiro valor '''   
def compara_maior(n,a,b,c,d,e):
    if a > n:
        print(a,end=' ')
    if b > n:
        print(b,end=' ')    
    if c > n:
        print(c,end=' ')
    if d > n:
        print(d,end=' ')
    if e > n:
        print(e)


def main():
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    n3 = int(input('Digite o terceiro número: '))
    n4 = int(input('Digite o quarto número: '))
    n5 = int(input('Digite o quinto número: '))

    v = media(n1,n2,n3,n4,n5)
    compara_maior(v,n1,n2,n3,n4,n5)


main()
