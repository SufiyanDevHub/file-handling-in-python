#read
# with open ("sample.txt","r") as f:
#     print(f.read())

#read for one line

# with open("sample.txt", "r") as f:
#     line_1 = f.readline()
#     line_2 = f.readline()
#     print(line_1)
#     print(line_2)

with open ("sample.txt","r+")as f:
   
    f.write("Hello i am sufiyan ali")
    print(f.read())