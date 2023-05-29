import requests
import csv

def descargar_endpoint():
    url = "https://dummyjson.com/quotes"
    response = requests.get(url)
    data = response.json()["quotes"]
    return data

def guardar_en_archivo(data):
    filename = "endpoint.csv"
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter="\t")
        writer.writerow(["autor", "texto"])  # Escribir los encabezados en la primera fila
        for item in data:
            writer.writerow([item["author"], item["quote"]])  # Escribir los valores de autor y texto en una fila
    print("Datos guardados en el archivo", filename)

# Descargar datos del endpoint
data = descargar_endpoint()

# Guardar datos en un archivo CSV
guardar_en_archivo(data)


