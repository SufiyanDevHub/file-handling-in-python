with open("sample.txt","a") as f:
    f.write(" I am the data without overwrite and the data is written by sufiyan ali")

with open ("doc.txt","a+") as f:
    f.write("I am a+ method of file handling\nI am new line text" )
