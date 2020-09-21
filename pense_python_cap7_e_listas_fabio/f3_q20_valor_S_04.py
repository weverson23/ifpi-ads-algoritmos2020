def soma_4(x):
    num = 1
    den = 1
    s = 0

    while den <= x:
        if den % 2 == 0:
            s = s - (num/den)
        else:
            s = s + (num/den)

        den = den + 1
    
    print (s)




def main():
    n = int(input('Digite o valor de N: '))
    soma_4(n)


main()
