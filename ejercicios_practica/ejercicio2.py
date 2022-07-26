# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json
import requests

import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"
    respuesta = requests.get(url)
    datos = respuesta.json()

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".


    # Alumno, de cada usuario en el total de las 200 entradas
    # debe contar cuantos títulos completó cada usuario (de los 10 posibles)
    # y armar un gráfico de barras resumiendo la información.
    # gráfico en el eje "x" está cada uno de los 10 usuarios y en el eje
    # "y" la cantidad de títulos completados.

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.
    
    
    usuarios_x = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]
    completo_y = []
    
    completos_1 = 0
    completos_2 = 0
    completos_3 = 0
    completos_4 = 0
    completos_5 = 0
    completos_6 = 0
    completos_7 = 0
    completos_8 = 0
    completos_9 = 0
    completos_10 = 0
    
    for usuario in datos:
        if usuario['userId'] == 1 and usuario['completed'] == True:
            completos_1 += 1

        elif usuario['userId'] == 2 and usuario['completed'] == True:
            completos_2 += 1

        elif usuario['userId'] == 3 and usuario['completed'] == True:
            completos_3 += 1

        elif usuario['userId'] == 4 and usuario['completed'] == True:
            completos_4 += 1

        elif usuario['userId'] == 5 and usuario['completed'] == True:
            completos_5 += 1

        elif usuario['userId'] == 6 and usuario['completed'] == True:
            completos_6 += 1

        elif usuario['userId'] == 7 and usuario['completed'] == True:
            completos_7 += 1

        elif usuario['userId'] == 8 and usuario['completed'] == True:
            completos_8 += 1

        elif usuario['userId'] == 9 and usuario['completed'] == True:
            completos_9 += 1

        elif usuario['userId'] == 10 and usuario['completed'] == True:
            completos_10 += 1   
        
    completo_y.append(completos_1)
    completo_y.append(completos_2)
    completo_y.append(completos_3)
    completo_y.append(completos_4)
    completo_y.append(completos_5)
    completo_y.append(completos_6)
    completo_y.append(completos_7)
    completo_y.append(completos_8)
    completo_y.append(completos_9)
    completo_y.append(completos_10)

           
    # Debe poder graficar dicha información en un gráfico de barras.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.

    fig = plt.figure()
    fig.suptitle('Libros completados por usuario', fontsize=14)
    ax = fig.add_subplot()
    ax.bar(usuarios_x, completo_y, label='leídos completos')
    ax.set_facecolor('whitesmoke')
    ax.set_xlabel("User Id")
    ax.set_ylabel("Completed")
    ax.grid(ls='dashdot')
    ax.legend()
    plt.xticks(usuarios_x)
    plt.show()

    print("terminamos")