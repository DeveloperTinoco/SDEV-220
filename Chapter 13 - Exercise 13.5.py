

# Asks user for multiple inputs to see which file they want to edit, which word they want to change and what word they want to replace it with
text_file = input("Enter a file's name: ")
replace_text = input("Enter the string you want to replace in the old file: ")
new_text = input("Enter the string you want to replace the old text with: ")

# Opens the file the user specified and reads it
with open(str(text_file), 'r') as file:
    filetext = file.read()

# Uses the replace() method to set the old word with the new word that the user specified to be replaced
filetext = filetext.replace(str(replace_text), str(new_text))

# Writes to the file with the new given data to replace the old word with the new word specified by the user
with open(str(text_file), 'w') as file:
    file.write(filetext)

# Closes the file
file.close()

# Lets the user know the process is complete and they can check the file
print("The file has been updated.")
