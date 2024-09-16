
try:
    with open("file_create.txt", "w") as file:
        #writelines accepts a list (so square brackets with "," as a separtor)
        file.writelines(["\nUsing \nNewline \nCharacters", "\nWritelines accepts a list or an array of strings",    "\nCheck the code out on creating_files.py"])
except FileNotFoundError as e:
    print("Can't locate file.", e)
    #in Line 3, within the with open(), if you put sample/file_create.txt it will throw this error because there is no sample directory
