import turtle

# Создаём экран и черепашку
screen = turtle.Screen()
screen.setup(800, 400)
t = turtle.Turtle()
t.speed(10)
t.pensize(3)
t.ht()

#Создаем сетку
import turtle

# Настройка
screen = turtle.Screen()
screen.setup(800, 400)
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

t.penup()

#Рисуем  4 треугольника
t.goto(-380, 190)


t.pendown()
t.fillcolor("yellow")
t.begin_fill()

t.goto(-360, 180)
t.goto(-380, 180)
t.goto(-380, 190)

t.end_fill()

t.penup()

t.goto(-380, 160)

t.penup()

t.pendown()
t.fillcolor("yellow")
t.begin_fill()

t.goto(-360, 160)
t.goto(-380, 150)
t.goto(-380, 160)

t.end_fill()

t.penup()

t.goto(-330, 180)

t.penup()

t.pendown()
t.fillcolor("yellow")
t.begin_fill()

t.goto(-310, 190)
t.goto(-310, 180)
t.goto(-330, 180)

t.end_fill()

t.penup()

t.goto(-330, 160)

t.penup()

t.pendown()
t.fillcolor("yellow")
t.begin_fill()

t.goto(-310, 160)
t.goto(-310, 150)
t.goto(-330, 160)

t.end_fill()

#Теперь рисуем прямоугольник
t.penup()
t.goto(-380, 180)
t.pendown()

t.fillcolor("pink")
t.begin_fill()
for _ in range(2):
    t.forward(70)
    t.right(90)
    t.forward(20)
    t.right(90)

t.end_fill()
t.penup()

#Рисуем 2 прямоугольник
t.goto(-350, 160)
t.pendown()
t.fillcolor("pink")
t.begin_fill()
t.begin_fill()
for _ in range(2):
    t.forward(10)
    t.right(90)
    t.forward(50)
    t.right(90)

t.end_fill()
#Рисуем 5 треугольник
t.penup()
t.goto(-350, 110)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()

t.goto(-340, 110)
t.goto(-345, 105)
t.goto(-350, 110)

t.end_fill()
t.penup()

#Второй рисункок
t.goto(-160, 140)
t.pendown()
t.fillcolor("pink")
t.begin_fill()

for _ in range(4):
    t.forward(20)
    t.right(90)
t.end_fill()
t.penup()

#Рисуем ухо
t.goto(-140, 140)
t.pendown()

t.fillcolor("pink")
t.begin_fill()
katet = 20

t.forward(katet)
t.left(90)
t.forward(katet)
t.goto(-140, 140)
t.end_fill()

#Рисуем туловище
t.penup()
t.goto(-140, 130)
t.pendown()

t.fillcolor("pink")
t.begin_fill()
katet = 50

t.backward(katet)
t.right(90)
t.forward(katet)
t.goto(-140, 130)
t.end_fill()

t.penup()
t.goto(-60, 50)
t.pendown()

t.fillcolor("pink")
t.begin_fill()
katet = 50

t.left(90)

t.forward(katet)
t.left(90)
t.forward(katet)
t.goto(-60, 50)
t.end_fill()


t.penup()
t.goto(-120, 80)
t.pendown()
t.fillcolor("pink")
t.begin_fill()

t.left(45)
for _ in range(2):
    t.forward(800**0.5)
    t.right(45)
    t.forward(40)
    t.right(135)
t.end_fill()


t.penup()
t.goto(-60, 100)
t.pendown()
t.fillcolor("pink")
t.begin_fill()

t.left(135)

t.forward(20)
t.left(90)
t.forward(20)
t.goto(-60, 100)
t.end_fill()


t.penup()
t.goto(-60, 40)
t.pendown()
t.fillcolor("pink")

t.begin_fill()
t.setheading(270)
t.forward(800**0.5/2)
t.left(135)
t.forward(800**0.5)
t.left(90)
t.forward(800**0.5)
t.goto(-60, 40)
t.end_fill()
t.penup()
t.end_fill()
t.penup()
t.end_fill()


#Рисуем цветок
t.penup()
t.goto(70,20)
t.pendown()

#Рисуем горшок
t.fillcolor("brown")
t.left(225)
t.begin_fill()
for _ in range(2):
    t.forward(60)
    t.left(90)
    t.forward(30)
    t.left(90)
t.end_fill()

t.penup()
t.goto(65,50)
t.pendown()

#Рисуем верхнюю часть горшка
t.fillcolor("brown")
t.begin_fill()
for _ in range(2):
    t.forward(70)
    t.left(90)
    t.forward(10)
    t.left(90)
t.end_fill()

#Рисуем стебель
t.penup()
t.goto(100, 60)
t.pendown()
t.pensize(5)
t.pencolor("green")
t.left(90)
t.forward(70)

#Рисуем листья
t.penup()
t.goto(125, 75)
t.pendown()
t.fillcolor("green")
t.begin_fill()
for _ in range(3):
    t.forward(25)
    t.left(120)
t.end_fill()

t.penup()
t.goto(80, 75)
t.pendown()
t.begin_fill()
for _ in range(3):
    t.forward(20)
    t.right(120)
t.end_fill()

t.penup()
t.goto(100, 140)
t.pendown()

#Рисуем лепестки
t.pensize(1)
circle_radius = 20
for _ in range(6):
    t.fillcolor("pink")
    t.begin_fill()
    t.circle(circle_radius)
    t.end_fill()
    t.penup()
    t.left(240)
    t.right(3 * circle_radius)
    t.right(240)
    t.pendown()

#Рисуем сердцевину
t.penup()
t.goto(110,130)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
for _ in range(4):
    t.forward(20)
    t.left(90)
t.end_fill()


#Рисуем корабль
t.penup()
t.goto(240,60)
t.pendown()

#Рисуем край
t.fillcolor("red")
t.begin_fill()
for _ in range(1):
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.left(135)
    t.forward(45)
t.end_fill()

t.penup()
t.goto(270,75)
t.pendown()

#Рисуем корпус
t.fillcolor("yellow")
t.right(135)
t.left(270)
t.begin_fill()
for _ in range(4):
    t.forward(15)
    t.left(90)
    t.forward(15)
t.end_fill()

t.penup()
t.goto(330,75)
t.pendown()

t.fillcolor("yellow")
t.begin_fill()
for _ in range(4):
    t.forward(15)
    t.left(90)
    t.forward(15)
t.end_fill()

t.penup()
t.goto(300,95)
t.pendown()

#Рисуем башню
t.fillcolor("brown")
t.begin_fill()
for _ in range(2):
    t.forward(50)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(35)
t.end_fill()

t.penup()
t.goto(292,125)
t.pendown()

#Рисуем окно
t.fillcolor("yellow")
t.begin_fill()
for _ in range(4):
    t.forward(8)
    t.left(90)
    t.forward(8)
t.end_fill()

#Рисуем края
t.penup()
t.goto(330,90)
t.pendown()
t.right(90)
t.fillcolor("red")
t.begin_fill()
t.forward(30)
t.right(135)
t.forward(45)
t.end_fill()

t.penup()
t.goto(280,145)
t.pendown()

#Рисуем крышу
t.fillcolor("red")
t.begin_fill()
t.left(135)
t.forward(30)
t.left(150)
t.forward(30)
t.left(60)
t.forward(30)
t.left(150)
t.forward(30)
t.end_fill()

t.hideturtle()
screen.exitonclick()
