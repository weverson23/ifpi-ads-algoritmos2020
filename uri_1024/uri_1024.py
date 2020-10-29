def inverter(s):
    if len(s) == 1:
        return s
    elif len(s) > 1:
        return inverter(s[1:]) + s[0]


def cifra1(c):
    aux1 = 0
    aux2 = 0
    aux3 = []
    aux4 = 0
    for letra in c: 
        aux1 = (ord(letra))
        if (65 <= aux1 <= 90) or (97 <= aux1 <= 122):
            aux1 = aux1 + 3 
        aux2 = chr(aux1)
        aux3.append(aux2)
    aux4 = ''.join(aux3)
    return aux4


def cifra2(c):
    frase = c
    frase2 = []
    for letra in frase:
        frase2.append(ord(letra))
    tam = len(frase2)
    meta = tam // 2
    i = 0
    #print(frase2)

    for i in range(tam):
        if i >= meta:
            frase2[i] = frase2[i] - 1

    #print(frase2)
    for i in range(tam):
        frase2[i] = chr(frase2[i])

    return ''.join(frase2)
        

def main():
    n = int(input())
    for i in range(n):
        frase = input()
        lista = []
        aux1 = cifra1(frase)
        lista = inverter(aux1)
        aux2 = cifra2(lista)
        print(aux2)


main()