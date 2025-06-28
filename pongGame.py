import turtle
import random 

# Initialize screen
myScr = turtle.Screen()
myScr.tracer(0)  # Disable automatic screen updates for better control
#myScr.setup(width=324*2, height=384*2)  # Ensure a properly sized window

# Initialize turtles
rightTurtle = turtle.Turtle()
sepTurtle = turtle.Turtle()
leftTurtle = turtle.Turtle()
ballTurtle = turtle.Turtle()
scoreTurtle1 = turtle.Turtle()
scoreTurtle2 = turtle.Turtle()

# Adjust speed
rightTurtle.speed(0)
leftTurtle.speed(0)
sepTurtle.speed(0)
ballTurtle.speed(0)
scoreTurtle1.speed(0)
scoreTurtle2.speed(0)

# Right paddle
rightTurtle.penup()
rightTurtle.shape("square")
rightTurtle.shapesize(5, 1)
rightTurtle.setpos(324, 0)

# Left paddle
leftTurtle.penup()
leftTurtle.shape("square")
leftTurtle.shapesize(5, 1)
leftTurtle.setpos(-324, 0)

# Separator
sepTurtle.penup()
sepTurtle.shape("square")
sepTurtle.shapesize(768, 0.25)

# Ball
ballTurtle.penup()
ballTurtle.shape("circle")
ballTurtle.shapesize(1, 1)

# Score Display
scoreTurtle1.penup()
scoreTurtle1.hideturtle()
scoreTurtle1.goto(81, 256)

scoreTurtle2.penup()
scoreTurtle2.hideturtle()
scoreTurtle2.goto(-81, 256)

score1 = 0
score2 = 0

def updateScore(right,left):
    global score1, score2
    if right:
        score1=score1+1
        right=0
    if left:
        score2=score2+1
        left=0
    scoreTurtle1.clear()
    scoreTurtle2.clear()
    scoreTurtle1.write(score1, font=("Arial", 20, "bold"))
    scoreTurtle2.write(score2, font=("Arial", 20, "bold"))

# Ball movement variables
ballTurtle.dx = 7  # Lower speed for smoother movement
ballTurtle.dy = 7


# Move paddle based on click
def moveTurtle(x, y):
    if x > 0:  # Right side
        rightTurtle.goto(324, y)
    else:  # Left side
        leftTurtle.goto(-324, y)

myScr.onscreenclick(moveTurtle)

# Reverse ball direction with slight variation
def reverse_ballx():
    ballTurtle.dx *= -1  # Reverse X direction
    ballTurtle.dy += random.uniform(-2, 2)  # Add small random variation

def reverse_bally():
    ballTurtle.dy *= -1  # Reverse Y direction
    ballTurtle.dx += random.uniform(-2, 2)  # Add small random variation


# Ball movement function
def move_ball():
    ballTurtle.setx(ballTurtle.xcor() + ballTurtle.dx)
    ballTurtle.sety(ballTurtle.ycor() + ballTurtle.dy)

    # Boundary collision (Top & Bottom)
    if ballTurtle.ycor() >= 382:
        ballTurtle.sety(382)
        reverse_ballx()
        reverse_bally()

    if ballTurtle.ycor() <= -382:
        ballTurtle.sety(-382)
        reverse_bally()
        reverse_ballx()
    

    # Boundary collision (Left & Right)
    if ballTurtle.xcor() >= 322:
        ballTurtle.setx(322)  # FIXED: set x, not y
        reverse_ballx()

    if ballTurtle.xcor() <= -322:
        ballTurtle.setx(-322)  # FIXED: set x, not y
        reverse_ballx()

        # Paddle collision
    if (ballTurtle.xcor() > 314 and ballTurtle.xcor() < 334) and (rightTurtle.ycor() - 50 < ballTurtle.ycor() < rightTurtle.ycor() + 50):
        ballTurtle.setx(314)
        reverse_ballx()  # Reverse X direction
        updateScore(1,0)

    if (ballTurtle.xcor() < -314 and ballTurtle.xcor() > -334) and (leftTurtle.ycor() - 50 < ballTurtle.ycor() < leftTurtle.ycor() + 50):
        ballTurtle.setx(-314)
        reverse_ballx()  # Reverse X direction
        updateScore(0,1)

    myScr.update()  # Refresh screen manually
    myScr.ontimer(move_ball, 10)  # Schedule next frame

# Start the game loop
move_ball()
updateScore(score1, score2)

# Keep the window open
myScr.mainloop()
