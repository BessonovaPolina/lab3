class Shape:
    def __init__(self, radius: int, side: int, sidee: int, tside: int, tsidee: int, height: int):
        self.radius = radius
        self.side = side
        self.sidee = sidee
        self.tside = tside
        self.tsidee = tsidee
        self.height = height
    
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius: int,side: int, sidee: int, tside: int, tsidee: int, height: int):
        super().__init__( radius, side, sidee, tside, tsidee, height)
    def area(self):
        return 3.14 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.14 * self.radius
        
class Rectangle(Shape):
    def __init__(self, radius: int,side: int, sidee: int, tside: int, tsidee: int, height: int):
        super().__init__( radius, side, sidee, tside, tsidee, height)      
    def area(self):
        return self.side * self.sidee
    def perimeter(self):
        return self.side*2 + self.side*2
        
class Triangle(Shape):
    def __init__(self, radius: int,side: int, sidee: int, tside: int, tsidee: int, height: int):
        super().__init__( radius, side, sidee, tside, tsidee, height)      
    def area(self):
        return (1/2) * self.tside * self.height
    def perimeter(self):
        return 2*self.tsidee + self.tside 
        
circle = Circle(5, 0, 0, 0, 0, 0)
rectangle = Rectangle(0, 3, 4, 0, 0, 0)
triangle = Triangle (0, 0, 0, 3, 4, 5)

print("Площадь круга:", circle.area())
print("Периметр круга:", circle.perimeter())
print("Площадь круга:", rectangle.area())
print("Периметр круга:", rectangle.perimeter())
print("Площадь круга:", triangle.area())
print("Периметр круга:", triangle.perimeter())