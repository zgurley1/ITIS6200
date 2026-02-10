import hashlib
import json
import os

# For this assignment I used the following documentation for hash functions https://www.geeksforgeeks.org/python/hashlib-module-in-python/

def hash_file(fileName):
    sha256 = hashlib.sha256()

    with open(fileName,"rb") as f:
        content = f.read()
        sha256.update(content)

    return sha256.hexdigest()

def traverse_dir(userDir):
    hashMap = {}
    for filename in os.listdir(userDir):
        filePath = os.path.join(userDir, filename)

        hashHex = hash_file(filePath)

        hashMap[filePath] = hashHex
    return hashMap

def generate_table(userDir):
    
    if os.path.exists(userDir):
        hashMap = traverse_dir(userDir)
    else:
        return False


    #print(hashMap)
    with open("HashMap.json", "w") as f:
        json.dump(hashMap, f, indent=4)

    print("Hash table generated :)")
    return

def verify(userDir):
    if os.path.exists(userDir):
        hashMap = traverse_dir(userDir)
    else:
        return False

    with open("HashMap.json", "r") as f:
        loadedHashMap = json.load(f)

    for hash in hashMap:

        if hash not in loadedHashMap:
            print(f"{hash} hash added")
        elif hashMap[hash] == loadedHashMap[hash]:
            print(f"{hash} hash is valid")
        elif  hashMap[hash] != loadedHashMap[hash]:
            print(f"{hash} hash has been modified")
            
        

    
    for hash in loadedHashMap:
        if hash not in hashMap:
            print(f"{hash} hash deleted")

    return

def main():
    validInput = False

    while not validInput:
        userChoice = input("Please select: \n1. Create new hash \n2. Verify hash\n")

        if (userChoice == "1" or userChoice == "2"):
            break
        else:
            print("Please enter valid input")



    if (userChoice == "1"):
        userDir = input("Please enter a directory path for hashing: ")
        generate_table(userDir)

    if (userChoice == "2"):
        userDir = input("Please enter a directory path for verification: ")
        verify(userDir)
        return


    return

if __name__=="__main__":
    main()