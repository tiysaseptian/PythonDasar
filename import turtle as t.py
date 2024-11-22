import turtle as t

# Setup turtle
t.speed(0)
t.bgcolor("white")
t.title("Logo SMK Prestasi Prima")

# Fungsi menggambar lingkaran berisi
def draw_circle(color, radius, position):
    t.penup()
    t.goto(position)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Fungsi menggambar persegi
def draw_square(color, size, position):
    t.penup()
    t.goto(position)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

# Fungsi menggambar persegi panjang
def draw_rectangle(color, width, height, position, angle=0):
    t.penup()
    t.goto(position)
    t.setheading(angle)  # Mengatur rotasi untuk kemiringan
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Lingkaran hitam luar
draw_circle("black", 160, (0, -160))

# Lingkaran putih kedua
draw_circle("white", 140, (0, -140))

# Lingkaran biru paling dalam
draw_circle("blue", 100, (0, -100))

# ===== Telapak Tangan =====
# Telapak tangan berada tepat di tengah
draw_rectangle("red", 100, 40, (-50, -80))  # Telapak tangan sejajar tengah

# ===== Jempol =====
thumb_angle = 30  # Ganti nilai ini untuk mengubah kemiringan jempol
draw_rectangle("red", 23, 30, (-45, -20), angle=thumb_angle)  # Jempol sejajar dengan tangan

# ===== Telunjuk =====
draw_rectangle("red", 20, 90, (-35, -20))  # Telunjuk lebih tinggi

# ===== Jari Tengah =====
draw_rectangle("red", 20, 40, (-11, -20))  # Jari tengah lebih tinggi

# ===== Jari Manis =====
draw_rectangle("red", 20, 33, (11, -20))  # Jari manis lebih tinggi

# ===== Kelingking =====
draw_rectangle("red", 20, 33, (33, -20))  # Kelingking lebih pendek dari jari tengah dan manis

# Menambahkan teks "SMK PRESTASI PRIMA" di bawah logo
t.penup()
t.goto(0, -200)  # Menyesuaikan posisi teks
t.color("black")
t.write("SMK PRESTASI PRIMA", align="center", font=("Arial", 20, "bold"))

# Menambahkan teks "IF BETTER IS POSSIBLE, GOOD IS NOT ENOUGH" di bawah teks sebelumnya
t.penup()
t.goto(0, -230)  # Menyesuaikan posisi teks
t.color("black")
t.write("IF BETTER IS POSSIBLE, GOOD IS NOT ENOUGH", align="center", font=("Arial", 14, "italic"))

# Selesai menggambar
t.hideturtle()
t.done()