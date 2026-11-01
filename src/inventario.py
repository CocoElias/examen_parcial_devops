import requests
import csv

def obtener_datos():
    """Obtiene los datos desde la API REST"""

    url = "https://dummyjson.com/products"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        print("Error al conectar con la API")
        print("Codigo de estado: ", respuesta.status_code)
        return None

def generar_csv(datos):
    """Genera el archivo CSV del inventario"""

    with open("data/inventario.csv", "w")as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["ID", "PRODUCTO", "PRECIO"])

        for producto in datos["products"]:
            escritor.writerow([
                producto["id"],
                producto["title"],
                producto["price"]
            ])
        print("Archivo generado correctamente")

def main():
    datos = obtener_datos()
    if datos:
        generar_csv(datos)

if __name__ == "__main__":
    main()