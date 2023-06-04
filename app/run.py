import cv2
import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


matplotlib.use('TkAgg') 
image = cv2.imread("images/BLOG703334.jpg") # Carregar imagem 
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Colocando cor da imagem
image_array = np.array(image) # Converta a imagem para um array NumPy

# Defina a faixa de valores de canal para a cor vermelha
low = np.array([0, 0, 0], dtype=np.uint8)  # Limite inferior (preto)
high = np.array([50, 50, 255], dtype=np.uint8)  # Limite superior (vermelho)

# Encontre os pixels que estão na faixa de cor vermelha
mask = cv2.inRange(image_array, low, high)

# Conte o número de pixels com a cor desejada
pixels_color_red = np.count_nonzero(mask)

# Calcule a porcentagem total
porcentagem_total = (pixels_color_red / image_array.size) * 100

print(f"A porcentagem total da cor vermelha na imagem é: {porcentagem_total}%")

#Plotagem bidimensional: 
plt.imshow(image_rgb , cmap=plt.cm.jet)   
plt.colorbar() # Cores analisadas
plt.show()
