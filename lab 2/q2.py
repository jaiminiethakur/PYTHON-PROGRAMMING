def compare_three(a, b, c):
    if a >= b and a >= c:
        print("Largest:", a)
    elif b >= a and b >= c:
        print("Largest:", b)
    else:
        print("Largest:", c)
        
    if a <= b and a <= c:
        print("Smallest:", a)
    elif b <= a and b <= c:
        print("Smallest:", b)
    else:
        print("Smallest:", c)