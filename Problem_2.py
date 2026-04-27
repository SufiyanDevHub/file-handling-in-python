with open ("problem.txt","r") as f:
    data = f.read()
    data = data.replace("python","java")

with open ("problem.txt","w") as f:
    f.write(data)
