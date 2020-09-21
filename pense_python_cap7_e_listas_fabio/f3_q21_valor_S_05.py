def soma_5():
    num = 1
    den = 1
    s = 0

    while den <= 50:
        s = s + (num/den)
        num = num + 2
        den = den + 1
    
    print (s)




def main():
    soma_5()


main()
