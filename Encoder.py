alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def handleRollover(num):
    while(num >= len(alphabet)-1):
        num -= len(alphabet)

    return num


text = input("enter text to be encrypted (no spaces all cap)")
key = input("enter key to encrypt against (no spaces all cap)")
cipher = []

keyPointer = 0

for i in range(0, len(text)):
    print(alphabet[keyPointer])

    cipher.append(alphabet[handleRollover(alphabet.index(key[keyPointer]) + alphabet.index(text[i]))])
    keyPointer += 1
    if(keyPointer > len(key)-1):
        keyPointer = 0

print("".join(cipher))


