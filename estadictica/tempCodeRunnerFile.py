from scipy.stats import wilcoxon

# # Edades de los pacientes del primer hospital (población completa)
# edades_poblacion = [57] * 90
# print(edades_poblacion)

# # Edades de los pacientes del segundo hospital (muestra)
# edades_muestra = [26, 90, 44, 67, 12, 34, 67, 66, 24, 49, 45, 15, 58, 77, 57]

# # Aplicar la prueba de Wilcoxon
# estadistica, valor_p = wilcoxon(edades_poblacion, edades_muestra, alternative='two-sided')

# # Imprimir los resultados
# print("Estadística de prueba:", estadistica)
# print("Valor p:", valor_p)

# # Tomar la decisión según el nivel de significancia
# nivel_significancia = 0.05
# if valor_p < nivel_significancia:
#     print("Rechazar la hipótesis nula. Las medianas de edad son diferentes en ambos centros.")
# else:
#     print("No se puede rechazar la hipótesis nula. Las medianas de edad son las mismas en ambos centros.")
