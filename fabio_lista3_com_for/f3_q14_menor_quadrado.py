def maior_menor_qua(a):
    x = int(a ** (1/2)) * int(a ** (1/2))
    return x
    

def main():
    n = int(input('Digite o valor de N: '))
    q = maior_menor_qua(n)
    print(q)


main()

