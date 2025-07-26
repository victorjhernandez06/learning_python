"""Arreglo multidimensional"""
long = 45.6
lat = 34.5
posicion = [lat, long]

historial = [
    [35.4, 23.4, '2025/07/23 17:30:39'],
    [34.4, 22.4, '2025/07/24 17:30:39'],
    [33.4, 20.4, '2025/07/27 17:30:39'],
    [32.4, 29.4, '2025/07/26 17:30:39'],
    [33.4, 27.4, '2025/07/28 17:30:39'],
    [39.4, 26.4, '2025/07/29 17:30:39'],
    [35.4, 25.4, '2025/07/30 17:30:39'],
    [37.4, 24.4, '2025/07/32 17:30:39'],
    [35.4, 23.4, '2025/07/31 17:30:39'],
    [33.4, 23.4, '2025/07/36 17:30:39'],
]
print(historial[0])
print(historial[0][0])
print(historial[0][1])
print(historial[0][2])

indiceLongitud = 0
indiceLatitud = 1
indicefecha = 2

print(historial[3][indicefecha])
print(historial[3][indiceLongitud])
for coordenada in historial:
    print(coordenada)

print(historial[indiceLatitud])


