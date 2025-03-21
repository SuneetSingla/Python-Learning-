# replace the word "donkey" with "######" in a file named donkeyfile.txt


word = "donkey"

with open("donkeyfile.txt", "r") as f:
    content = f.read()

newcontent = content.replace(word, "######")

with open("donkeyfile.txt", "w" ) as f:
    f.write(newcontent)
    f.close()

print("The word has been replaced successfully")