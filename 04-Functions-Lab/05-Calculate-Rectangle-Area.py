def rectangle_area(a: float, b: float):
    area = None
    area = a * b

    if area is not None:
        return int(area)

a = float(input())
b = float(input())

print(rectangle_area(a, b))