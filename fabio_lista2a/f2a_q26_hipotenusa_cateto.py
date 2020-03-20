# Recebe 3 lados e identifica a hipotenusa e seus catetos
def hipo_cat(a,b,c):
    hip = 0
    cat1 = 0
    cat2 = 0
    if a > b and a > c:
        hip = a
        cat1 = b
        cat2 = c
    elif b > a and b > c:
        hip = b
        cat1 = a
        cat2 = c
    else:
        hip = c
        cat1 = a
        cat2 = b

    print(f'A hipotenusa é {hip} e os catetos são {cat1} e {cat2}')


def main():
    a = float(input('Digite o primeiro lado: '))
    b = float(input('Digite o segundo lado: '))
    c = float(input('Digite o terceiro lado: '))

    hipo_cat(a,b,c)


main()
