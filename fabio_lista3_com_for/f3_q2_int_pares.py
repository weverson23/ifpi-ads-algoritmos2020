def numero_int_par(a):
    for i in range(1,a+1):
        if i % 2 == 0:
            print(i)
    

def main():
    n = int(input('Digite um número inteiro: '))
    numero_int_par(n)


main()