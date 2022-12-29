from square import Square
from canvas import Canvas
from rectangle import Rectangle

# Canvas dimensions
canvas_width = int(input("Insert canvas width: "))
canvas_height = int(input("Insert canvas height: "))

# Canvas color
color = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color: (white or black): ")

# Create canvas
canvas = Canvas(canvas_width, canvas_height, color[canvas_color.lower()])

while True:
    shape_type = input("What do you like to draw? Enter quit to quit... ")

    # Enter rectangle data, if chosen rectangle
    if shape_type.lower() == "rectangle":
        rect_x = int(input("Enter x of rectangle: "))
        rect_y = int(input("Enter y of rectangle: "))
        rect_width = int(input("Enter width of rectangle: "))
        rect_height = int(input("Enter height of rectangle: "))

        # Colors
        red = int(input("How much red should the rectangle have: "))
        green = int(input("How much green should the rectangle have: "))
        blue = int(input("How much blue should the rectangle have: "))

        # Draw rectangle
        r1 = Rectangle(rect_x, rect_y, rect_width, rect_height, (red, green, blue))
        r1.draw(canvas)

    # Enter square data, if chosen square
    elif shape_type.lower() == "square":
        square_x = int(input("Enter x of square: "))
        square_y = int(input("Enter y of square: "))
        square_side = int(input("Enter side of square: "))

        # Colors
        red = int(input("How much red should the square have: "))
        green = int(input("How much green should the square have: "))
        blue = int(input("How much blue should the square have: "))

        # Draw square
        s1 = Square(square_x, square_y, square_side, (red, green, blue))
        s1.draw(canvas)

    elif shape_type.lower() == "quit":
        break
    else:
        print("Please type square, rectangle or quit...")

canvas.make('canvas.png')
