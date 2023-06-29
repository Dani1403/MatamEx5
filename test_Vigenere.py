import unittest
from ex5 import VigenereCipher, getVigenereFromStr

class TestVigenere(unittest.TestCase):
    def test_encrypt_char(self):
        vigenere_cipher = VigenereCipher([3, 1, -4, -2])
        self.assertEqual(vigenere_cipher.encrypt('a'), 'd')
        self.assertEqual(vigenere_cipher.encrypt('x'), 'a')
        vigenere_cipher = VigenereCipher([-3, -1, 4, 2])
        self.assertEqual(vigenere_cipher.encrypt('a'), 'x')
        self.assertEqual(vigenere_cipher.encrypt('d'), 'a')

    def test_decrypt_char(self):
        vigenere_cipher = VigenereCipher([3, 1, -4, -2])
        self.assertEqual(vigenere_cipher.decrypt('d'), 'a')
        self.assertEqual(vigenere_cipher.decrypt('y'), 'v')
        vigenere_cipher = VigenereCipher([-3, -1, 4, 2])
        self.assertEqual(vigenere_cipher.decrypt('x'), 'a')
        self.assertEqual(vigenere_cipher.decrypt('y'), 'b')

    def test_encrypt_string(self):
        vigenere_cipher = VigenereCipher([3, 1, -4, -2])
        self.assertEqual(vigenere_cipher.encrypt('Hello, World!'), 'Kfhjr, Xkpoe!')
        vigenere_cipher = VigenereCipher([-3, -1, 4, 2])
        self.assertEqual(vigenere_cipher.encrypt('Hello, World!'), 'Edpnl, Vstic!')
        vigenere_cipher = VigenereCipher([1,2,3,4,-5])
        self.assertEqual(vigenere_cipher.encrypt("Hello World! "), "Igopj Xqupy! ")

    def test_decrypt_string(self):
        vigenere_cipher = VigenereCipher([3, 1, -4, -2])
        self.assertEqual(vigenere_cipher.decrypt('Kfhjr, Xkpoe!'), 'Hello, World!')
        vigenere_cipher = VigenereCipher([-3, -1, 4, 2])
        self.assertEqual(vigenere_cipher.decrypt('Edpnl, Vstic!'), 'Hello, World!')
        vigenere_cipher = VigenereCipher([1,2,3,4,-5])
        self.assertEqual(vigenere_cipher.decrypt("Igopj Xqupy! "), "Hello World! ")

    def test_encrypt_string_with_spaces(self):
        vigenere_cipher = VigenereCipher([3, 1, -4, -2])
        self.assertEqual(vigenere_cipher.encrypt('This is a test'), 'Wieq lt w rhtp')
        vigenere_cipher = VigenereCipher([-3, -1, 4, 2])
        self.assertEqual(vigenere_cipher.encrypt('This is a test'), 'Qgmu fr e vbrx')

    def test_decrypt_string_with_spaces(self):
        vigenere_cipher = VigenereCipher([3, 1, -4, -2])
        self.assertEqual(vigenere_cipher.decrypt('Wieq lt w rhtp'), 'This is a test')
        vigenere_cipher = VigenereCipher([-3, -1, 4, 2])
        self.assertEqual(vigenere_cipher.decrypt('Qgmu fr e vbrx'), 'This is a test')

    def test_encrypt_string_with_non_alpha_chars(self):
        vigenere_cipher = VigenereCipher([3, 1, -4, -2])
        self.assertEqual(vigenere_cipher.encrypt('Hello, World!123'), 'Kfhjr, Xkpoe!123')
        vigenere_cipher = VigenereCipher([-3, -1, 4, 2])
        self.assertEqual(vigenere_cipher.encrypt('Hello, World!123'), 'Edpnl, Vstic!123')

    def test_decrypt_string_with_non_alpha_chars(self):
        vigenere_cipher = VigenereCipher([3, 1, -4, -2])
        self.assertEqual(vigenere_cipher.decrypt('Kfhjr, Xkpoe!123'), 'Hello, World!123')
        vigenere_cipher = VigenereCipher([-3, -1, 4, 2])
        self.assertEqual(vigenere_cipher.decrypt('Edpnl, Vstic!123'), 'Hello, World!123')

    def test_encrypt_string_shift_26(self):
        vigenere_cipher = VigenereCipher([26, 26, 26, 26])
        self.assertEqual(vigenere_cipher.encrypt('Hello, World!'), 'Hello, World!')
        vigenere_cipher = VigenereCipher([-26, -26, -26, -26])
        self.assertEqual(vigenere_cipher.encrypt('Hello, World!'), 'Hello, World!')

    def test_decrypt_string_shift_26(self):
        vigenere_cipher = VigenereCipher([26, 26, 26, 26])
        self.assertEqual(vigenere_cipher.decrypt('Hello, World!'), 'Hello, World!')
        vigenere_cipher = VigenereCipher([-26, -26, -26, -26])
        self.assertEqual(vigenere_cipher.decrypt('Hello, World!'), 'Hello, World!')

    def test_get_vigenere_from_str(self):
        vigenere_from_str = getVigenereFromStr("hello")
        self.assertIsInstance(vigenere_from_str, VigenereCipher)
        self.assertEqual(vigenere_from_str.encrypt("Hello, World!"), "Oiwwc, Dscwr!")
        self.assertEqual(vigenere_from_str.decrypt("Oiwwc, Dscwr!"), "Hello, World!")

        vigenere_from_str = getVigenereFromStr("PYTHON")
        self.assertIsInstance(vigenere_from_str, VigenereCipher)
        self.assertEqual(vigenere_from_str.encrypt("Hello, World!"), "Wcesc, Jdpek!")
        self.assertEqual(vigenere_from_str.decrypt("Wcesc, Jdpek!"), "Hello, World!")

        vigenere_from_str = getVigenereFromStr("abcDEF")
        self.assertIsInstance(vigenere_from_str, VigenereCipher)
        self.assertEqual(vigenere_from_str.encrypt("Hello, World!"), "Hfnos, Bosng!")
        self.assertEqual(vigenere_from_str.decrypt("Hfnos, Bosng!"), "Hello, World!")

        vigenere_from_str = getVigenereFromStr("XYZxyz")
        self.assertIsInstance(vigenere_from_str, VigenereCipher)
        self.assertEqual(vigenere_from_str.encrypt("Hello, World!"), "Eckim, Vlpka!")
        self.assertEqual(vigenere_from_str.decrypt("Eckim, Vlpka!"), "Hello, World!")

        vigenere_from_str = getVigenereFromStr("")
        self.assertIsInstance(vigenere_from_str, VigenereCipher)
        self.assertEqual(vigenere_from_str.encrypt("Hello, World!"), "Hello, World!")
        self.assertEqual(vigenere_from_str.decrypt("Hello, World!"), "Hello, World!")

        vigenere_from_str = getVigenereFromStr("python rules, C drools")
        self.assertEqual(vigenere_from_str.encrypt("JK, C is awesome"), "YI, V pg nnydseg")

        vigenere_from_str = getVigenereFromStr("python rules, C drools")
        self.assertEqual(vigenere_from_str.decrypt("YI, V pg nnydseg"), "JK, C is awesome")

if __name__ == '__main__':
    unittest.main()
