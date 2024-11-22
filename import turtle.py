import turtle

# Atur layar
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Masjid Sederhana dengan Python")

# Fungsi untuk menggambar persegi panjang
def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

# Fungsi untuk menggambar lingkaran
def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)  # Pindahkan posisi ke bawah untuk lingkaran
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
…