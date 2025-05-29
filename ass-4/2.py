user_input=input("Enter the text you want to write in the file: ")
with open("output.txt","w")as file:
    file.write(user_input)
user_append=input("Enter the text you want to append in the file: ")
with open("output.txt","a")as file:
    file.write(user_append)
with open("output.txt","r") as file:
    fi=file.read()
print(fi)