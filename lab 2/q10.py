def compare_area_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    
    if area > perimeter:
        print("Area is greater than perimeter")
    else:
        print("Area is not greater than perimeter")