LOWER_A = ord("a")
UPPER_A = ord("A")
ALPHABET_SIZE = ord("z") - ord("a") + 1

class CaesarCipher:

    def __init__(self, shift: int):
        self.shift = shift

    def encrypt(self, plainText: str) -> str:
        encryptedStr = ""
        for char in plainText:
            if char.isalpha():
                position = ord(char) - (LOWER_A if char.islower() else UPPER_A)
                encryptedStr += chr((position + self.shift) % ALPHABET_SIZE + (LOWER_A if char.islower() else UPPER_A))
            else:
                encryptedStr += char
        return encryptedStr

    def decrypt(self, cipherText: str) -> str:
        self.shift = -self.shift
        decryptedStr = self.encrypt(cipherText)
        self.shift = -self.shift
        return decryptedStr


class VigenereCipher:

    def __init__(self, keys: list):
        self.keys = keys

    def encrypt(self, plainText: str) -> str:
        index = 0
        encryptedStr = ""
        for char in plainText:
            if char.isalpha():
                position = ord(char) - (LOWER_A if char.islower() else UPPER_A)
                encryptedStr += chr((position + self.keys[index]) % ALPHABET_SIZE + (LOWER_A if char.islower() else UPPER_A))
                index = (index + 1) % len(self.keys)
            else:
                encryptedStr += char
        return encryptedStr

    def decrypt(self, cipherText: str) -> str:
        self.keys = [-num for num in self.keys]
        decryptedStr = self.encrypt(cipherText)
        self.keys = [-num for num in self.keys]
        return decryptedStr

def getVigenereFromStr(keyString: str) -> VigenereCipher:
    keys = []
    for char in keyString:
        if char.isalpha():
            keys.append(ord(char) - (LOWER_A if char.islower() else UPPER_A))
    return VigenereCipher(keys)

def processDirectory(dir_path: str) -> None:

    print("d")
caesar_cipher = CaesarCipher(3)
print(caesar_cipher.encrypt('a'))
print(caesar_cipher.encrypt('Mtm is the BEST!'))
print(caesar_cipher.decrypt('d'))
print(caesar_cipher.decrypt("Pwp lv wkh EHVW!"))
vigenere_cipher = VigenereCipher([1,2,3,4,-5])
print(vigenere_cipher.encrypt("Hello World! "))
print(vigenere_cipher.decrypt("Igopj Xqupy! "))
vigenere_from_str = getVigenereFromStr("python rules, C drools")
print(vigenere_from_str.encrypt("JK, C is awesome"))
print(vigenere_from_str.decrypt("YI, V pg nnydseg"))
