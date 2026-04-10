def check_collinear(x1, y1, x2, y2, x3, y3):
    slope1 = (y2 - y1) * (x3 - x2)
    slope2 = (y3 - y2) * (x2 - x1)
    
    if slope1 == slope2:
        print("Points fall on one straight line")
    else:
        print("Points do not fall on one straight line")