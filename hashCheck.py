with open("check.txt","r") as textfile:
    content = textfile.readlines()
    hashToCheck = content[435:-49]
    print("Found hash on website: ", hashToCheck)
with open("generatedHash.txt", "r") as generatedHash:
    compare = generatedHash.readlines()
    if hashToCheck == compare:
        print("Hashes match.")
    else:
        print("Hashes dont yet match.")