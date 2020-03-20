# Lê uma senha de 4 números diz se é ou não válida
def valida_senha(a):
    m = a // 1000
    c = (a % 1000) // 100
    d = ((a % 1000) % 100) // 10
    u = ((a % 1000) % 100) % 10
    if m == 1 and c == 2 and d == 3 and u == 4:
        return True
    else:
        return False


def main():
    senha = int(input('Digite uma senha de 4 números: '))
    v = valida_senha(senha)
    if v == True:
        print('Senha válida!')
    else:
        print('Senha incorreta!')


main()