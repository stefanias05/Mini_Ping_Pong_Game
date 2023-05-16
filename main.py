import turtle

'''creare ecran'''
screen = turtle.Screen()
'craere titlu si culoare window'
screen.title('Ping Pong')
screen.bgcolor('Grey')
'''creare setari ecran: lungime, latime'''
screen.setup(width=700, height=500)
'''activare window si actualizare desen: tracer(n,z) n- actualizare ecran, z-valoarea intarzierii act.'''
screen.tracer(0)

'''jucatori'''
jucator1 =turtle.Turtle()
jucator1.shape('square')
jucator1.color('white')
jucator1.shapesize(stretch_wid=5, stretch_len=1)
jucator1.penup()
#position jucator 1
jucator1.goto(-250,0)

jucator2 =turtle.Turtle()
jucator2.shape('square')
jucator2.color('white')
jucator2.shapesize(stretch_wid=5, stretch_len=1)
jucator2.penup()
#position jucator 2
jucator2.goto(250,0)


'''creare minge de joc'''
ball = turtle.Turtle()
ball.shape('circle')
ball.color('black')
ball.penup()
ball.goto(0,0)
ball.dx =0.1
ball.dy = -0.1

'''scorul'''
score1= 0
score2= 0
score = turtle.Turtle()

score.color("white")
score.hideturtle()
score.penup()
score.goto(0,260)
score.write("Player 1 : 0  Player 2 : 0", align="center", font=("Courier",22,"normal"))



step = 10


'''miscare minge'''

def move_ball():
     '''setare locatie minge pe axa X + 0.1'''
     ball.setx(ball.xcor() + ball.dx)
     ball.sety(ball.ycor() +ball.dy)

     x = ball.xcor()
     y = ball.ycor()

     if x > 390:
         ball.setx(390)
         ball.dx = ball.dx * -1
     if x < -390:
        ball.setx(-390)
        ball.dx = ball.dx * -1
     if y >290:
        ball.sety(290)
        ball.dy = ball.dy *-1
     if y < -290:
        ball.sety(-290)
        ball.dy = ball.dy * -1




'''functie pentru jucaror 1 pt initiere miscari'''
def jucator1_up():
    '''returnez coordonatele y'''
    j= jucator1.ycor()
    '''nr de px necesari miscarii'''
    j = j + step
    '''setez a doua coordonata y, prima ramanan neschimbata'''
    jucator1.sety(j)
    '''verific ca jucatorul sa nu iasa din ecran.'''
    if j > 210:
        jucator1.sety(210)

def jucator1_down():
    j = jucator1.ycor()
    j = j - step
    jucator1.sety(j)
    if j < -210:
        jucator1.sety(-210)

def jucator1_dreapta():
    ''':returnez coordonatele x'''
    j = jucator1.xcor()
    j = j + step
    '''setez prima coordonata x, a doua ramanand neschimbata'''
    jucator1.setx(j)
    if j > -10:
        jucator1.setx(-10)


def jucator1_stanga():
    ''':returnez coordonatele x'''
    j = jucator1.xcor()
    j = j - step
    '''setez prima coordonata x, a doua ramanand neschimbata'''
    jucator1.setx(j)
    if j < -350:
        jucator1.setx(-350)


def jucator2_up():
    '''returnez coordonatele y'''
    j= jucator2.ycor()
    j = j + 10
    '''setez a doua coordonata y, prima ramanan neschimbata'''
    jucator2.sety(j)
    '''verific ca jucatorul sa nu iasa din ecran.'''
    if j > 210:
        jucator2.sety(210)

def jucator2_down():
    j = jucator2.ycor()
    j = j - step
    jucator2.sety(j)
    if j < -210:
        jucator2.sety(-210)

def jucator2_dreapta():
    ''':returnez coordonatele x'''
    j = jucator2.xcor()
    j = j + step
    '''setez prima coordonata x, a doua ramanand neschimbata'''
    jucator2.setx(j)
    if j > 350:
        jucator2.setx(350)


def jucator2_stanga():
    ''':returnez coordonatele x'''
    j = jucator2.xcor()
    j = j - step
    '''setez prima coordonata x, a doua ramanand neschimbata'''
    jucator2.setx(j)
    if j < 10:
        jucator2.setx(10)

'''Opresc miscarea mingii la intersectia cu jucatorul-> Collision Detection'''
def checkCollision():
    if (jucator1.xcor() + 20 >= ball.xcor() >= jucator1.xcor() - 20) and (
            jucator1.ycor() + 60 >= ball.ycor() >= jucator1.ycor() - 60):
        ball.dx = ball.dx * -1
        ball.dy = ball.dy * -1

        x = ball.xcor()
        x = x + 10
        ball.setx(x)

    if (jucator2.xcor() + 20 >= ball.xcor() >= jucator2.xcor() - 20) and (
            jucator2.ycor() + 60 >= ball.ycor() >= jucator2.ycor() - 60):
        ball.dx = ball.dx * -1
        ball.dy = ball.dy * -1

        x = ball.xcor()
        x = x - 10
        ball.setx(x)




'''inregistrez ecranului evenimentele de la tastatura '''
screen.listen()


'''la apasarea butonului 1 jucarorul1 va urca. idem cu jucatorul 2'''
screen.onkeypress(jucator1_up, '1')
screen.onkeypress(jucator2_up, '2')

'''apasare butoane pt miscare down'''
screen.onkeypress(jucator1_down, '9')
screen.onkeypress(jucator2_down, '0')

'''apasare buton pt miscare dreapta'''
screen.onkeypress(jucator2_dreapta, 'k')
screen.onkeypress(jucator1_dreapta,'d')

'''apasare buton pt miscare stanga'''
screen.onkeypress(jucator1_stanga, 's')
screen.onkeypress(jucator2_stanga,'l')

'''create infinite loop'''
while(1):
    screen.update()
    move_ball()
    checkCollision()

    '''calculez scorul jucatorilor in functie de miscarile pe axa'''
    if ball.xcor() >= 350:
        score1 = score1 + 1
        score.clear()
        score.write("Player 1 : {}  Player 2 : {}".format(score1, score2), align="center",
                        font=("Courier", 22, "normal"))
        ball.goto(0, 0)
        ball.dx = ball.dx * -1

    if ball.xcor() < -350:
        score2 = score2 + 1
        score.clear()
        score.write("Player 1 : {}  Player 2 : {}".format(score1, score2), align="center",
                        font=("Courier", 22, "normal"))
        ball.goto(0, 0)
        ball.dx = ball.dx * -1