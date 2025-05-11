from Shapes import Circle, Rectangle, Square, Triangle

def main():
    print("Welcome to the Geometric Shapes !")
    print("Please select one of the following shapes!")
    print("1.Circle.\n 2.Rectangle.\n 3.Square.\n 4.Triangle. ")

    The_choice = input("Enter the number based on the shape you had choosen.")
    
    try:
        
        if The_choice == '1':
            radius = float(input("Enter the radius of the circle:"))
            shape = Circle(radius)
        elif The_choice == '2':
            length = float(input("Enter the length of the rectangle : "))
            width = float(input("Enter the width of the rectangle : "))    
            shape = Rectangle(length, width)
        elif The_choice == '3':
            side = float(input("Enter the side length of the square: "))
            shape = Square(side)
        elif The_choice == '4':
            side1 = float(input("Enter the length of side 1 of the triangle: "))
            side2 = float(input("Enter the length of side 2 of the triangle: "))
            side3 = float(input("Enter the length of side 3 of the triangle: "))
            shape = Triangle(side1, side2, side3)
        else :
            print("Invalid Input.Select valid option!")
            return
        print("\n" + str(shape))
        print(f"Area: {shape.area():.2f}")
        print(f"Perimeter: {shape.perimeter():.2f}")
        
    except ValueError as e:
        
        print(f"Error: {e}")
        


if __name__ == "__main__":
    main()