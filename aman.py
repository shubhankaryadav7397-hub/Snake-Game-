import turtle
import random
import time

delay = 0.1
score = 0
high_score = 0
bodies = []  # List to store snake body segments

# Creating the screen
s = turtle.Screen()
s.title("SNAKE GAME")
s.bgcolor("light blue")
s.setup(width=600, height=600)

# Creating the snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("blue")
head.fillcolor("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Creating the food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.fillcolor("blue")
food.penup()
food.goto(random.randint(-290, 290), random.randint(-290, 290))

# Creating the scoreboard
sb = turtle.Turtle()
sb.penup()
sb.ht()
sb.goto(-250, 250)
sb.write("Score: 0 | Highest Score: 0", align="left", font=("Arial", 14, "bold"))

# Movement functions
def moveup():
    if head.direction != "down":
        head.direction = "up"

def movedown():
    if head.direction != "up":
        head.direction = "down"

def moveright():
    if head.direction != "left":
        head.direction = "right"

def moveleft():
    if head.direction != "right":  # Fixed the incorrect condition
        head.direction = "left"

def movestop():
    head.direction = "stop"

# Main move function
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)

# Event handling
s.listen()
s.onkey(moveup, "Up")
s.onkey(movedown, "Down")
s.onkey(moveleft, "Left")
s.onkey(moveright, "Right")
s.onkey(movestop, "space")

# Main game loop
while True:
    s.update()

    # Border collision handling (wrap-around)
    if head.xcor() > 290:
        head.setx(-290)
    if head.xcor() < -290:
        head.setx(290)
    if head.ycor() > 290:
        head.sety(-290)
    if head.ycor() < -290:
        head.sety(290)

    # Check collision with food
    if head.distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))

        # Increase the size of the snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        bodies.append(body)

        # Update score
        score += 100
        delay -= 0.001
        if score > high_score:
            high_score = score
        
        sb.clear()
        sb.write(f"Score: {score} | Highest Score: {high_score}", align="left", font=("Arial", 14, "bold"))

    # Move snake body
    for i in range(len(bodies) - 1, 0, -1):
        x = bodies[i - 1].xcor()
        y = bodies[i - 1].ycor()
        bodies[i].goto(x, y)

    if bodies:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # Check collision with snake body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide all body parts
            for body in bodies:
                body.ht()
            bodies.clear()

            score = 0
            delay = 0.1

            sb.clear()
            sb.write(f"Score: {score} | Highest Score: {high_score}", align="left", font=("Arial", 14, "bold"))

    time.sleep(delay)

s.mainloop()               
        
            
            
    
                
    




