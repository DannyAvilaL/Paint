"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""

# Código modificado
# Autor: Daniela Avila Luna    A01378664
# Autor: Liam Garay Monroy     A01750632

# Importa las librerías a utilizar
from turtle import *
from freegames import vector
from math import tan, hypot


def line(start, end):
    """Define el funcionamiento de la línea."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Define el comportamiento de el cuadrado."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # se realiza un for que trazara las cuatro líneas del cuadrado
    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def draw_circle(start, end):
    """Dibuja un circulo obteniendo el punto de inicio y
    el final del mismo utilizándolos como diametro.casefold()"""
    lado = round(hypot(end.x - start.x, end.y - start.y))
    radio = lado / 2
    up()
    goto(start.x, start.y)
    down()
    seth(towards(end.x, end.y) - 90)
    begin_fill()
    circle(radio)
    end_fill()


def rectangle(start, end):
    """Dibuja un rectángulo al dar las coordenadas
    de inicio y fin con el mouse."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    seth(0)

    for lado in range(2):  # Trazará medio rectángulo por iteración
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()


def triangle(start, end):
    """Dibuja un triángulo equilátero al dar las coordenadas
    de inicio y fin de un lado."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    # Mide la longitud del lado con la hipotenusa de un triángulo rectángulo
    lado = round(hypot(end.x - start.x, end.y - start.y))
    seth(towards(end.x, end.y))  # Apunta en la dirección del segundo punto

    for lados in range(3):  # Realiza un triángulo equilátero al girar 120
        forward(lado)
        left(120)

    end_fill()  # Termina de colorear


def tap(x, y):
    """Almacena las coordenadas cada vez que se de un click en la pantalla."""
    start = state["start"]

    if start is None:
        state["start"] = vector(x, y)
    else:
        shape = state["shape"]
        end = vector(x, y)
        shape(start, end)
        state["start"] = None


def store(key, value):
    """
    Almacena la función o figura en un diccionario al momento
    de presionar alguna de las teclas indicadas para los trazos.
    """
    state[key] = value


state = {"start": None, "shape": line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, "u")

# Cambia de color dependiendo la tecla presionada
onkey(lambda: color("black"), "K")
onkey(lambda: color("white"), "W")
onkey(lambda: color("green"), "G")
onkey(lambda: color("blue"), "B")
onkey(lambda: color("red"), "R")
onkey(lambda: color("yellow"), "Y")

# Cambia de dirección dependiendo la tecla presionada
onkey(lambda: store("shape", line), "l")
onkey(lambda: store("shape", square), "s")
onkey(lambda: store("shape", draw_circle), "c")
onkey(lambda: store("shape", rectangle), "r")
onkey(lambda: store("shape", triangle), "t")

done()
