"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""
#Importa las librerías a utilizar
from turtle import *
from freegames import vector
from math import tan, hypot

def line(start, end):
    #Define el funcionamiento de la línea 
    up()        #Levanta la pluma de forma que aún no dibuja
    goto(start.x, start.y)      #se dan las coordenas iiciales de la línea
    down()      #baja la pluma para comenzar a dibujar
    goto(end.x, end.y)      #Lleva la pluma a las segundas coordenadas dibujando la línea      

def square(start, end):
    #Define el comportamiento de el cuadrado
    up()        #Levanta la pluma de forma que aún no dibuja
    goto(start.x, start.y)      #se dan las coordenas iniciales de la primera esquina del cuadrado
    down()      #baja la pluma para comenzar a dibujar
    begin_fill()        #Se llama a esta función antes de hacer una figura para que la misma se llene        

    for count in range(4):      #se realiza un for que trazara las cuatro líneas del cuadrado     
        forward(end.x - start.x)        #se avanza la distancia que hay entre el punto de inicio y el punto del final
        left(90)        #se gira 90 grados cada vez que se entra al for, con el fin de que las 4 lineas formen un cuadrado

    end_fill()      #Se termina el llenado de la figura 

def draw_circle(start, end):
    #Dibuja un circulo obteniendo el punto de inicio y el final del mismo utilizándolos como diametro
    lado = round(hypot(end.x - start.x, end.y - start.y))
    radio = lado/2     #Se obtiene la distancia entre el principio y el final del circulo y se divide entre 2 para obtener su radio
    up()        #Levanta la pluma de forma que aún no dibuja
    goto(start.x, start.y)      #se dan las coordenas iniciales del circulo
    down()      #baja la pluma para comenzar a dibujar
    seth(towards(end.x, end.y)-90)     #apunta en la dirección del segundo punto, restando 90° para coincidir con los puntos
    begin_fill()        #Se llama a esta función antes de hacer una figura para que la misma se llene
    circle(radio)       #se llama a esta función con el radio del círculo, lo que permitirá que se dibuje
    end_fill()      #Se termina el llenado de la figura

def rectangle(start, end):
    "Draw rectangle from start to end."
    pass  # TODO

def triangle(start, end):
    "Draw triangle from start to end."
    pass  # TODO

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', draw_circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()