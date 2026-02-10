import numpy as np

# 1
np.sum(notas_mates)

# 2
media_mates = np.mean(notas_mates)

# 3
aprobados_mates = notas_mates >= 5
alumnos[aprobados_mates]

# 4
superior_media_mates = notas_mates > media_mates
alumnos[superior_media_mates]

# 5
notas_5_mas_1 = np.where(notas_mates > 5, notas_mates + 1, notas_mates)

# 6
notas_mates_6 = np.where(notas_mates > 5, notas_mates + 2, notas_mates * 1)

# 7
array_abs = np.abs(array_float)

# 8
notas_mates_10 = notas_mates.copy()
notas_mates_10[alumnos == "Pedro"] = 10
# Mejor usar where

# 9
