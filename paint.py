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
    radio = (end.x - start.x)/2     
    up()        
    goto(start.x, start.y)      
    down()      
    setheading(270)     
    begin_fill()        
    circle(radio)       
    end_fill()      

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
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()