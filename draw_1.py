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

    # Подписываем координаты углов
    t.penup()
    t.goto(-400, -220)
    t.write("(-400,-200)", font=("Arial", 8))
    t.goto(380, -220)
    t.write("(400,-200)", font=("Arial", 8))
    t.goto(-400, 180)
    t.write("(-400,200)", font=("Arial", 8))
    t.goto(380, 180)
    t.write("(400,200)", font=("Arial", 8))


# Рисуем сетку
draw_grid_lines()

# Показываем центр
t.penup()
t.goto(0, 0)
t.dot(10, "red")
t.write("Центр (0,0)", font=("Arial", 10))

t.hideturtle()
turtle.done()

