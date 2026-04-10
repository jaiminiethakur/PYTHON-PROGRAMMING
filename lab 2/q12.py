def check_point_circle(cx, cy, radius, px, py):
    distance_squared = (px - cx) ** 2 + (py - cy) ** 2
    radius_squared = radius ** 2
    
    if distance_squared < radius_squared:
        print("Inside the circle")
    elif distance_squared == radius_squared:
        print("On the circle")
    else:
        print("Outside the circle")