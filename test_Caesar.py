import unittest
from ex5 import CaesarCipher

class TestCaesar(unittest.TestCase):
    def test_encrypt_char(self):
        caesar_cipher = CaesarCipher(3)
        self.assertEqual(caesar_cipher.encrypt('a'), 'd')
        self.assertEqual(caesar_cipher.encrypt('x'), 'a')
        self.assertEqual(caesar_cipher.encrypt('A'), 'D')
        self.assertEqual(caesar_cipher.encrypt('z'), 'c')
        self.assertEqual(caesar_cipher.encrypt(' '), ' ')
        caesar_cipher = CaesarCipher(-3)
        self.assertEqual(caesar_cipher.encrypt('a'), 'x')
        self.assertEqual(caesar_cipher.encrypt('d'), 'a')
        self.assertEqual(caesar_cipher.encrypt('A'), 'X')
        self.assertEqual(caesar_cipher.encrypt('z'), 'w')
        self.assertEqual(caesar_cipher.encrypt(' '), ' ')

    def test_encrypt_char_shift_26(self):
        caesar_cipher = CaesarCipher(26)
        self.assertEqual(caesar_cipher.encrypt('A'), 'A')
        self.assertEqual(caesar_cipher.encrypt('z'), 'z')
        caesar_cipher = CaesarCipher(-26)
        self.assertEqual(caesar_cipher.encrypt('A'), 'A')
        self.assertEqual(caesar_cipher.encrypt('z'), 'z')

    def test_decrypt_char(self):
        caesar_cipher = CaesarCipher(3)
        self.assertEqual(caesar_cipher.decrypt('d'), 'a')
        self.assertEqual(caesar_cipher.decrypt('a'), 'x')
        self.assertEqual(caesar_cipher.decrypt('D'), 'A')
        self.assertEqual(caesar_cipher.decrypt('c'), 'z')
        self.assertEqual(caesar_cipher.decrypt(' '), ' ')
        caesar_cipher = CaesarCipher(-3)
        self.assertEqual(caesar_cipher.decrypt('x'), 'a')
        self.assertEqual(caesar_cipher.decrypt('a'), 'd')
        self.assertEqual(caesar_cipher.decrypt('X'), 'A')
        self.assertEqual(caesar_cipher.decrypt('w'), 'z')
        self.assertEqual(caesar_cipher.decrypt(' '), ' ')

    def test_decrypt_char_shift_26(self):
        caesar_cipher = CaesarCipher(26)
        self.assertEqual(caesar_cipher.decrypt('A'), 'A')
        self.assertEqual(caesar_cipher.decrypt('z'), 'z')
        caesar_cipher = CaesarCipher(-26)
        self.assertEqual(caesar_cipher.decrypt('A'), 'A')
        self.assertEqual(caesar_cipher.decrypt('z'), 'z')

    def test_encrypt_string(self):
        caesar_cipher = CaesarCipher(3)
        self.assertEqual(caesar_cipher.encrypt('Hello'), 'Khoor')
        self.assertEqual(caesar_cipher.encrypt('world'), 'zruog')
        self.assertEqual(caesar_cipher.encrypt('Mtm is the BEST!'), 'Pwp lv wkh EHVW!')
        self.assertEqual(caesar_cipher.encrypt('123'), '123')
        caesar_cipher = CaesarCipher(-3)
        self.assertEqual(caesar_cipher.encrypt('Hello'), 'Ebiil')
        self.assertEqual(caesar_cipher.encrypt('world'), 'tloia')
        self.assertEqual(caesar_cipher.encrypt('123'), '123')
        self.assertEqual(caesar_cipher.encrypt('Pwp lv wkh EHVW!'), 'Mtm is the BEST!')


    def test_encrypt_string_shift_26(self):
        caesar_cipher = CaesarCipher(26)
        self.assertEqual(caesar_cipher.encrypt('Hello, World!'), 'Hello, World!')
        self.assertEqual(caesar_cipher.encrypt(''), '')
        caesar_cipher = CaesarCipher(-26)
        self.assertEqual(caesar_cipher.encrypt('Hello, World!'), 'Hello, World!')
        self.assertEqual(caesar_cipher.encrypt(''), '')

    def test_decrypt_string(self):
        caesar_cipher = CaesarCipher(3)
        self.assertEqual(caesar_cipher.decrypt('Pwp lv wkh EHVW!'), 'Mtm is the BEST!')
        self.assertEqual(caesar_cipher.decrypt('Khoor'), 'Hello')
        self.assertEqual(caesar_cipher.decrypt('zruog'), 'world')
        self.assertEqual(caesar_cipher.decrypt('123'), '123')
        caesar_cipher = CaesarCipher(-3)
        self.assertEqual(caesar_cipher.decrypt('Ebiil'), 'Hello')
        self.assertEqual(caesar_cipher.decrypt('tloia'), 'world')
        self.assertEqual(caesar_cipher.decrypt('123'), '123')
        self.assertEqual(caesar_cipher.decrypt('Mtm is the BEST!'), 'Pwp lv wkh EHVW!')

    def test_decrypt_string_shift_26(self):
        caesar_cipher = CaesarCipher(26)
        self.assertEqual(caesar_cipher.decrypt('Hello, World!'), 'Hello, World!')
        self.assertEqual(caesar_cipher.decrypt(''), '')
        caesar_cipher = CaesarCipher(-26)
        self.assertEqual(caesar_cipher.decrypt('Hello, World!'), 'Hello, World!')
        self.assertEqual(caesar_cipher.decrypt(''), '')
     
if __name__ == '__main__':
    unittest.main()
