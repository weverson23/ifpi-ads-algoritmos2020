# Lê uma letra e verifique se a letra digitada é vogal ou consoante.
def vogal_cons(a):
    if a == 'a' or a == 'A' or a == 'e' or a == 'E' or a == 'i' or a == 'I' or a == 'o' or a == 'O' or a == 'u' or a == 'U':
        return 'Vogal'
    elif(a == 'b' or a == 'B' or a == 'c' or a == 'C' or a == 'd' or a == 'D' or a == 'f' or a == 'F' or a == 'g' or a == 'G'
        or a == 'h' or a == 'H' or a == 'j' or a == 'J' or a == 'k' or a == 'K' or a == 'l' or a == 'L' or a == 'm' or a == 'M'
        or a == 'n' or a == 'N' or a == 'p' or a == 'P' or a == 'q' or a == 'Q' or a == 'r' or a == 'R' or a == 's' or a == 'S'
        or a == 't' or a == 'T' or a == 'u' or a == 'U' or a == 'v' or a == 'V' or a == 'w' or a == 'W' or a == 'x' or a == 'X'
        or a == 'y' or a == 'Y' or a == 'z' or a == 'Z'):
        return 'Consoante'
    else:
        return 'Não faz parte do alfabeto'


def main():
    letra = input('Digite uma letra: ')
    print(vogal_cons(letra))


main()
