import turtle

print("Turtle is imported")

window = turtle.Screen()
window.bgcolor("light blue")
window.title("Spirals")
bob = turtle.Turtle()

bob.penup()
bob.goto(-80, -100) #position cursor at the bootom right of the screen
bob.pendown()

length = 200
for i in range (1,27):
   bob.forward(length)
   bob.left(120)
   length = length - 8

turtle.done()


# Description:

# 1. First I am setting position of cursor at -80, -100 coordinates
# 2. Then simply I have used for loop which moves turtle forward first for 200 pixels and then it takes an angle of 120 degrees
#    on left. Then I reduce the length of triangular side by 8 pixels for each iteration.
# 3. This loops from 1 to 27.
