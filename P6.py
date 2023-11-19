a = float(input("a: "))
b = float(input("b: "))
if a == 0 and b == 0:
    print("a/b = Not definded")
elif a != 0 and b == 0 :
    if a > 0 :
        print("a/b = Infinity")
    elif a < 0 :
        print("a/b = Negative Infinity")
else :
    r = a/b
    print("a/b =",r)

