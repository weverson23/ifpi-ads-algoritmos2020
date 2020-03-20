def num_iguais(a,b,c):
    if a == b and a == c:
        return 3
    elif (a == b and a != c) or (b == c and b != a) or (c == a and c != b):
        return 2
    else:
        return 0 



def main():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    v = num_iguais(a,b,c)
    if v == 3:
        print('3 iguais')
    elif v == 2:
        print('2 iguais')
    else:
        print('Nenhum numero igual')


main()

