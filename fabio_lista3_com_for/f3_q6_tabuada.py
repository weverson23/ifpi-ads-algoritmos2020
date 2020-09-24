def tabuada():
    c = 1
    for i in range(1,11):
        for j in range(1,11):
            print(f'{c} x {j} = {j*c}')
        c = c + 1


def main():
    tabuada()


main()    