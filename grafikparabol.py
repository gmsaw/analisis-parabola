import matplotlib.pyplot as plt
import numpy as np

def gerak_parabola(jarak_maksimum, tinggi_maksimum, sudut_elevasi, jumlah_titik=100):
    g = 9.8  # percepatan gravitasi
    sudut_rad = np.radians(sudut_elevasi)  # konversi sudut ke radian
    
    v0 = np.sqrt((jarak_maksimum * g) / np.sin(2 * sudut_rad))  # kecepatan awal
    t_total = (2 * v0 * np.sin(sudut_rad)) / g  # waktu total penerbangan
    t = np.linspace(0, t_total, jumlah_titik)  # array waktu
    
    # Menghitung posisi (x, y) pada setiap saat t
    x = v0 * np.cos(sudut_rad) * t
    y = v0 * np.sin(sudut_rad) * t - 0.5 * g * t**2 + tinggi_maksimum
    
    return x, y

# Meminta input dari pengguna untuk jumlah grafik
jumlah_grafik = int(input("Berapa banyak grafik yang ingin ditampilkan? "))

# Inisialisasi list untuk menyimpan data setiap grafik
grafik_data = []

# Loop untuk mengumpulkan input untuk setiap grafik
for i in range(jumlah_grafik):
    print(f"\nGrafik sudut {i + 1}:")
    jarak_maksimum = float(input("Masukkan jarak maksimum (m): "))
    tinggi_maksimum = float(input("Masukkan tinggi maksimum (m): "))
    sudut_elevasi = float(input("Masukkan sudut elevasi (derajat): "))
    
    # Menghasilkan data gerak parabola untuk setiap grafik
    x, y = gerak_parabola(jarak_maksimum, tinggi_maksimum, sudut_elevasi)
    
    # Menggeser posisi untuk memulai dari (0,0)
    x -= x[0]
    y -= y[0]
    
    # Menambahkan data ke list grafik_data
    grafik_data.append((x, y, f'Grafik sudut {sudut_elevasi}°'))

# Menampilkan grafik simulasi gerak parabola untuk setiap grafik
for data in grafik_data:
    plt.plot(data[0], data[1], label=data[2])

plt.title('Simulasi Gerak Parabola')
plt.xlabel('Jarak (m)')
plt.ylabel('Tinggi (m)')
plt.legend()
plt.grid(True)
plt.show()