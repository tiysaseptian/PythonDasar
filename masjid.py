import turtle

# Atur layar
screen = turtle.Screen()
screen.bgcolor("darkblue")
screen.title("Bulan Sabit dengan Python")

# Atur turtle
moon = turtle.Turtle()
moon.shape("turtle")
moon.color("white")
moon.speed(10)

# Gambar lingkaran penuh sebagai dasar bulan
moon.penup()
moon.goto(0, -100)  # Posisikan turtle
moon.pendown()
moon.begin_fill()
moon.circle(100)
moon.end_fill()

# Gambar lingkaran lebih kecil untuk membuat efek bulan sabit
moon.penup()
moon.goto(30, -100)  # Geser posisi untuk lingkaran kecil
moon.color("darkblue")  # Warna lingkaran sesuai background
moon.pendown()
moon.begin_fill()
moon.circle(100)
moon.end_fill()

# Selesai
moon.hideturtle()
screen.mainloop()