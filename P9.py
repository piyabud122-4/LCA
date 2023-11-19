if __name__ == '__main__':
    capacity = float(input("Battery capacity (mAh):"))
    Wh = (capacity/1000)*12

    print('At its 12 V rating, it stores %.2f Wh.'%Wh)