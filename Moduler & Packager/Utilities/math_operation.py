import math


def math_menu():

    while True:
        print("""
          Mathematical Operation

1. Calculate Factorial
2. Solve Compound Interest
3. Trigonometric Calculations
4. Area of Geometric Shapes
5. Back to Main Menu
""")
        inner_user = int(input("Enter your Choice: "))
        
        if inner_user == 1:
            num = int(input("Enter a number to calculate Factorial: "))
            print(f"Factorial: {math.factorial(num)}")
        
        elif inner_user == 2:
            per = int(input("Enter Principal Amount: "))
            rate = int(input("Enter rate of interest: "))
            time = int(input("Enter Time (in years): "))
            com = per * math.pow(1+rate/100,time)-per
            print(f"Compound Interest Is : {round(com,2)}")
        
        elif inner_user == 3:
            angle = float(input("Enter a Value: "))
        
            print("Sin",math.sin(math.radians(angle)))
            print("Cos",math.cos(math.radians(angle)))
            print("Tan",math.tan(math.radians(angle)))
        
        elif inner_user == 4:

            print("""
       Area of Geometric Shapes

A. Circle
B. Rectangle
C. Triangle
D. Back
""")
            shape = input("Enter your Choice (a/b/c/d): ").lower()
        
            if shape == "a":
                              radius = float(input("Enter the Radius of the circle: "))
                              area = math.pi * math.pow(radius,2)
                              print(f"Area of the circle: {round(area,2)}")
    
            elif shape == 'b':
                            length = float(input("Enter length: "))
                            width = float(input("Enter width: "))
                            area = length * width
                            print(f"Area of Rectangle: {round(area, 2)}")
        
            elif shape == 'c':
                            base = float(input("Enter base length: "))
                            height = float(input("Enter height: "))
                            area = 0.5 * base * height
                            print(f"Area of Triangle: {round(area, 2)}")
        
            elif shape == "d":
                        print("Back to the main menu ")
                        continue 
            else:
                        print("Invaid input ")    
        
        elif inner_user == 5:
                        print("Going Back to the main menu")
                        break
        else:
                print("Invaid input ")