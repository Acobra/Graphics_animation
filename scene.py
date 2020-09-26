import turtle
import random
import pygame
wn=turtle.Screen()
wn.title('scene')
wn.bgcolor('black')
#wn.tracer(0)
light_base=turtle.Turtle()
light_base.penup()
light_base.speed(0)
light_base.goto(200,200)
light_base.setheading(270)
light_base.color('white')
for i in range(1,9):
    light_base.pendown()
    light_base.pensize(3)
    if i==1 or i==5:
        light_base.forward(100)
        light_base.left(45)
    elif i==2 or i==4 or i==6 or i==8:
        light_base.forward(25)
        light_base.left(45)
    elif i==3 or i==7:
        light_base.forward(50)
        light_base.left(45)
light_base.hideturtle()
light=turtle.Turtle()
color=['red','yellow','green']
black_color='black'
light.penup()
light.color('red',black_color)
light.goto(243,180)
light.speed(0)
light.begin_fill()
for i in range(25):
    light.pendown()
    light.forward(4)
    light.left(15)
light.end_fill()
light.hideturtle()
yel_light=turtle.Turtle()
yel_light.penup()
yel_light.color('yellow',black_color)
yel_light.goto(243,140)
yel_light.speed(0)
yel_light.begin_fill()
for i in range(25):
    yel_light.pendown()
    yel_light.forward(4)
    yel_light.left(15)
yel_light.end_fill()
yel_light.hideturtle()
last_light=turtle.Turtle()
last_light.penup()
last_light.color('green',black_color)
last_light.goto(243,100)
last_light.speed(0)
last_light.begin_fill()
for i in range(25):
    last_light.pendown()
    last_light.forward(4)
    last_light.left(15)
last_light.end_fill()
last_light.hideturtle()
#main games
#finish line
finish_line=turtle.Turtle()
finish_line.goto(300,-10)
finish_line.color('white')
finish_line.pensize(5)
finish_line.setheading(270)
finish_line.forward(150)
finish_line.hideturtle()
#player1
player1=turtle.Turtle()
player1.penup()
player1.goto(-200,-50)
player1.color('red')
#player2
player2=turtle.Turtle()
player2.penup()
player2.goto(-200,-100)
player2.color('blue')
#player3
player3=turtle.Turtle()
player3.penup()
player3.goto(-200,-150)
player3.color('cyan')
#player2 controls
def moveRight():
    x_speed=random.randint(8,16)
    if player1.xcor() >=1 or player3.xcor()>=1:
        x=player2.xcor()
        x+=x_speed
        player2.setx(x)
wn.listen()
wn.onkeypress(moveRight,"Right")
#player1 and 3 control
tk=turtle.Turtle()
tk.penup()
tk.color('cyan')
tk.goto(-200,200)
tk.hideturtle()
play="C:\\Users\\aayush\\Desktop\\scene\\ring.mp3"
run=True
play_sound=1
count=0
while run:
    wn.update()
    x1_speed = random.randint(1, 10)
    x2_speed = random.randint(1, 10)
    if count==0:
        black_color=color[0]
        light.color('red', black_color)
        light.begin_fill()
        for i in range(25):
            light.pendown()
            light.forward(4)
            light.left(15)
        light.end_fill()
        pygame.mixer.init()
        pygame.mixer.music.load("C:\\Users\\aayush\\Desktop\\scene\\ring.mp3")
        pygame.mixer.music.play()
        tk.write('Ready',False,font=('Arial',50,'bold'))
        player1.setx(player1.xcor())
        player3.setx(player3.xcor())
        count+=1
    elif count==1:
        light.color('red','black')
        light.begin_fill()
        for i in range(25):
            light.pendown()
            light.forward(4)
            light.left(15)
        light.end_fill()
        black_color = color[1]
        yel_light.color('yellow', black_color)
        yel_light.begin_fill()
        for i in range(25):
            yel_light.pendown()
            yel_light.forward(4)
            yel_light.left(15)
        yel_light.end_fill()
        tk.clear()
        tk.write('Steady', False, font=('Arial', 50, 'bold'))
        pygame.mixer.init()
        pygame.mixer.music.load("C:\\Users\\aayush\\Desktop\\scene\\ring.mp3")
        pygame.mixer.music.play()
        player1.setx(player1.xcor())
        player3.setx(player3.xcor())
        count+=1
    elif count==2:
        yel_light.color('yellow','black')
        yel_light.begin_fill()
        for i in range(25):
            yel_light.pendown()
            yel_light.forward(4)
            yel_light.left(15)
        yel_light.end_fill()
        black_color = color[2]
        last_light.color('green',black_color)
        last_light.begin_fill()
        for i in range(25):
            last_light.pendown()
            last_light.forward(4)
            last_light.left(15)
        last_light.end_fill()
        tk.clear()
        r=tk.write('Go', False, font=('Arial', 50, 'bold'))
        if play_sound==1:
            pygame.mixer.init()
            pygame.mixer.music.load(play)
            pygame.mixer.music.play()
            play_sound+=1
        wn.tracer(0)
        player1.setx(player1.xcor() + x1_speed)
        player3.setx(player3.xcor() + x2_speed)
        if player1.xcor()>302:
            tk.clear()
            tk.color('red')
            tk.write('player1 won the race',font=('Arial',30,'bold'))
            break
            run=False
        elif player2.xcor()>302:
            tk.clear()
            tk.color('blue')
            tk.write('player2 won the race',font=('Arial',30,'bold'))
            break
            run = False
        elif player3.xcor()>302:
            tk.clear()
            tk.color('cyan')
            tk.write('player3 won the race',font=('Arial',30,'bold'))
            break
            run = False
pygame.mixer.init()
pygame.mixer.music.load("C:\\Users\\aayush\\Desktop\\scene\\applause.mp3")
pygame.mixer.music.play()
wn.mainloop()