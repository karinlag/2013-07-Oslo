def area(point1, point2):
    xdiff = point2[0] - point1[0]
    ydiff = point2[1] - point1[1]
    area = xdiff * ydiff
    return area

if __name__ == "__main__":
    firstpoint = [2,2]
    secondpoint = [4,4]
    print area(firstpoint, secondpoint)
