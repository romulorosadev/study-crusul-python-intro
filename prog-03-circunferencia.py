# PROBLEMA:
# Calcular e exibir o comprimento e área de circunferência, apenas com a entrada do valor de raio


# MEU RACIONAL 
# 1) Importar a bibliteca math pra utilizar suas funções
# 2) Solicitar a entrada de dados de raio 
# 3) Com base em raio calcular a área
# 4) Com base em raio calcular o comprimento
# 5) Exibir os dados de área e comprimento

#1
import math

#2
inRaio = float(input("Informe o valor de um raio de circunferência em cm: "))

#3
outArea = math.pi * math.pow(inRaio,2)
#4
outComprimento = 2 * math.pi * inRaio

#5
print("CIRCUNFERÊNCIA")
print("Área:", outArea)
print("Comprimento:", outComprimento)