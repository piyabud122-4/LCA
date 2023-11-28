if __name__ == '__main__':
    capacity = float(input("Battery capacity (Wh):"))
    power_idle = float(input("average power (idle, mW):"))
    power_norm = float(input("average power (normal, mW):"))
    d_idle = capacity/(power_idle/1000)
    d_norm = capacity/(power_norm/1000)

    print('The battery will last %.0f hrs in idle mode.'%d_idle)
    print('The battery will last %.1f hrs in normal mode.'%d_norm)