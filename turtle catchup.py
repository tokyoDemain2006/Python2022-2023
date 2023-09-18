from turtle import *
#imports turtle from the python library
color("blue", "red")
begin_fill()
#sets colour and begins the fill
shape = int(input("how many sides do you want in your shape"))
#asks the user how many sides are needed
for i in range(0, shape):
    #starts the loop
    forward(1000/shape)
    right(360/shape)
    #sets the size and rotation based off the amount of sides
end_fill()
done()
#finishes the program



