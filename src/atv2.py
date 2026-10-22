import numpy as np
import matplotlib.pyplot as plt

AZUL = (0, 85, 164)
BRANCO = (255, 255, 255)
VERMELHO = (239, 65, 53)

bandeira = np.zeros((12, 18, 3), dtype=np.uint8)
bandeira[:, :6] = AZUL
bandeira[:, 6:12] = BRANCO
bandeira[:, 12:] = VERMELHO

plt.imshow(bandeira)
plt.title("Bandeira da França")
plt.axis("off")
plt.show()