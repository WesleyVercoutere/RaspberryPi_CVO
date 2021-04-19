'''< ClassName >.< method_name > (self, < args >)
or
super(). < method_name > (< args >)
'''


class Triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def find_area(self):
        print((self.base * self.height) / 2)


class RightTriangle(Triangle):

    def display_area(self):
        print("=== Right Triangle Area ===")
        # This line calls the method from the Triangle class
        Triangle.find_area(self)  # You could also use super().find_area()


print("1", dir(RightTriangle))


right_triangle = RightTriangle(5, 6)
right_triangle.display_area()
right_triangle.find_area()
