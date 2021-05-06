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
    "Define el funcionamiento de la línea"
    up()        #Levanta la pluma de forma que aún no dibuja
    goto(start.x, start.y)      #se dan las coordenas iiciales de la línea
    down()      #baja la pluma para comenzar a dibujar
    goto(end.x, end.y)      #Lleva la pluma a las segundas coordenadas dibujando la línea      

def square(start, end):
    "Define el comportamiento de el cuadrado"
    up()        #Levanta la pluma de forma que aún no dibuja
    goto(start.x, start.y)      #se dan las coordenas iniciales de la primera esquina del cuadrado
    down()      #baja la pluma para comenzar a dibujar
    begin_fill()        #Se llama a esta función antes de hacer una figura para que la misma se llene        

    for count in range(4):      #se realiza un for que trazara las cuatro líneas del cuadrado     
        forward(end.x - start.x)        #se avanza la distancia que hay entre el punto de inicio y el punto del final
        left(90)        #se gira 90 grados cada vez que se entra al for, con el fin de que las 4 lineas formen un cuadrado

    end_fill()      #Se termina el llenado de la figura 

def draw_circle(start, end):
    "Dibuja un circulo obteniendo el punto de inicio y el final del mismo utilizándolos como diametro"
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
    "Dibuja un rectángulo al dar las coordenadas de inicio y fin con el mouse."
    up()        #Levanta la pluma
    goto(start.x, start.y)      #Va a las coordenadas de inicio
    down()      #Baja la pluma
    begin_fill()        #Comienza a colorear
    
    for lado in range(2):       #Trazará medio rectángulo por iteración
        forward(end.x - start.x)    
        left(90)
        forward(end.y - start.y)        #Aquí llega al segundo punto indicado
        left(90)

    end_fill()      #Termina de colorear

def triangle(start, end):
    "Dibuja un triángulo equilátero al dar las coordenadas de inicio y fin de un lado."
    up()        #Sube lápiz
    goto(start.x, start.y)      #Va a las coordenadas de inicio
    down()      #Baja lápiz
    begin_fill()    #Comienza a colorear
    lado = round(hypot(end.x - start.x, end.y - start.y))   #Mide la longitud del lado con la hipotenusa de un triángulo rectángulo
    seth(towards(end.x, end.y))     #Apunta en la dirección del segundo punto
    for lados in range(3):      #Realiza un triángulo equilátero al girar 120
        forward(lado)
        left(120)
    
    end_fill()      #Termina de colorear
        
def tap(x, y):
    "Almacena las coordenadas cada vez que se de un click en la pantalla"
    start = state['start']      #obtiene el estado actual de state, tipo diccionario

    if start is None:       # Si es None, entonces almacena el valor de las coordenadas de inicio
        state['start'] = vector(x, y)
    else:                   # Si no es None, entonces obtiene la figura a trazar para llamar a esa función
        shape = state['shape']
        end = vector(x, y)      # Almacena las coordenadas del punto de fin
        shape(start, end)       # Se envían las coordenadas de incio y final a la función actualmente seleccionada
        state['start'] = None   # Después de realizar el trazo, actualiza el estado de incio a None.

def store(key, value):
    """
    Almacena la función o figura en un diccionario al momento
    de presionar alguna de las teclas indicadas para los trazos.
    """
    state[key] = value

state = {'start': None, 'shape': line}      # Al momento de inciar el programa, guardará el primer punto y el trazo por default es una línea
setup(420, 420, 370, 0)     # Dimensiones de la ventana
onscreenclick(tap)      # Con cada click, llamará a la función de tap
listen()        #Función que ayudará a tener actualizado la detección de eventos en la ventana.
onkey(undo, 'u')        # Regresa un paso al trazo de la tortuga
onkey(lambda: color('black'), 'K')      # Cambia a color negro con K
onkey(lambda: color('white'), 'W')      # Cambia al color blanco con W
onkey(lambda: color('green'), 'G')      # Cambia al color verde con G
onkey(lambda: color('blue'), 'B')       # Cambia al color azul con B
onkey(lambda: color('red'), 'R')        # Cambia al color rojo con R
onkey(lambda: store('shape', line), 'l')        # Pinta una línea recta con l
onkey(lambda: store('shape', square), 's')      # Pinta un cuadrado con s
onkey(lambda: store('shape', circle), 'c')      # Pinta un círculo con c
onkey(lambda: store('shape', rectangle), 'r')   # Pinta un rectángulo con r
onkey(lambda: store('shape', triangle), 't')    # Pinta un triángulo con t
done()