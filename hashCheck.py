from termcolor import colored

# For older python
# print colored('hello', 'red'), colored('world', 'green')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

with open("check.txt","r") as textfile:
    content = textfile.read()
    hashToCheck = content[436:-95]
    print("Found hash on website: ", hashToCheck)
with open("generatedHash.txt", "r") as generatedHash:
    compare = generatedHash.read()
    print("Hash to compare to:    ", compare)
    if hashToCheck == compare:
        # print("Hashes match.\033[92m")
        # print(f"{bcolors.OKGREEN}Hashes match.{bcolors.ENDC}")
        print(colored('Hashes match.', 'green'))
    else:
        # print("Hashes dont yet match.\033[92m")
        # print(f"{bcolors.WARNING}Hashes dont yet match.{bcolors.ENDC}")
        print(colored('Hashes dont yet match.', 'red'))

