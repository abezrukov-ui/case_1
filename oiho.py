import turtle

# Инициализация
t = turtle.Turtle()
t.speed(1)  # Медленная скорость для контроля
t.pensize(3)  # Толщина линии
t.color("black")

# Функция для рисования ромба
def draw_rhombus(size, angle=60):
    for _ in range(2):
        t.forward(size)
        t.left(angle)
        t.forward(size)
        t.left(120 - angle)

# Функция для рисования треугольника
def draw_triangle(size, angle=60):
    for _ in range(3):
        t.forward(size)
        t.left(120)

# Рисуем голову лисы
# 1. Основной контур (ромб)
t.penup()
t.goto(-30, 0)  # Начальная точка
t.pendown()
draw_rhombus(40, 60)  # Ромб с углом 60°

# 2. Уши (два треугольника сверху)
# Левое ухо
t.penup()
t.goto(-20, 40)
t.pendown()
draw_triangle(25, 60)

# Правое ухо
t.penup()
t.goto(10, 40)
t.pendown()
draw_triangle(25, 60)

# 3. Глаза (два маленьких ромба)
# Левый глаз
t.penup()
t.goto(-15, 15)
t.pendown()
draw_rhombus(8, 60)

# Правый глаз
t.penup()
t.goto(5, 15)
t.pendown()
draw_rhombus(8, 60)

# 4. Нос (треугольник вниз)
t.penup()
t.goto(-5, 10)
t.pendown()
t.setheading(-90)  # Ориентация вниз
draw_triangle(15, 60)

# Скрываем черепашку и завершаем программу
t.hideturtle()
turtle.done()
