# Sistema de Inventario Automatizado con API REST

## Descripción

Proyecto desarrollado para el curso de Fundamentos de DevOps.

La aplicación consume datos desde una API REST utilizando el protocolo HTTPS, procesa la información en formato JSON y genera un archivo CSV con el inventario de productos obtenidos.

## Objetivos

- Consumir datos desde una API REST segura.
- Procesar información en formato JSON.
- Generar reportes en formato CSV.
- Aplicar buenas prácticas de programación en Python.
- Utilizar Git y GitHub para el control de versiones.
- Aplicar comandos fundamentales de Linux para la administración de usuarios, grupos y permisos.

## Tecnologías Utilizadas

- Linux
- Python 3
- Git
- GitHub
- REST API
- JSON
- CSV
- Requests

## Estructura del Proyecto

```text
examen_parcial/
│
├── data/
│   └── inventario.csv
│
├── docs/
│
├── src/
│   └── inventario.py
│
└── README.md
```

## Funcionalidades

- Consumo de una API REST mediante HTTPS.
- Procesamiento de datos JSON.
- Generación de archivos CSV.
- Manejo básico de errores HTTP.
- Código organizado mediante funciones.
- Control de versiones con Git y GitHub.

## Instalación

Instalar la librería requerida:

```bash
pip install requests
```

## Ejecución

Ejecutar el programa con:

```bash
python3 src/inventario.py
```

## Resultado Esperado

El sistema genera el archivo:

```text
data/inventario.csv
```

que contiene información de los productos obtenidos desde la API.

## Repositorio GitHub

Repositorio del proyecto:

https://github.com/CocoElias/examen_parcial_devops

## Autor

Proyecto desarrollado como parte del curso Fundamentos de DevOps.
