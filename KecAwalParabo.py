import sympy as sp

def kecawal():
    # Definisi variabel simbolik
    v0, theta, h, t, g = sp.symbols('v0 theta h t g')

    # Persamaan gerak parabola
    equation = sp.Eq(-h, v0 * sp.sin(theta) * t - 0.5 * g * t**2)

    # Meminta input dari pengguna
    theta_value = float(input("Masukkan sudut theta (dalam derajat): "))
    h_value = float(input("Masukkan ketinggian h (dalam meter): "))
    t_value = float(input("Masukkan waktu t (dalam detik): "))
    g_value = float(input("Masukkan percepatan gravitasi g (dalam m/s^2): "))

    # Menggantikan nilai yang diketahui
    equation = equation.subs({theta: sp.rad(theta_value), h: h_value, t: t_value, g: g_value})

    # Menyelesaikan persamaan untuk v0
    solutions_v0 = sp.solve(equation, v0)

    # Mengambil solusi positif jika ada
    positive_solution_v0 = [sol.evalf() for sol in solutions_v0 if sol.evalf() >= 0]

    # Menampilkan solusi
    if positive_solution_v0:
        print(f"Besar kecepatan awal (v0): {positive_solution_v0[0]} m/s")
    else:
        print("Tidak ada solusi positif untuk kecepatan awal (v0)")

def jarak():
    v0, theta, t, x = sp.symbols('v0 theta t x')
    equation =sp.Eq(x, v0 * sp.cos(theta) * t)
    theta_value = float(input("Masukkan sudut theta (dalam derajat): "))
    t_value = float(input("Masukkan waktu t (dalam detik): "))
    v0_value = float(input("Masukkan nilai kecepata awal (m/s): "))
    equation = equation.subs({theta: sp.rad(theta_value), t: t_value, v0: v0_value})
    solutions_x = sp.solve(equation, x)
    positive_solution_x = [sol.evalf() for sol in solutions_x if sol.evalf() >= 0]

    # Menampilkan solusi
    if positive_solution_x:
        print(f"Besar jarak (x): {positive_solution_x[0]} m")
    else:
        print("Tidak ada solusi positif untuk kecepatan awal (v0)")

def hmax():
    # Definisi variabel simbolik
    v0, theta, h, g, y0 = sp.symbols('v0 theta h g y0')

    # Persamaan untuk ketinggian maksimum (hmax)
    equation = sp.Eq(h, ((v0**2 * sp.sin(theta)**2) / (2 * g)) + y0)

    # Meminta input dari pengguna
    theta_value = float(input("Masukkan sudut theta (dalam derajat): "))
    v0_value = float(input("Masukkan nilai kecepatan awal (m/s): "))
    g_value = float(input("Masukkan percepatan gravitasi g (dalam m/s^2): "))
    y0_value = float(input("Masukkan ketinggian awal (meter): "))

    # Menggantikan nilai yang diketahui
    equation = equation.subs({theta: sp.rad(theta_value), v0: v0_value, g: g_value, y0: y0_value})

    # Menyelesaikan persamaan untuk hmax
    solutions_hmax = sp.solve(equation, h)

    # Mengambil solusi positif jika ada
    positive_solution_hmax = [sol.evalf() for sol in solutions_hmax if sol.evalf() >= 0]

    # Menampilkan solusi
    if positive_solution_hmax:
        print(f"Ketinggian maksimum (hmax): {positive_solution_hmax[0]} meter")
    else:
        print("Tidak ada solusi positif untuk ketinggian maksimum (hmax)")

print("Menu pilihan: \n 1. Hitung Kecepatan awal. \n 2. jarak maksimal. \n 3. Ketinggian Maksimal.")
pilih = int(input("Pilih menu : "))

if pilih == 1:
    kecawal()
elif pilih == 2:
    jarak()
elif pilih == 3:
    hmax()
else:
    print("tidak valid")