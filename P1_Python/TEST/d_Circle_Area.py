def calculate_circle_area(radius):
    area = 3.14159 * (radius ** 2)
    return area


radius = float(input("Enter the radius of the circle: "))

if radius >= 0:
    area = calculate_circle_area(radius)
    print(f"The area of the circle with radius {radius} is {area:.2f} meter square")
else:
    print("Radius cannot be negative.")