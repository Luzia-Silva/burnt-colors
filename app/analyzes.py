import cv2
import cv2
import numpy as np

def DegreesOfBurns():
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
  porcentage = (pixels_color_red / 100)
  return porcentage
  
def AnalyzesTheBurns(burn_value, burns_values): 
      if len(burns_values) > 0:
        values = np.array(burns_values, dtype=float)
        bigger = np.max(values)
        smaller = np.min(values)
        median = np.median(values)
        if str(smaller) < str(burn_value):
            print(" \n 1º grau: atinge a epiderme (camada superficial da pele)." + str(burn_value))
            print("\n Dados encontrados: \n MÉDIA:" + str(median) + " \n MAIOR:" + str(bigger) + "\n MENOR:" + str(smaller) + "\n\n")
        elif str(bigger) <= str(burn_value):
            print("\n 2º grau: atinge a epiderme e parte da derme (2ª camada da pele). \n Há presença de bolhas, e uma vermelhidão mais intensa e a dor é acentuada;" + str(burn_value))
            print("\n Dados encontrados: \n MÉDIA:" + str(median) + " \n MAIOR:" + str(bigger) + "\n MENOR:" + str(smaller) + "\n\n")
        else:
            print("Não encontramos o seu grau de acordo com os nosso dados, entretando pode ser que após a entrada de mais um dado ele tenha resultado como Grau I ou II\n\n")
      else: 
          print("\n\n Essa é seu primeiro dado em nossa base, faça carregamento de mais dados para obter análises de MÉDIA, MAIOR E MENOR valores!\n")
    





