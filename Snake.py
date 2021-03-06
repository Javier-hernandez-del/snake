from turtle import *
from random import randrange
from random import shuffle
from freegames import square 
from freegames import vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
# Sección de colores usados por la serpiente y la comida cada vez que se reinicia el juego.
colors = ["green","blue","orange","black","pink"]
shuffle(colors)

def change(x, y):  # Función que permite mover a la serpiente
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):  # Función mejorada para que el snake y la comida se queden en el tablero.
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190
def insidef(food):
    "Return True if head inside boundaries."
    return -190 < food.x < 180 and -190 < food.y < 180

def move():  # Función que le permite al usuario mover a la serpiente con las teclas de dirección.
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
    clear()

    for body in snake:
        square(body.x, body.y, 9, colors[0])
        square(food.x, food.y, 9, colors[1]) 
    # If para que la comida se mueva aleatoriamente
    if insidef(food):
        food.x = food.x + randrange(-1,2) * 10
        food.y = food.y + randrange(-1,2) * 10
    else:
        if food.x > 170: food.x = 170
        elif food.x < -180: food.x = -180
        if food.y > 170: food.y = 170
        elif food.y < -180: food.y = -180
    update()
    ontimer(move, 100)

# Parámetros del juego.
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()