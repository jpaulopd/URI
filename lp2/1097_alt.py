lista = []
j_inicial = 7
for i in range (1, 10 , 2):
    lista.append(i)
    lista.append(j_inicial)
    j_inicial += 2

for x in range(0, len(lista), 2 ):
    i = lista[x]
    j = lista[x+1]
    for y in range(3):
        print('I={} J={}'.format(i,j))
        j -= 1