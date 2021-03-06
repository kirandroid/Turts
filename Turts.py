import turtle

turtle.showturtle()
print("[0] Change title: ")
print("[1] Turn left: ")
print("[2] Move forward: ")
print("[3] Penup: ")
print("[4] Pendown: ")
print("[5] Draw circle: ")
print("[6] Draw a dot: ")
print("[7] Change color: ")
print("[8] Change background color: ")
print("[9] Change turtle shape: ")
print("[10] Change pensize: ")
x = eval(input("Enter the option: "))
while True:
    if x == 0:
        title_text = input("Enter title: ")
        turtle.title(title_text)
        x = eval(input("Enter the option: "))
    elif x == 1:
        left_angle = eval(input("Enter angle: "))
        turtle.left(left_angle)
        x = eval(input("Enter the option: "))
    elif x == 2:
        forward_angle = eval(input("Enter distance: "))
        turtle.forward(forward_angle)
        x = eval(input("Enter the option: "))
    elif x == 3:
        turtle.penup()
        x = eval(input("Enter the option: "))
    elif x == 4:
        turtle.pendown()
        x = eval(input("Enter the option: "))
    elif x == 5:
        circle_angle = eval(input("Enter size "))
        turtle.circle(circle_angle)
        x = eval(input("Enter the option: "))
    elif x == 6:
        dot_angle = eval(input("Enter size: "))
        dot_color_angle = input("Enter color of dot: ")
        turtle.dot(dot_angle, dot_color_angle)
        x = eval(input("Enter the option: "))
    elif x == 7:
        color_angle = input("Enter color: ")
        turtle.color(color_angle)
        x = eval(input("Enter the option: "))
    elif x == 8:
        bg_color_angle = input("Enter color: ")
        turtle.bgcolor(bg_color_angle)
        x = eval(input("Enter the option: "))
    elif x == 9:
        print("[1] Arrow: ")
        print("[2] Turtle: ")
        print("[3] Circle: ")
        print("[4] Square: ")
        print("[5] Triangle: ")
        print("[6] Classic: ")

        in_shape = eval(input("Enter the shape option: "))

        if in_shape == 1:
            turtle.shape("arrow")
            x = eval(input("Enter the option: "))
        elif in_shape == 2:
            turtle.shape("turtle")
            x = eval(input("Enter the option: "))
        elif in_shape == 3:
            turtle.shape("circle")
            x = eval(input("Enter the option: "))
        elif in_shape == 4:
            turtle.shape("square")
            x = eval(input("Enter the option: "))
        elif in_shape == 5:
            turtle.shape("triangle")
            x = eval(input("Enter the option: "))
        elif in_shape == 6:
            turtle.shape("classic")
            x = eval(input("Enter the option: "))
        else:
            print("Invalid input")
            break
    elif x == 10:
        pensize_angle = eval(input("Enter pensize: "))
        turtle.pen(pensize=pensize_angle)
        x = eval(input("Enter the option: "))
    else:
        print("Enter from 1-6")
        break
