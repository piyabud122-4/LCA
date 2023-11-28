if __name__ == '__main__':
    energy = float(input("Energy( in kcal):"))
    J = energy*4184
    Wh = J/3600

    print("That is {:.2f} J or {:.2f} Wh.".format(J, Wh))