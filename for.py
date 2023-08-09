datos = {
    "name": "eder",
    "edad": 23,
    "gustos": [
        "altas",
        "rubias",
        "delgadas"
    ]
}

amount_gustos = len(datos["gustos"])

#method 1
for e in datos["gustos"]:
    print(f"me gustan {e}")

#method 2
for i in range(amount_gustos):
    print(datos["gustos"][i], "i like it")
