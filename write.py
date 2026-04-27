# with open("sample.txt","w") as f:

#     f.write(" Hello i am overwrite data and the data is written by sufiyan")

with open("sample.txt","w+") as f:
    f.write("I am Abdul Rehman")

with open("test.txt","w+") as f:
    f.write("I am a new file by creating a python code")