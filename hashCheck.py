with open("check.txt","r") as textfile:
    content = textfile.read()
    hashToCheck = content[436:-88]
    print("Found hash on website: ", hashToCheck)
with open("generatedHash.txt", "r") as generatedHash:
    compare = generatedHash.read()
    print("Hash to compare to:    ", compare)
    if hashToCheck == compare:
        print("Hashes match.")
    else:
        print("Hashes dont yet match.")