from rectangle import Rectangle

width = float(input("Width: "))
height = float(input("Height: "))

rec = Rectangle(width, height)

print(rec.__str__())
