def main():
    # entrada
    ced = int(input())
    
    # processamento
    cem = ced // 100
    cinquenta = (ced % 100) // 50
    vinte = ((ced % 100) % 50) // 20
    dez = (((ced % 100) % 50) % 20) // 10
    cinco = ((((ced % 100) % 50) % 20) % 10) // 5
    dois = (((((ced % 100) % 50) % 20) % 10) % 5) // 2
    um = (((((ced % 100) % 50) % 20) % 10) % 5) % 2

    # saída
    print(ced)
    print('{} nota(s) de R$ 100,00'.format(cem))
    print('{} nota(s) de R$ 50,00'.format(cinquenta))
    print('{} nota(s) de R$ 20,00'.format(vinte))
    print('{} nota(s) de R$ 10,00'.format(dez))
    print('{} nota(s) de R$ 5,00'.format(cinco))
    print('{} nota(s) de R$ 2,00'.format(dois))
    print('{} nota(s) de R$ 1,00'.format(um))


main()