"""
CONSTANTES = "Variaveis" que não mudam
Muitas condicoes no mesmo if (ruim)
         <- contagem de complexidade(ruim)
"""
velocidade = 60 # Velocidade atuial do carro
local_carro = 98 #Local em que o carro está na estrada

#CONSTANTES LETRA MAIUSCULA
RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distancia onde o radar pega

if velocidade > RADAR_1:
    print('Velocidade maior que o RADAR 1')

if local_carro >= RADAR_1:
    print('Carro passou radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 - RADAR_RANGE) and \
    velocidade >= RADAR_1:
    print('Velocidade do carro multado')