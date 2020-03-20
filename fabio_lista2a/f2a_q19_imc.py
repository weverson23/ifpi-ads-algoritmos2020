# Através do peso e altura calcula o IMC
def imc(p,a):
    m = p /(a ** 2)
    return m


def main():
    p = float(input('Digite o peso: '))
    a = float(input('Digite a altura: '))

    m = imc(p,a)
    if m < 25:
        print(f'O imc é {m}\nSituação: Normal')
    elif m >= 25 and m <= 30:
        print(f'O imc é {m}\nSituação: Obeso')
    else:
        print(f'O imc é {m}\nSituação: Obesidade mórbida')

    
main()