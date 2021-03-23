

# Creates a counter that will keep track of the ten allowed numbers per line
counter = 0

# Loops through the numbers 200-400
for i in range(200, 401):

    # Finds the numbers that are divisible by 7 but not by 8
    if (i % 7 == 0) and not (i % 8 == 0):

        # Increments the counter if a number meets the requirements and prints it for the user to see with 10 numbers per line
        counter += 1
        print(i, end=(" " if counter < 10 else "\n"))

        # Resets the counter once it hits 10
        if counter == 10:
            counter = 0
