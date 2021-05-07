# Paint
Repositorio de la SemanaTec para el programa de paint

Iniciamos con el código base de Paint que incluia:
* Dibujar líneas
* Dibujar cuadrados
* Color Negro
* Color Blanco
* Color Verde
* Color azul
* Color rojo

## Agregamos:  
### Daniela Avila Luna: Dibujar Tiangulo y Rectángulo 

#### Códigos
* Dibujar Rectángulo

```python
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
```

* Dibujar Triangulo
```python
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
```

### Liam Garay Monroy: Dibujar Circulo y color amarillo 
 
* Dibujar Circulo
```python
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
```
* Color amarillo
```python
onkey(lambda: color("yellow"), "Y")
```
