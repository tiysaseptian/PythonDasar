import turtle

# Fungsi menggambar persegi panjang
def gambar_persegi_panjang(pen, panjang, lebar):
    pen.penup()
    pen.goto(-300, 200)  # Pindah ke posisi awal
    pen.pendown()
    pen.color("red")  # Warna merah
    for _ in range(2):
        pen.forward(panjang)  # Panjang sisi
        pen.left(90)
        pen.forward(lebar)    # Lebar sisi
        pen.left(90)

# Fungsi menggambar segitiga
def gambar_segitiga(pen, sisi):
    pen.penup()
    pen.goto(-50, 200)  # Pindah ke posisi awal
    pen.pendown()
    pen.color("yellow")  # Warna kuning
    for _ in range(3):
        pen.forward(sisi)
        pen.left(120)

# Fungsi menggambar trapesium
def gambar_trapesium(pen, atas, bawah, sisi_miring):
    pen.penup()
    pen.goto(200, 200)  # Pindah ke posisi awal
    pen.pendown()
    pen.color("green")  # Warna hijau
    pen.forward(bawah)  # Sisi bawah
    pen.left(120)
    pen.forward(sisi_miring)  # Sisi miring kiri
    pen.left(60)
    pen.forward(atas)  # Sisi atas
    pen.left(60)
    pen.forward(sisi_miring)  # Sisi miring kanan
    pen.left(120)

# Fungsi menggambar jajar genjang
def gambar_jajar_genjang(pen, panjang, lebar):
    pen.penup()
    pen.goto(-300, -50)  # Pindah ke posisi awal
    pen.pendown()
    pen.color("blue")  # Warna biru
    pen.forward(panjang)  # Sisi bawah
    pen.left(60)
    pen.forward(lebar)  # Sisi miring kanan
    pen.left(120)
    pen.forward(panjang)  # Sisi atas
    pen.left(60)
    pen.forward(lebar)  # Sisi miring kiri
    pen.left(120)

# Fungsi menggambar belah ketupat
def gambar_belah_ketupat(pen, sisi):
    pen.penup()
    pen.goto(50, -50)  # Pindah ke posisi awal
    pen.pendown()
    pen.color("purple")  # Warna ungu
    for _ in range(2):
        pen.forward(sisi)
        pen.left(60)
        pen.forward(sisi)
        pen.left(120)

# Membuat turtle
pen = turtle.Turtle()
pen.speed(3)

# Memanggil fungsi untuk menggambar masing-masing bangun
gambar_persegi_panjang(pen, 150, 100)
gambar_segitiga(pen, 100)
gambar_trapesium(pen, 80, 150, 100)
gambar_jajar_genjang(pen, 150, 100)
gambar_belah_ketupat(pen, 100)

# Menyelesaikan gambar
pen.hideturtle()
turtle.done()