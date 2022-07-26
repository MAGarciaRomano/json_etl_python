# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json


def serializar():
    print("Funcion que genera un archivo JSON")
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede inventar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    # json_data = {...}
    jason_data = {
                 "nombre": "Soledad",
                 "apellido": "Romano",
                 "DNI": "29.148.237",
                 "vestidor": [
                    {
                     "prenda": "zapatos",
                     "cantidad": 9
                    },
                    {
                     "prenda": "camisas",
                     "cantidad": 6
                    }
                    ]
                 }

    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina.
    with open('practica_1_json.json', 'w') as jsonfile:
        datos_prendas = [jason_data]
        json.dump(datos_prendas, jsonfile, indent=4)

    # Observe el archivo y verifique que se almaceno lo deseado.


def deserializar():
    print("Funcion que lee un archivo JSON")
    # JSON Deserialize
    # Basado en la función  anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()
    with open('practica_1_json.json', 'r') as jsonfile:
        contenido_datos_prendas = json.load(jsonfile)
        
    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en la función anterior
    print('¿Qué hay adentro del archivo practica_1_json?')
    print(json.dumps(contenido_datos_prendas, indent=4))


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    serializar()
    deserializar()

    print("terminamos")