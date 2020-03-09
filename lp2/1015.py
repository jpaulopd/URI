import math

ponto1 = input()
ponto2 = input()

ponto1 = ponto1.split() #['1.0', '7.0']
ponto2 = ponto2.split() #['5.0','9.0']

x1 = float(ponto1[0])
y1 = float(ponto1[1])

x2 = float(ponto2[0])
y2 = float(ponto2[1])

# Distância euclidiana

d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("{:.4f}".format(d))
