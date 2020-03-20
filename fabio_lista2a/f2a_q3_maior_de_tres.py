# programa recebe 3 valores   

def maior_de_tres(a,b,c):
    maior = 0
    if(a >= b) and (a >= c):
        maior = a
    elif(b >= a) and (b >= c):
        maior = b
    elif(c >= a) and (c >= b):
        maior = c
    return maior


def main():
    a = float(input('Digite o primeiro valor: ')) 
    b = float(input('Digite o segundo valor: '))
    c = float(input('Digite o terceiro valor: '))
    maior = maior_de_tres(a,b,c)
    print(f"O maior valor é: {maior}")


main()
    
