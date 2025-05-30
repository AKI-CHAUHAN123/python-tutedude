name = {"Ankit": 22, "Nitin": 88, "Ashish": 89, "Aditya": 77}

try:
    e = input("Enter the name of Student: ")
    print(name[e])
except:
    print("Student not found")