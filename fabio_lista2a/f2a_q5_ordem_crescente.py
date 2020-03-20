# lê três números e os coloca na ordem crescente
def crescente(a,b,c):
    menor = 0
    meio = 0
    maior = 0
    if(a >= b) and (a >= c) and (b >=c):
        maior = a
        meio = b
        menor = c
    elif(a >= b) and (a >= c) and (c >= b):
        maior = a
        meio = c
        menor = b
    elif(b >= a) and (b >= c) and (a >= c):
        maior = b
        meio = a
        menor = c
    elif(b >= a) and (b >= c) and (c >= a):
        maior = b
        meio = c
        menor = a
    elif(c >= a) and (c >= b) and (a >= b):
        maior = c
        meio = a
        menor = b
    elif(c >= a) and (c >= b) and (b >= a):
        maior = c
        meio = b
        menor = a
    return menor, meio, maior
    


def main():
    a = float(input('Digite o primeiro valor: '))
    b = float(input('Digite o segundo valor: '))
    c = float(input('Digite o terceiro valor: '))
    print(crescente(a,b,c))


main()