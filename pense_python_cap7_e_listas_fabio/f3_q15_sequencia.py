def sequencia(x):
    a = 1
    b = 1
    c = 2
    while a <= x:
        print(b)
        a = a + 1
        b = b + c
        c = c + 1 


    
def main():
    n = int(input('Digite o a quantidade de termos da sequência: '))
    sequencia(n)


main()