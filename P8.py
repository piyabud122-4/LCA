import math 
if __name__ == '__main__':
    N = int(input('Number of values:'))
    ss = 0
    for i in range(N):
        value = float(input("value:"))
        ss += value**2
    rms = math.sqrt(ss/N)
    print('RMS = {:,.2f}'.format(rms))