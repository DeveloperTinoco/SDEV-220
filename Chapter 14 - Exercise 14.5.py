# THIS PROGRAM WAS SUPPOSED TO EMBED THE GRAPH INTO THE TKINTER WINDOW BUT I DID NOT DO THAT PORTION OF THE ASSIGNMENT SO FEEL FREE TO ATTEMPT IT YOURSELF

from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import matplotlib.pyplot as plt

# Creates the global empty dictionary that will hold the letters that appear and how many times they appear in the text file that the user selects
data = {}

# A function that makes every letter in the text file lowercase so that the uppercase and lowercase versions of the same letter will be counted as one single letter


def lowerCase(letter):
    return letter.lower()

# Function that is run when the "Open" button is clicked to allow the user to select a file


def openFile():

    # Brings in the global 'data' variable so that we may use it here
    global data

    # Resets the dictionary to an empty dictionary each time the user wants to select a new file
    data = {}

    # Opens the user's file explorer so that they may select a .txt file for the program to read
    file = askopenfile(mode='r', filetypes=[('Python Files', '*.txt')])

    # Reads the file if the user selects one or tells the user that the file they selected does not exist or they didn't select a file at all
    if file is not None:
        content = file.read()

        # Loops through every character of the .txt file's contents
        for letter in content:

            # Only checks if the character is a letter from a-z
            if letter.isalpha():

                # If the character is a letter, the program sends the letter to the lowerCase() function
                lowerletter = lowerCase(letter)

                # Adds the key value pair to the 'data' dictionary and adds each occurance of each key (letter that is present) to their corresponding values (how many times this particular key appears)
                if lowerletter in data.keys():
                    data[lowerletter] += 1
                else:
                    data[lowerletter] = 1

            # If the character is not a letter, the program just moves on to check the next character
            else:
                continue
    else:
        print("You need to either actually select a file or the file you have chosen does not exist.")

    return data

# A function that creates the histogram that visually displays the data in the 'data' dictionary


def createHistogram():
    global data

    # Sorts the 'data' dictionary into list of tuples in alphabetical order & then creates a new dictionary with that same information
    orderedData = sorted(data.items())
    newDict = dict(orderedData)

    # Labels the graph and passes the 'keys' and 'values' into the graph so that it can be correctly displayed
    plt.xlabel("Letters That Are Present In File")
    plt.ylabel("Occurance Per Letter")
    plt.bar(newDict.keys(), newDict.values(), width=.5, color='blue')
    plt.show()


# Runs the program
if __name__ == "__main__":

    # Creates the main instance of the Tkinter window, labels the title and sets the size of the window
    root = Tk()
    root.title("Occurence Of Letters In Histogram")
    root.geometry('500x300')

    # Creates two buttons that perform their corresponding functions
    openbtn = Button(root, text='Open', command=lambda: openFile())
    openbtn.place(x=150, y=125)
    createbtn = Button(root, text='Show Result',
                       command=lambda: createHistogram())
    createbtn.place(x=275, y=125)

    root.mainloop()
