# En 90 pacientes se probó un nuevo medicamento y 10 de ellos no se curaron en el plazo previsto. La idea es aceptar la droga si logra mejoría en el 75% de los casos. ¿Qué decisión se debe tomar a la luz de estos resultados experimentales?
#Se instala la biblioteca spyci que pesa 36mb, desintalar luego, esta en pyenv pruebas

# from scipy.stats import fisher_exact

# # Definir los datos del ejercicio
# total_pacientes = 90
# no_curados = 10

# # Calcular los valores para la prueba de Fisher
# curados = total_pacientes - no_curados
# umbral = 0.75 * total_pacientes

# # Realizar la prueba exacta de Fisher
# odds_ratio, p_value = fisher_exact([[curados, no_curados], [umbral, total_pacientes - umbral]])

# # Imprimir los resultados
# print("Odds ratio:", odds_ratio)
# print("Valor p:", p_value)

# # Interpretación de los resultados
# if p_value < 0.05:
#     print("Hay una diferencia significativa en la proporción de pacientes curados.")
#     if curados >= umbral:
#         print("Se puede aceptar el nuevo medicamento.")
#     else:
#         print("No se debe aceptar el nuevo medicamento.")
# else:
#     print("No hay una diferencia significativa en la proporción de pacientes curados.")
#     print("No se debe aceptar el nuevo medicamento.")




# from scipy.stats import binomtest

# # Datos del experimento
# n = 90  # Número total de pacientes
# x = n-10  # Número de pacientes que no se curaron

# # Parámetro bajo la hipótesis nula
# p_null = 0.75

# # Realizar el test de hipótesis utilizando la función binomtest()
# result = binomtest(x, n, p_null)

# # Obtener el valor p del resultado del test
# p_value = result.pvalue

# # Imprimir el valor p
# print("Valor p:", p_value)



# # Interpretación de los resultados
# n_significancia = 0.05

# if p_value < n_significancia:
#     print("Se rechaza la hipótesis nula. No se acepta la nueva droga.")
# else:
#     print("No se puede rechazar la hipótesis nula. Se acepta la nueva droga.")

# numero_notacion_cientifica = 2.2983750242646814e-37
# numero_flotante = float(numero_notacion_cientifica)
# print(format(numero_notacion_cientifica, '.40f'))

# from scipy.stats import wilcoxon

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



# Ejercicio de la unheval n1

# from scipy.stats import wilcoxon

# # Calificaciones de los estudiantes del grupo A
# grupo_a = [15, 17, 12, 14, 16, 18, 13, 11, 15, 16, 19, 14, 17, 15, 16, 12, 13, 15, 16, 14]

# # Calificaciones de los estudiantes del grupo B
# grupo_b = [13, 14, 15, 12, 13, 16, 17, 15, 14, 12, 16, 15, 14, 17, 13, 12, 15, 16, 13, 14]

# # Aplicar la prueba de Wilcoxon
# estadistica, valor_p = wilcoxon(grupo_a, grupo_b, alternative='two-sided')

# # Imprimir los resultados
# print("Estadística de prueba:", estadistica)
# print("Valor p:", valor_p)

# # Tomar la decisión según el nivel de significancia
# nivel_significancia = 0.05
# if valor_p < nivel_significancia:
#     print("Rechazar la hipótesis nula. Existe una diferencia en el rendimiento académico entre los grupos A y B.")
# else:
#     print("No se puede rechazar la hipótesis nula. No hay diferencia en el rendimiento académico entre los grupos A y B.")


from scipy.stats import kruskal

# Calificaciones de los estudiantes del grupo A
grupo_a = [15, 17, 12, 14, 16, 18, 13, 11, 15, 16, 19, 14, 17, 15, 16, 12, 13, 15, 16, 14]

# Calificaciones de los estudiantes del grupo B
grupo_b = [13, 14, 15, 12, 13, 16, 17, 15, 14, 12, 16, 15, 14, 17, 13, 12, 15, 16, 13, 14]

# Aplicar la prueba de Kruskal-Wallis
estadistica, valor_p = kruskal(grupo_a, grupo_b)

# Imprimir los resultados
print("Estadística de prueba:", estadistica)
print("Valor p:", valor_p)

# Tomar la decisión según el nivel de significancia
nivel_significancia = 0.05
if valor_p < nivel_significancia:
    print("Rechazar la hipótesis nula. Existe una diferencia en el rendimiento académico entre los grupos A y B.")
else:
    print("No se puede rechazar la hipótesis nula. No hay diferencia en el rendimiento académico entre los grupos A y B.")
