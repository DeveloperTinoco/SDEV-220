

from tkinter import *


class geometricFig:

    def __init__(self):

        # Creates GUI
        window = Tk()
        window.title("Geometric Figures")

        # Creates and packs the canvas within the GUI
        self.canvas = Canvas(window, width=200, height=200, bg="white")
        self.canvas.pack()

        # Creates a frame and packs it within the instance of the GUI
        frame = Frame(window)
        frame.pack()

        # Creates variables for each shape to be referenced to
        self.v1 = StringVar()
        self.v1.set("1")
        self.v2 = StringVar()
        self.v2.set("0")

        # Creates the radio buttons for either shape that executes a function when pressed
        rbTriangle = Radiobutton(
            frame, text="Triangle", command=self.optionChanged, variable=self.v1, value='1')
        rbDiamond = Radiobutton(
            frame, text="Diamond", command=self.optionChanged, variable=self.v1, value='2')

        # Creates a check button for the "fill" option that executes a function when pressed
        cbtFill = Checkbutton(frame, text="Fill",
                              command=self.optionChanged, variable=self.v2)

        # Places the buttons into their proper position
        rbTriangle.grid(row=1, column=1)
        rbDiamond.grid(row=1, column=2)
        cbtFill.grid(row=1, column=3)

        # Begins each instance of the program
        window.mainloop()

    # Creates function that is called when the buttons are pressed
    def optionChanged(self):

        # Deletes the fill of whatever shape is currently selected when check button is pressed
        self.canvas.delete("Diamond", "Triangle")
        color = "white" if self.v2.get() == "0" else "blue"

        # Redraws each shape whenever the radio buttons are changed
        if self.v1.get() == '1':
            self.canvas.create_polygon(
                55, 85, 155, 85, 105, 180, 55, 85, tags="Triangle", fill=color, outline="blue")
        else:
            self.canvas.create_polygon(
                55, 85, 105, 5, 155, 85, 105, 180, 55, 85, tags="Diamond", fill=color, outline="blue")


geometricFig()
