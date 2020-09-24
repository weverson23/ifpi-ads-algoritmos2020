def prog_geom(a,l,r):
    aux = a
    for i in range(a,l):
        if aux < l:
            print(aux)
        aux = aux * r
    

def main():
    a = int(input('Digite o valor inicial da P.G: '))
    l = int(input('Digite o limite: '))
    r = int(input('Digite a razão: '))
    
    prog_geom(a,l,r)


main()