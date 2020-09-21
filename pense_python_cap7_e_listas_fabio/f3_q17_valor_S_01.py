def soma_1(x):
    n = 1
    s = 0

    while n <= x:
        s = s + ( 1/(n+1))
        n = n + 1
    print(s)




def main():
    n = int(input('Digite o valor de N: '))
    soma_1(n)


main()
