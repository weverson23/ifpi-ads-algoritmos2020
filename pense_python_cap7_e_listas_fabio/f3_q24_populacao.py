def censo(h):
    i = 0
    total_hab = h
    sal_total = 0
    filhos_total = 0
    sal_ate_mil = 0
    while i < h:
        print(f'habitante Nº {i + 1}')
        s = float(input('Salário: '))
        f = int(input('Número de filhos: '))
        sal_total = sal_total + s
        filhos_total = filhos_total + f
        if s <= 1000:
            sal_ate_mil = sal_ate_mil + s
        i = i + 1
    media_sal = sal_total / total_hab
    media_filhos = filhos_total / total_hab
    media_ate_mil = sal_ate_mil / total_hab

    print(f'Média do salário da população: {media_sal} R$')
    print(f'Média de número de filhos: {media_filhos}')
    print(f'Percentual de pessoas com salário maior que 1000 R$: {media_ate_mil:.2f} %')
    



def main():
    h = int(input('Digite o numero de habitantes: '))
    censo(h)


main() 