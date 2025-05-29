try:
    with open("file.txt","r") as file:
        reading_file=file.read()
except FileNotFoundError:
    print("Error: The file 'file.txt' does not exist.")

