# Supongamos que deseamos investigar si hay una relación entre el nivel de estrés y el rendimiento académico de los estudiantes de la Universidad "X".
# Recolectamos datos de una muestra aleatoria de 100 estudiantes, registrando su nivel de estrés (bajo, medio, alto) y su rendimiento académico (bajo, medio, alto).

# Hipótesis nula (H0): No hay relación entre el nivel de estrés y el rendimiento académico de los estudiantes de la Universidad "X".
# Hipótesis alternativa (H1): Existe una relación entre el nivel de estrés y el rendimiento académico de los estudiantes de la Universidad "X".

# A continuación, presento un ejemplo utilizando la prueba no paramétrica de chi-cuadrado en Python para analizar esta relación:



# import numpy as np
# from scipy.stats import chi2_contingency

# # Datos de nivel de estrés y rendimiento académico de los estudiantes
# # nivel_estres = np.random.choice(['bajo', 'medio', 'alto'], size=100)
# # rendimiento = np.random.choice(['bajo', 'medio', 'alto'], size=100)
# nivel_estres = ['bajo', 'bajo', 'bajo', 'bajo', 'bajo', 'bajo', 'alto', 'alto', 'alto', 'alto', 'bajo', 'medio', 'alto', 'bajo', 'bajo', 'bajo', 'alto', 'alto', 'alto', 'bajo', 'alto', 'bajo', 'bajo', 'medio', 'bajo', 'bajo', 'bajo', 'bajo', 'medio', 'bajo', 'alto', 'bajo', 'alto', 'alto', 'alto', 'alto', 'medio', 'medio', 'alto', 'medio', 'medio', 'bajo', 'bajo', 'alto', 'medio', 'medio', 'alto', 'medio', 'alto', 'bajo', 'alto', 'bajo', 'medio', 'bajo', 'alto', 'medio', 'alto', 'medio', 'alto', 'alto', 'alto', 'bajo', 'medio', 'alto', 'alto', 'alto', 'alto', 'medio', 'alto', 'bajo', 'alto', 'alto', 'bajo', 'bajo', 'medio', 'bajo', 'bajo', 'medio', 'bajo', 'medio', 'bajo', 'medio', 'alto', 'bajo', 'bajo', 'medio', 'medio', 'medio', 'bajo', 'medio', 'medio', 'medio', 'medio', 'medio', 'bajo', 'medio', 'bajo', 'alto', 'alto', 'alto']


# rendimiento = ['alto', 'alto', 'bajo', 'alto', 'bajo', 'alto', 'medio', 'alto', 'alto', 'medio', 'alto', 'alto', 'medio', 'alto', 'medio', 'medio', 'alto', 'medio', 'bajo', 'bajo', 'alto', 'medio', 'alto', 'alto', 'medio', 'bajo', 'alto', 'bajo', 'alto', 'alto', 'bajo', 'medio', 'alto', 'alto', 'bajo', 'medio', 'alto', 'alto', 'bajo', 'bajo', 'bajo', 'medio', 'medio', 'medio', 'alto', 'alto', 'medio', 'alto', 'bajo', 'medio', 'medio', 'bajo', 'alto', 'bajo', 'medio', 'alto', 'medio', 'bajo', 'medio', 'medio', 'bajo', 'medio', 'bajo', 'alto', 'medio', 'alto', 'bajo', 'medio', 'bajo', 'medio', 'medio', 'alto', 'alto', 'alto', 'alto', 'bajo', 'bajo', 'medio', 'medio', 'medio', 'medio', 'alto', 'bajo', 'alto', 'alto', 'bajo', 'bajo', 'alto', 'medio', 'bajo', 'alto', 'bajo', 'alto', 'alto', 'medio', 'bajo', 'medio', 'medio', 'alto', 'medio']



# # Crear tabla de contingencia
# tabla_contingencia = np.zeros((3, 3))
# for i in range(100):
#     fila = {'bajo': 0, 'medio': 1, 'alto': 2}[nivel_estres[i]]
#     columna = {'bajo': 0, 'medio': 1, 'alto': 2}[rendimiento[i]]
#     tabla_contingencia[fila, columna] += 1


# print(tabla_contingencia)
# # Aplicar la prueba de chi-cuadrado
# estadistico, valor_p, grados_libertad, _ = chi2_contingency(tabla_contingencia)

# # Imprimir los resultados
# print("Estadístico de prueba:", estadistico)
# print("Valor p:", valor_p)
# print("Grados de libertad:", grados_libertad)

# # Tomar la decisión según el nivel de significancia
# nivel_significancia = 0.05
# if valor_p < nivel_significancia:
#     print("Rechazar la hipótesis nula. Existe una relación entre el nivel de estrés y el rendimiento académico.")
# else:
#     print("No se puede rechazar la hipótesis nula. No hay evidencia suficiente para afirmar una relación entre el nivel de estrés y el rendimiento académico.")


# import numpy as np
# from scipy.stats import chi2_contingency
# datos = np.array[
#     [ 2, 98],
#     [ 0, 75],
#     [ 2, 95],
#     [ 1, 100],
#     [ 0, 99],
#     [ 0, 65],
#     [ 0, 64],
#     [ 2, 70],
#     [ 2, 85],
#     [ 1, 74],
#     [ 1, 68],
#     [ 2, 66],
#     [ 2, 71],
#     [ 0, 62],
#     [ 1, 69],
#     [ 1, 84],
#     [ 2, 63],
#     [ 1, 72],
#     [ 2, 67],
#     [ 0, 65],
#  ]

# stat, p, _, _ = chi2_contingency(datos)

# print("Estadística de prueba:", stat)
# print("Valor p:", p)

# nivel_significancia = 0.05
# if p < nivel_significancia:
#     print("Se rechaza la hipótesis nula. Existe una relación entre el rendimiento académico y el IQ.")
# else:
#     print("No se puede rechazar la hipótesis nula. No existe una relación entre el rendimiento académico y el IQ.")


import numpy as np
from scipy.stats import chi2_contingency

# Datos de rendimiento académico
rendimiento = np.array([3, 1, 3, 2, 1, 1, 1, 3, 3, 2, 2, 3, 3, 1, 2, 2, 3, 2, 3, 1])

# Datos de IQ
iq = np.array([98, 75, 95, 100, 99, 65, 64, 70, 85, 74, 68, 66, 71, 62, 69, 84, 63, 72, 67, 65])

# Crear tabla de contingencia
tabla_contingencia = np.histogram2d(rendimiento, iq, bins=(3, 5))[0]
print(tabla_contingencia)

# Realizar la prueba de chi-cuadrado
chi2, p_valor, grados_libertad, _ = chi2_contingency(tabla_contingencia)

# Imprimir los resultados
print("Estadística de prueba:", chi2)
print("Valor p:", p_valor)
print("Grados de libertad:", grados_libertad)

# Tomar la decisión según el nivel de significancia
nivel_significancia = 0.05
if p_valor < nivel_significancia:
    print("Rechazar la hipótesis nula. Existe una relación entre el grado de IQ y el rendimiento académico.")
else:
    print("Aceptar la hipótesis nula. No hay suficiente evidencia para concluir que hay una relación entre el grado de IQ y el rendimiento académico.")
