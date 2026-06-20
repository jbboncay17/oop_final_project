from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPACE_SIZE = 40
BODY_PARTS = 3

SNAKE_COLOR = "#32CD32"
HEAD_COLOR = "#7CFC00"
FOOD_COLOR = "#FF4444"
BACKGROUND_COLOR = "#111111"


class Snake:

    def __init__(self):
        self.coordinates = []

        for i in range(BODY_PARTS):
            self.coordinates.append([0, 0])


class Food:

    def __init__(self):

        self.coordinates = [
            random.randint(0, GAME_WIDTH // SPACE_SIZE - 1) * SPACE_SIZE,
            random.randint(0, GAME_HEIGHT // SPACE_SIZE - 1) * SPACE_SIZE
        ]


def draw_snake(snake):

    canvas.delete("snake")

    for i, (x, y) in enumerate(snake.coordinates):

        color = HEAD_COLOR if i == 0 else SNAKE_COLOR

        canvas.create_oval(
            x,
            y,
            x + SPACE_SIZE,
            y + SPACE_SIZE,
            fill=color,
            outline="#228B22",
            width=2,
            tag="snake"
        )


        if i == 0:


            canvas.create_oval(
                x + 10, y + 10,
                x + 15, y + 15,
                fill="black",
                tag="snake"
            )

            canvas.create_oval(
                x + 25, y + 10,
                x + 30, y + 15,
                fill="black",
                tag="snake"
            )


            canvas.create_arc(
                x + 10, y + 18,
                x + 30, y + 32,
                start=180,
                extent=180,
                style=ARC,
                outline="black",
                width=2,
                tag="snake"
            )



def draw_food(food):

    canvas.delete("food")

    x, y = food.coordinates

    canvas.create_oval(
        x,
        y,
        x + SPACE_SIZE,
        y + SPACE_SIZE,
        fill=FOOD_COLOR,
        outline="#AA0000",
        tag="food"
    )



def next_turn(snake, food):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, [x, y])


    if [x, y] == food.coordinates:

        global score
        score += 1
        label.config(text=f"Score: {score}")

        food = Food()

    else:
        snake.coordinates.pop()

    draw_snake(snake)
    draw_food(food)

    if check_collisions(snake):
        game_over()
    else:
        window.after(150, next_turn, snake, food)


def change_direction(new_direction):

    global direction

    if new_direction == "left" and direction != "right":
        direction = new_direction
    elif new_direction == "right" and direction != "left":
        direction = new_direction
    elif new_direction == "up" and direction != "down":
        direction = new_direction
    elif new_direction == "down" and direction != "up":
        direction = new_direction


def check_collisions(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    if y < 0 or y >= GAME_HEIGHT:
        return True

    for body in snake.coordinates[1:]:
        if [x, y] == body:
            return True

    return False


def game_over():

    canvas.delete(ALL)

    canvas.create_text(
        GAME_WIDTH / 2,
        GAME_HEIGHT / 2 - 30,
        text="GAME OVER",
        fill="red",
        font=("Consolas", 60, "bold")
    )

    canvas.create_text(
        GAME_WIDTH / 2,
        GAME_HEIGHT / 2 + 40,
        text="HINDI KA NA MAANGAS",
        fill="red",
        font=("Consolas", 25, "bold")
    )


window = Tk()
window.title("Snake Game - Final Version")
window.resizable(False, False)

score = 0
direction = "down"

label = Label(window, text=f"Score: {score}", font=("Consolas", 30))
label.pack()

canvas = Canvas(window, width=GAME_WIDTH, height=GAME_HEIGHT, bg=BACKGROUND_COLOR)
canvas.pack()

snake = Snake()
food = Food()

window.bind("<Left>", lambda e: change_direction("left"))
window.bind("<Right>", lambda e: change_direction("right"))
window.bind("<Up>", lambda e: change_direction("up"))
window.bind("<Down>", lambda e: change_direction("down"))

next_turn(snake, food)
window.mainloop()