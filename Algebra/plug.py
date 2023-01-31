#using brute force
def plug():
    x = -100
    while x < 100:
        if x*2 + 5 == 13:
            print("x = ", x)
        x += 1

plug()