
from tkinter import *
import time
import random



tk = Tk()

tk.title('Game')
tk.resizable(0, 0)

from classes import Ball, Paddle, Score

canvas = Canvas(tk, width=500, height=400, highlightthickness=0)
canvas.pack()

tk.update()

# создаём объект — зелёный счёт
score = Score(canvas, 'green')

# создаём объект — белую платформу

paddle = Paddle(canvas, 'White')

# создаём объект — красный шарик

ball = Ball(canvas, paddle, score, 'red')

# пока шарик не коснулся дна

while not ball.hit_bottom:

    # если игра началась и платформа может двигаться

    if paddle.started == True:
        # двигаем шарик

        ball.draw()

        # двигаем платформу

        paddle.draw()

    # обновляем наше игровое поле, чтобы всё, что нужно, закончило рисоваться

    tk.update_idletasks()

    # обновляем игровое поле, и смотрим за тем, чтобы всё, что должно было быть сделано — было сделано

    tk.update()

    # замираем на одну сотую секунды, чтобы движение элементов выглядело плавно

    time.sleep(0.01)

# если программа дошла досюда, значит, шарик коснулся дна. Ждём 3 секунды, пока игрок прочитает финальную надпись, и завершаем игру

time.sleep(3)