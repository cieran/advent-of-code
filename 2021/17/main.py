INPUT = (207, 263, -115, -63)

def sim(x_min, x_max, y_min, y_max, x, y):
    x3, y3 = 0,0
    mh = 0
    while y3 > y_min:
        x3 += x
        y3 += y
        x -= 1 if x > 0 else 0
        y -= 1
        mh = max(y3, mh)
        if (x_min <= x3 <= x_max) and (y_min <= y3 <= y_max):
            return mh
    return -1


if __name__ == "__main__":

    x_min, x_max, y_min, y_max = INPUT
    mh, c = -1, 0
    for x in range(x_max+1):
        for y in range(y_min, 115):
            h = sim(x_min, x_max, y_min, y_max, x, y)
            mh = max(mh, h)
            if h != -1:
                c += 1

    print(mh)
    print(c)
