import turtle as t
import colorsys

t.bgcolor('black')
t.speed(0)
t.pensize(2)
hue = 0.0
t.hideturtle()

# Define your name
your_name = "By aby"

for i in range(500):
    # Update color using HSV gradient
    hue += 0.005
    if hue > 1.0:
        hue -= 1.0
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    t.pencolor(color)

    # Draw spiral
    t.forward(i)
    t.right(98.5)
    t.circle(50)

    # Shimmering effect
    t.lt(0.5)

# Write your name
t.penup()
t.goto(150, -300)  # Adjust the position of the name
t.color('white')  # Set the color of the name
t.write(your_name, align='center', font=('Pacifico', 20, 'bold'))

t.exitonclick()

