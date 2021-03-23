

from tkinter import *


class racingCar:

    def __init__(self):

        # Create GUI window
        window = Tk()
        window.title("Car Racing")
        window.geometry("600x400")

        # Set variables for positioning purposes
        w = 600
        h = 400
        x = w//2
        y = h//2

        # Create canvas
        self.canvas = Canvas(window, width=w, height=h, bg="white")
        self.canvas.pack()

        # Draw car on canvas
        wheel_1 = self.canvas.create_oval(
            x, y, x+10, y+10, fill="black", tags="W1")
        wheel_2 = self.canvas.create_oval(
            x+30, y,  x+20, y+10, fill="black", tags="W2")
        body = self.canvas.create_rectangle(
            x-10, y-20, x+40, y-1, fill="grey", tags="Body")
        roof = self.canvas.create_polygon(
            x, y-20, 310, 170, 325, 170, 335, 180, x, y-20, tags="Roof")

        # Create event listener for right movement using up arrow key
        def right(event):
            x = 10
            y = 0
            self.canvas.move(wheel_1, x, y)
            self.canvas.move(wheel_2, x, y)
            self.canvas.move(body, x, y)
            self.canvas.move(roof, x, y)

        # Create event listener for left movement using down arrow key
        def left(event):
            x = -10
            y = 0
            self.canvas.move(wheel_1, x, y)
            self.canvas.move(wheel_2, x, y)
            self.canvas.move(body, x, y)
            self.canvas.move(roof, x, y)

        # Binds keys to functions
        window.bind("<Up>", right)
        window.bind("<Down>", left)

        window.mainloop()


racingCar()
