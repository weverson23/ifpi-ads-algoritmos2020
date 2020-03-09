def dupla_funcao(f):
    f()
    f()

def linha():
    print('+ - - - -', end=' ')


def linha2():
    dupla_funcao(linha)
    print('+')


def coluna():
    print('|        ', end=' ')


def coluna2():
    dupla_funcao(coluna)
    print('|')


def quatro(f):
    dupla_funcao(f)
    dupla_funcao(f)


def linha3():
    linha2()
    quatro(coluna2)

def grade():
    dupla_funcao(linha3)
    linha2()


def linha_final():
    quatro(linha)
    print('+')


def coluna_final():
    quatro(coluna)
    print('|')

def grade_maior1():
    linha_final()
    quatro(coluna_final)


def grade_maior_final():
    quatro(grade_maior1)
    linha_final()


grade_maior_final()

