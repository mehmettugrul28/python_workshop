import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle
from matplotlib.transforms import Affine2D

# Deprem parametreleri
deprem_siddeti = 8  # 1-10 arası bir değer (ne kadar büyükse o kadar şiddetli)
frekans = deprem_siddeti * 0.5  # Frekans, şiddete bağlı olarak artıyor

# Animasyon için figür ve eksen oluştur
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(0, 5)
ax.set_aspect('equal')

# Bina çizimi
bina = Rectangle((-0.5, 0), 1, 4, color='brown')
ax.add_patch(bina)

# Animasyon başlangıç fonksiyonu
def init():
    bina.set_transform(ax.transData)  # Başlangıçta dönüşümsüz olarak ayarla
    return bina,

# Deprem hareketi fonksiyonu
def animate(frame):
    angle = np.sin(frame * 0.1 * frekans) * (deprem_siddeti * 2)  # Binanın eğim açısı
    trans = Affine2D().rotate_deg_around(0, 0, angle) + ax.transData  # Dönüşüm uygula
    bina.set_transform(trans)
    return bina,

# Animasyonu başlat
ani = animation.FuncAnimation(fig, animate, frames=100, init_func=init, interval=50, blit=True)
plt.title("Deprem Simülasyonu")
plt.show()
