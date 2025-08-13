# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Aprenderás a crear una API REST básica utilizando el framework FastAPI en Python. El objetivo es que los estudiantes comprendan los conceptos fundamentales de las APIs, rutas, métodos HTTP y manejo de datos con FastAPI.

## 📝 Tasks

### 🛠️ Crear un endpoint GET para listar elementos

#### Description
Crea un endpoint `/items` que devuelva una lista de elementos (puede ser una lista de diccionarios con nombre y precio).

#### Requirements
Completed program should:

- Definir una ruta `/items` que responda a solicitudes GET
- Retornar una lista de al menos 3 elementos con nombre y precio
- Usar el decorador adecuado de FastAPI


### 🛠️ Crear un endpoint POST para agregar un elemento

#### Description
Permite a los usuarios agregar un nuevo elemento enviando un JSON con nombre y precio a la ruta `/items`.

#### Requirements
Completed program should:

- Definir una ruta `/items` que acepte solicitudes POST
- Recibir un JSON con los campos `name` y `price`
- Agregar el nuevo elemento a la lista y devolverlo como respuesta
