import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.speed(100)

# Idea: we draw a triangle and apply the koch algorithm to each side of the triangle
# However we cannot change the koch function, as it messes up the koch pattern
# So create a new function which draws one koch side on the triangle, then turns 120 degrees
# This way a full triangle will be created, and on each side the koch function will be called

def koch(t, order, size):
    # We draw 3 sides
    for i in range(3):
        # We put the original koch recursion function here
        def koch2(t, order, size):
            if order == 0:
                t.forward(size)
            else:
                for angle in [60, -120, 60, 0]:
                    koch2(t, order-1, size/3)
                    t.left(angle)
        # Draw one side of the triangle containing an n-th order koch pattern, then turn 120 degrees
        koch2(t, order, size)
        t.right(120)

koch(tess, 2, 150)

wn.mainloop()
