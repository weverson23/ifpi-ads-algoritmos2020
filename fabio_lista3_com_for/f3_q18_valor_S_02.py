def soma_2(x):
    n = x
    s = 0
    if x == 0:
        print('Denominador não pode ser "zero" ')
    else:
        for i in range(1,x+1):
            s = s + (i/n)
            n = n - 1
        print(s)



def main():
    n = int(input('Digite o valor de N: '))
    soma_2(n)


main()
