def prog_arit(a,l,r):
    aux = a
    for i in range(a,l):
        if aux < l:
            print(aux)
        aux = aux + r
    

def main():
    a = int(input('Digite o valor inicial da P.A: '))
    l = int(input('Digite o limite: '))
    r = int(input('Digite a razão: '))
    
    prog_arit(a,l,r)


main()