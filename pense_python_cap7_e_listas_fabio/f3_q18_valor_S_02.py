def soma_2(x):
    n = x
    s = 0
    a = 1
    if x == 0:
        print('Denominador não pode ser "zero" ')
    else:
        while a <= x:
            s = s + (a/n)
            a = a + 1
            n = n - 1
            print(s)



def main():
    n = int(input('Digite o valor de N: '))
    soma_2(n)


main()
