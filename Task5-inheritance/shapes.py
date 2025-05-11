import math 

class Shape:
    """
    Base class for geometric shapes.
    """

    def area(self):
        """
        Calculate the area of the shape .
        It will be used with the subclasses.
        """
        raise NotImplementedError("Subclasses must implement this menthod.")
    
    def perimeter(self):
        """
        Calculate the perimeter of the shape.
        It will be used with the subclasses.
        
        """
    def __str__(self):
        """
        Return a string representation of the shape .
        """    
        return "This is a generic shape."
class Circle(Shape):
    """
    Circle shape with a given radius.
    """    
    def __init__(self, radius):
        if radius<= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.
        """    
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """
        Calculate the perimeter / circumference of the circle. 
        """
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return f"Circle with radius {self.radius}"
    
class Rectangle(Shape):
    """
    Rectangle shape with a given length and width.
    """
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and Width must be a positive number.")
        self.length = length
        self.width = width

    def area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.width * self.length

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        """
        return 2 * (self.width + self.length)
                    
    def __str__(self):
        return f"Rectangle with length {self.length} and width {self.width}."

class Square (Rectangle):
    """
    Square shape with equal sides.
    Inherits from the Rectangle class.
    """

    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side length must be positive.")
        Rectangle.__init__(self, side, side)

    def __str__(self):
        return f"Square with side length {self.length}."

class Triangle(Shape):
    """
    Triangle shape with 3 sides.
    """

    def __init__(self, side1, side2, side3):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("All sides must be positive.")
        # Check for triangle inequality

        if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
            raise ValueError("The given sides do not form valid triangle.")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        """
        Calculate the area of the triangle using 
        """
        s = self.perimeter() / 2 

        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s -self.side3))
    
    def perimeter(self):
        """
        Calculate the perimeter of the triangle.
        """
        return self.side1 + self.side2 + self.side3
    def __str__(self):
        return f"Triangle with sides {self.side1}, {self.side2}, {self.side3}"