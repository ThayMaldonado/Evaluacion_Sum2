import requests
from collections import Counter

def descargar_endpoint():
    # Realizar una solicitud GET al endpoint y obtener la respuesta en formato JSON
    response = requests.get("https://dummyjson.com/quotes")
    return response.json()["quotes"]

def obtener_palabras_mas_repetidas():
    palabras = []  # Lista para almacenar todas las palabras de los textos

    # Recorrer cada item en los datos obtenidos del endpoint
    for item in data:
        # Convertir el texto a minúsculas y dividirlo en palabras
        palabras.extend(item["quote"].lower().split())

    palabras_excluir = ["the", "and", "of", "a", "an", "is", "to", "in", "it", "that"]
    # Filtrar las palabras excluyendo artículos y conectores
    palabras_filtradas = [palabra for palabra in palabras if palabra not in palabras_excluir]

    # Obtener el ranking de las palabras más repetidas
    ranking_top_ten = Counter(palabras_filtradas).most_common(10)

    # Imprimir el ranking de las 10 palabras más repetidas
    print("Ranking de las 10 palabras más repetidas (excluyendo artículos y conectores):")
    for palabra, frecuencia in ranking_top_ten:
        print(f"Palabra: {palabra}\tFrecuencia: {frecuencia}")

# Descargar datos del endpoint
data = descargar_endpoint()

# Obtener ranking de palabras más repetidas
obtener_palabras_mas_repetidas()