import unittest
from ex5 import *

class TestGetEncryptorFromDict(unittest.TestCase):

    def test_get_encryptor_from_dict_caesar(self):
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_CAESAR,
            CONFIG_KEY_KEY: 3
        }
        encryptor = getEncryptorFromDict(config_dict)
        self.assertIsInstance(encryptor, CaesarCipher)
        self.assertEqual(encryptor.shift, 3)

    def test_get_encryptor_from_dict_vigenere_str(self):
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_VIGENERE,
            CONFIG_KEY_KEY: "python"
        }
        encryptor = getEncryptorFromDict(config_dict)
        self.assertIsInstance(encryptor, VigenereCipher)

    def test_get_encryptor_from_dict_vigenere_list(self):
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_VIGENERE,
            CONFIG_KEY_KEY: [3, 1, -4, -2]
        }
        encryptor = getEncryptorFromDict(config_dict)
        self.assertIsInstance(encryptor, VigenereCipher)

    def test_get_encryptor_from_dict_invalid_type(self):
        config_dict = {
            CONFIG_KEY_TYPE: "InvalidType",
            CONFIG_KEY_KEY: "key"
        }
        with self.assertRaises(ValueError):
            getEncryptorFromDict(config_dict)

    def test_get_encryptor_from_dict_invalid_caesar_key(self):
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_CAESAR,
            CONFIG_KEY_KEY: "key"
        }
        with self.assertRaises(TypeError):
            getEncryptorFromDict(config_dict)

    def test_get_encryptor_from_dict_invalid_vigenere_key(self):
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_VIGENERE,
            CONFIG_KEY_KEY: 123
        }
        with self.assertRaises(TypeError):
            getEncryptorFromDict(config_dict)

    def test_get_encryptor_from_dict_missing_key_key(self):
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_CAESAR
        }
        with self.assertRaises(KeyError):
            getEncryptorFromDict(config_dict)

    def test_get_encryptor_from_dict_invalid_keys(self):
        config_dict = {
            "InvalidKey": "InvalidValue",
            "AnotherInvalidKey": "AnotherInvalidValue"
        }
        with self.assertRaises(KeyError):
            getEncryptorFromDict(config_dict)

    # Edge case: Empty dictionary
    def test_get_encryptor_from_dict_empty_dict(self):
        config_dict = {}
        with self.assertRaises(KeyError):
            getEncryptorFromDict(config_dict)

    # Edge case: Empty encryption key for Caesar cipher
    def test_get_encryptor_from_dict_caesar_empty_key(self):
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_CAESAR,
            CONFIG_KEY_KEY: None
        }
        with self.assertRaises(TypeError):
            getEncryptorFromDict(config_dict)

    # Edge case: Empty encryption key for Vigenere cipher
    def test_get_encryptor_from_dict_vigenere_empty_key(self):
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_VIGENERE,
            CONFIG_KEY_KEY: ""
        }
        with self.assertRaises(TypeError):
            getEncryptorFromDict(config_dict)

    # Edge case: Long encryption key for Vigenere cipher
    def test_get_encryptor_from_dict_vigenere_long_key(self):
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_VIGENERE,
            CONFIG_KEY_KEY: "verylongkeythatexceedsthesizeoftheplaintext"
        }
        encryptor = getEncryptorFromDict(config_dict)
        self.assertIsInstance(encryptor, VigenereCipher)

    # Edge case: Negative encryption key for Caesar cipher
    def test_get_encryptor_from_dict_caesar_negative_key(self):
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_CAESAR,
            CONFIG_KEY_KEY: -3
        }
        encryptor = getEncryptorFromDict(config_dict)
        self.assertIsInstance(encryptor, CaesarCipher)
        self.assertEqual(encryptor.shift, -3)

    # Edge case: Negative encryption key for Vigenere cipher
    def test_get_encryptor_from_dict_vigenere_negative_key(self):
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_VIGENERE,
            CONFIG_KEY_KEY: [-3, -1, -4, -2]
        }
        encryptor = getEncryptorFromDict(config_dict)
        self.assertIsInstance(encryptor, VigenereCipher)

if __name__ == '__main__':
    unittest.main()
