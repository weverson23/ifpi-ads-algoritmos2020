def progre_arit(a,b,c):
    while (a <= b):
        print(a)
        a = a + c

    
def main():
    i = int(input('Digite o valor inicial:  '))
    l = int(input('Digite o limite:  '))
    r = int(input('Digite a razão:  '))
    progre_arit(i,l,r)


main()