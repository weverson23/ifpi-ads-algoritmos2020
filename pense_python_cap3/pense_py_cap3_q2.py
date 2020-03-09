def do_twice(fun, valor):
    fun(valor)
    fun(valor)

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_four(fun, valor):
    do_twice(fun, valor)
    do_twice(fun, valor)

do_twice(print,'spam')

do_four(print,'spam')
