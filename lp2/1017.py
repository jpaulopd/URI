tempo_horas = int(input())

vel_media = int(input())

consumo_km_litros = 12

distancia = tempo_horas * vel_media

litros_necessarios = distancia / consumo_km_litros

print("{:.3f}".format(litros_necessarios))
