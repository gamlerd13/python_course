datos = {
    "name": "eder",
    "edad": 30,
    "gustos": [
        "futbol",
        "natacion",
        "basquetball"
    ]
}

amount_gustos = len(datos["gustos"])

#method 1
for e in datos["gustos"]:
    print(f"me gusta el/la {e}")

#method 2
for i in range(amount_gustos):
    print(datos["gustos"][i], "i like it")
