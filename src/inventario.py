import requests
import csv

url = "https://dummyjson.com/products"

respuesta = requests.get(url)

if respuesta.status_code == 200:
    datos = respuesta.json()
    with open("data/inventario.csv", "w", newline="", encoding="utf-8")as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["ID","Producto","Precio"])
        for producto in datos["products"]:
            escritor.writerow([
                producto["id"],
                producto["title"],
                producto["price"]
            ])

        print ("Archivo CSV generado correctamente")
else:
    print("Error al conectar con la API")
    print("Codigo de estado: ", respuesta.status_code)