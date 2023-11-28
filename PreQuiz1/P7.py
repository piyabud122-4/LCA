import math
def rec_to_pol(r,c):
    polar = math.sqrt(r**2+c**2)
    degree = math.degrees(math.atan2(c,r))
    if r<0 and c<0 :
        degree+=360
    return polar,degree

if __name__ == '__main__':
    r, c = input('Enter (x y):').split()
    m, a = rec_to_pol(float(r), float(c))
    print("polar: {:.2f} with {:.2f} degree".format(m, a))