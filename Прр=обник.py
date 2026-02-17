import turtle

# Создаём экран и черепашку
screen = turtle.Screen()
screen.setup(800, 400)
t = turtle.Turtle()
t.speed(10)  # Ускоряем рисование
t.pensize(3)  # Увеличиваем толщину линий

t.pos()


#Создаем сетку
import turtle

# Настройка
screen = turtle.Screen()
screen.setup(800, 400)
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.pensize(2)


def draw_grid_lines():
    """Рисует только линии сетки"""

    # Вертикальные линии (делим ширину 800 на 4 части по 200)
    for x in range(-400, 401, 200):  # от -400 до 400 с шагом 200
        t.penup()
        t.goto(x, -200)
        t.pendown()
        t.goto(x, 200)

    # Горизонтальные линии (делим высоту 400 на 2 части по 200)
    for y in range(-200, 201, 200):  # от -200 до 200 с шагом 200
        t.penup()
        t.goto(-400, y)
        t.pendown()
        t.goto(400, y)



# Рисуем сетку
draw_grid_lines()

# Показываем центр
t.penup()
t.goto(0, 0)
t.dot(10, "red")
t.write("Центр (0,0)", font=("Arial", 10))

t.hideturtle()

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
    t.forward(70)   # длина
    t.right(90)
    t.forward(20)   # ширина
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
    t.forward(20)   # длина
    t.right(90)
t.end_fill()
t.penup()

#Рисуем ухо
t.goto(-140, 140)
t.pendown()

t.fillcolor("pink")
t.begin_fill()
katet = 20

t.forward(katet)      # первый катет
t.left(90)            # поворот на 90 градусов
t.forward(katet)      # второй катет
t.goto(-140, 140)          # гипотенуза (возврат в начало)
t.end_fill()

#Рисуем туловище
t.penup()
t.goto(-140, 130)
t.pendown()

t.fillcolor("pink")
t.begin_fill()
katet = 50

t.backward(katet)      # первый катет
t.right(90)            # поворот на 90 градусов
t.forward(katet)      # второй катет
t.goto(-140, 130)          # гипотенуза (возврат в начало)
t.end_fill()

t.penup()
t.goto(-60, 50)
t.pendown()

t.fillcolor("pink")
t.begin_fill()
katet = 50

t.left(90)

t.forward(katet)      # первый катет
t.left(90)            # поворот на 90 градусов
t.forward(katet)      # второй катет
t.goto(-60, 50)          # гипотенуза (возврат в начало)
t.end_fill()


t.penup()
t.goto(-120, 80)
t.pendown()
t.fillcolor("pink")
t.begin_fill()

t.left(45)
for _ in range(2):
    t.forward(800**0.5)   # длина
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
t.left(90)# второй катет
t.forward(20)
t.goto(-60, 100)          # гипотенуза (возврат в начало)
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
t.penup()


turtle.done()