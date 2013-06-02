def area(x1, y1, x2, y2):
    xdiff = x2 - x1
    ydiff = y2 - y1
    area = xdiff * ydiff
    return area

if __name__ == "__main__":
    print area(2,2,4,4)
