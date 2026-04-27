try:
    with open("doc.txt", "r") as f:
        data = f.read()
    print("File exists")
except FileNotFoundError:
    print("File does not exist")