import json
import os
from typing import Union

# ----------------------------- Constants --------------------------- #
LOWER_A = ord("a")
UPPER_A = ord("A")
ALPHABET_SIZE = ord("z") - ord("a") + 1

CONFIG_FILE_NAME = ".json"
CONFIG_KEY_TYPE = "type"
CONFIG_KEY_MODE = "mode"
CONFIG_KEY_KEY = "key"

CONFIG_TYPE_CAESAR = "Caesar"
CONFIG_TYPE_VIGENERE = "Vigenere"
CONFIG_MODE_ENCRYPT = "encrypt"
CONFIG_MODE_DECRYPT = "decrypt"

TXT_EXTENSION = ".txt"
ENC_EXTENSION = ".enc"

# ------------------------ Caesar Cipher Class ----------------------- #
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

# ------------------------ Vigenere Cipher Class --------------------- #
class VigenereCipher:

    def __init__(self, keys: list):
        self.keys = keys

    def encrypt(self, plainText: str) -> str:
        if not self.keys :
            return plainText
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

# ---------------------- Global functions -------------------- #

def getVigenereFromStr(keyString: str) -> VigenereCipher:
    keys = []
    for char in keyString:
        if char.isalpha():
            keys.append(ord(char) - (LOWER_A if char.islower() else UPPER_A - ALPHABET_SIZE))
    return VigenereCipher(keys)

def getEncryptorFromDict(configDict: dict)-> Union[CaesarCipher, VigenereCipher]:

    encryptionType = configDict[CONFIG_KEY_TYPE]
    if type(encryptionType) != str:
        raise TypeError("Encryption type should be string")
    encryptionKey = configDict[CONFIG_KEY_KEY]

    if (encryptionType == CONFIG_TYPE_CAESAR) :
        if isinstance(encryptionKey, int):
            return CaesarCipher(encryptionKey)
        else:
            raise TypeError("Encryption key for Caesar Cipher should be int")
    elif (encryptionType == CONFIG_TYPE_VIGENERE):
        if isinstance(encryptionKey, str):
            return getVigenereFromStr(encryptionKey)
        elif isinstance(encryptionKey, list):
            return VigenereCipher(encryptionKey)
        else:
            raise TypeError("Encryption key for Vigenere Cipher should be string or list")
    else:
        raise ValueError(f"Invalid encryption Type, should be either Caesar or Vigenere but got {encryptionType}")

def processFile(filePath: str, encryptionMode: str, encryptor: Union[CaesarCipher, VigenereCipher]) -> None:  
    if encryptor is None:
        raise TypeError("Encryptor is None")
    basename, extension = os.path.splitext(filePath)
    if encryptionMode == CONFIG_MODE_ENCRYPT:
        if extension.lower() != TXT_EXTENSION:
            return
        outFile = f"{basename}{ENC_EXTENSION}"
        with open(filePath, "rt") as plainTextFile:
            content = encryptor.encrypt(plainTextFile.read())
    elif encryptionMode == CONFIG_MODE_DECRYPT:
        if extension.lower() != ENC_EXTENSION:
            return
        outFile = f"{basename}{TXT_EXTENSION}"
        with open(filePath) as encryptedTextFile:
            content = encryptor.decrypt(encryptedTextFile.read())
    else:
        raise ValueError(f"Encryption mode should be either decrypt or encrypt but got {encryptionMode}")
    
    with open(outFile, "wt") as resultFile:
        resultFile.write(content)
    


#TODO : raise Value Error  if dir_path is not directory, raise more exceptions...
def processDirectory(dir_path: str) -> None:
    configPath = os.path.join(dir_path, CONFIG_FILE_NAME)
    with open(configPath, "rt") as configFile:
        configDict = json.load(configFile)

    for fileName in os.listdir(dir_path):
        filePath = os.path.join(dir_path, fileName)
        processFile(filePath, configDict[CONFIG_KEY_MODE], getEncryptorFromDict(configDict))
