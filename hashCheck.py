from urllib.request import urlopen
link = "https://fratiloiu.com/key"
f = urlopen(link)
myfile = f.read()
print("Hash currently online: ", myfile[435:-49])