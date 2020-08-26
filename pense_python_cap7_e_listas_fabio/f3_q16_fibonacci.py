def fibonacci(x):
    a = 1
    ant1 = 1
    ant2 = 1
    prox = 0
    print(0)
    print(1)
    print(1)
    while a <= x:
        prox = ant1 + ant2
        print(prox)
        a = a + 1
        ant1 = ant2
        ant2 = prox 


    
def main():
    n = int(input('Digite o a quantidade de termos da sequência: '))
    fibonacci(n)


main()