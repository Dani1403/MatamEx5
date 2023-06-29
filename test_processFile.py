import unittest
from ex5 import *
import tempfile

class TestProcessFile(unittest.TestCase):

    def setUp(self):
        self.temp_files = []

    def tearDown(self):
        for file_path in self.temp_files:
            os.remove(file_path)

    def create_temp_file(self, content, extension=".txt"):
        with tempfile.NamedTemporaryFile(suffix=extension, delete=False) as temp_file:
            temp_file.write(content.encode())
            temp_file_path = temp_file.name
            self.temp_files.append(temp_file_path)
        return temp_file_path

    def assertFileContentEqual(self, file_path, expected_content):
        with open(file_path, "rt") as file:
            content = file.read()
            self.assertEqual(content, expected_content)

    def remove_temp_files(self, *file_paths):
        for file_path in file_paths:
            if file_path in self.temp_files:
                os.remove(file_path)
                self.temp_files.remove(file_path)

    def test_process_file_encrypt_valid_file_caesar(self):
        plaintext = "This is a test file."
        temp_file_path = self.create_temp_file(plaintext)
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_CAESAR,
            CONFIG_KEY_KEY: 3
        }
        encryptor = getEncryptorFromDict(config_dict)
        processFile(temp_file_path, CONFIG_MODE_ENCRYPT, encryptor)
        expected_enc_file_path = temp_file_path.replace(".txt", ".enc")
        self.assertTrue(os.path.exists(expected_enc_file_path))
        self.assertFileContentEqual(expected_enc_file_path, "Wklv lv d whvw iloh.")
        self.remove_temp_files(temp_file_path, expected_enc_file_path)

    def test_process_file_decrypt_valid_file_caesar(self):
        encrypted_content = "Wklv lv d whvw iloh."
        temp_file_path = self.create_temp_file(encrypted_content, extension=".enc")
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_CAESAR,
            CONFIG_KEY_KEY: 3
        }
        encryptor = getEncryptorFromDict(config_dict)
        processFile(temp_file_path, CONFIG_MODE_DECRYPT, encryptor)
        expected_dec_file_path = temp_file_path.replace(".enc", ".txt")
        self.assertTrue(os.path.exists(expected_dec_file_path))
        self.assertFileContentEqual(expected_dec_file_path, "This is a test file.")
        self.remove_temp_files(temp_file_path, expected_dec_file_path)

    def test_process_file_encrypt_valid_file_vigenere(self):
        plaintext = "This is a test file."
        temp_file_path = self.create_temp_file(plaintext)
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_VIGENERE,
            CONFIG_KEY_KEY: "python"
        }
        encryptor = getEncryptorFromDict(config_dict)
        processFile(temp_file_path, CONFIG_MODE_ENCRYPT, encryptor)
        expected_enc_file_path = temp_file_path.replace(".txt", ".enc")
        self.assertTrue(os.path.exists(expected_enc_file_path))
        self.assertFileContentEqual(expected_enc_file_path, "Ifbz wf p rxzh sxjx.")
        self.remove_temp_files(temp_file_path, expected_enc_file_path)

    def test_process_file_decrypt_valid_file_vigenere(self):
        encrypted_content = "Ifbz wf p rxzh sxjx."
        temp_file_path = self.create_temp_file(encrypted_content, extension=".enc")
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_VIGENERE,
            CONFIG_KEY_KEY: "python"
        }
        encryptor = getEncryptorFromDict(config_dict)
        processFile(temp_file_path, CONFIG_MODE_DECRYPT, encryptor)
        expected_dec_file_path = temp_file_path.replace(".enc", ".txt")
        self.assertTrue(os.path.exists(expected_dec_file_path))
        self.assertFileContentEqual(expected_dec_file_path, "This is a test file.")
        self.remove_temp_files(temp_file_path, expected_dec_file_path)

    def test_process_file_invalid_mode(self):
        plaintext = "This is a test file."
        temp_file_path = self.create_temp_file(plaintext)
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_CAESAR,
            CONFIG_KEY_KEY: 3
        }
        encryptor = getEncryptorFromDict(config_dict)
        with self.assertRaises(ValueError):
            processFile(temp_file_path, "invalid_mode", encryptor)
        self.remove_temp_files(temp_file_path)

    def test_process_file_invalid_key(self):
        plaintext = "This is a test file."
        temp_file_path = self.create_temp_file(plaintext)
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_CAESAR,
            CONFIG_KEY_KEY: "invalid_key"
        } 
        with self.assertRaises(TypeError):
            encryptor = getEncryptorFromDict(config_dict)
            processFile(temp_file_path, CONFIG_MODE_ENCRYPT, encryptor)
        self.remove_temp_files(temp_file_path)

    def test_process_file_invalid_encryptor(self):
        plaintext = "This is a test file."
        temp_file_path = self.create_temp_file(plaintext)
        encryptor = None
        with self.assertRaises(TypeError):
            processFile(temp_file_path, CONFIG_MODE_ENCRYPT, encryptor)
        self.remove_temp_files(temp_file_path)

    def test_process_file_vigenere_with_list_key(self):
        plaintext = "This is a test file."
        temp_file_path = self.create_temp_file(plaintext)
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_VIGENERE,
            CONFIG_KEY_KEY: [1, 1, 1, 1, 1]
        }
        encryptor = getEncryptorFromDict(config_dict)
        processFile(temp_file_path, CONFIG_MODE_ENCRYPT, encryptor)
        expected_enc_file_path = temp_file_path.replace(".txt", ".enc")
        self.assertTrue(os.path.exists(expected_enc_file_path))
        self.assertFileContentEqual(expected_enc_file_path, "Uijt jt b uftu gjmf.")
        self.remove_temp_files(temp_file_path, expected_enc_file_path)

    def test_process_file_vigenere_with_list_key_2(self):
        plaintext = "This is a test file."
        temp_file_path = self.create_temp_file(plaintext)
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_VIGENERE,
            CONFIG_KEY_KEY: [16, 25, 20, 7, 14, 17]
        }
        encryptor = getEncryptorFromDict(config_dict)
        processFile(temp_file_path, CONFIG_MODE_ENCRYPT, encryptor)
        expected_enc_file_path = temp_file_path.replace(".txt", ".enc")
        self.assertTrue(os.path.exists(expected_enc_file_path))
        self.assertFileContentEqual(expected_enc_file_path, "Jgcz wj q syzh wyky.")
        self.remove_temp_files(temp_file_path, expected_enc_file_path)

    def test_process_file_encrypt_valid_file_caesar_negative_key(self):
        plaintext = "This is a test file."
        temp_file_path = self.create_temp_file(plaintext)
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_CAESAR,
            CONFIG_KEY_KEY: -3
        }
        encryptor = getEncryptorFromDict(config_dict)
        processFile(temp_file_path, CONFIG_MODE_ENCRYPT, encryptor)
        expected_enc_file_path = temp_file_path.replace(".txt", ".enc")
        self.assertTrue(os.path.exists(expected_enc_file_path))
        self.assertFileContentEqual(expected_enc_file_path, "Qefp fp x qbpq cfib.")
        self.remove_temp_files(temp_file_path, expected_enc_file_path)

    def test_process_file_decrypt_valid_file_caesar_negative_key(self):
        encrypted_content = "Qefp fp x qbpq cfib."
        temp_file_path = self.create_temp_file(encrypted_content, extension=".enc")
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_CAESAR,
            CONFIG_KEY_KEY: -3
        }
        encryptor = getEncryptorFromDict(config_dict)
        processFile(temp_file_path, CONFIG_MODE_DECRYPT, encryptor)
        expected_dec_file_path = temp_file_path.replace(".enc", ".txt")
        self.assertTrue(os.path.exists(expected_dec_file_path))
        self.assertFileContentEqual(expected_dec_file_path, "This is a test file.")
        self.remove_temp_files(temp_file_path, expected_dec_file_path)

    def test_process_file_encrypt_valid_file_vigenere_negative_key(self):
        plaintext = "This is a test file."
        temp_file_path = self.create_temp_file(plaintext)
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_VIGENERE,
            CONFIG_KEY_KEY: [-1, -1]
        }
        encryptor = getEncryptorFromDict(config_dict)
        processFile(temp_file_path, CONFIG_MODE_ENCRYPT, encryptor)
        expected_enc_file_path = temp_file_path.replace(".txt", ".enc")
        self.assertTrue(os.path.exists(expected_enc_file_path))
        self.assertFileContentEqual(expected_enc_file_path, "Sghr hr z sdrs ehkd.")
        self.remove_temp_files(temp_file_path, expected_enc_file_path)

    def test_process_file_decrypt_valid_file_vigenere_negative_key(self):
        encrypted_content = "Sghr hr z sdrs ehkd."
        temp_file_path = self.create_temp_file(encrypted_content, extension=".enc")
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_VIGENERE,
            CONFIG_KEY_KEY: [-1,-1]
        }
        encryptor = getEncryptorFromDict(config_dict)
        processFile(temp_file_path, CONFIG_MODE_DECRYPT, encryptor)
        expected_dec_file_path = temp_file_path.replace(".enc", ".txt")
        self.assertTrue(os.path.exists(expected_dec_file_path))
        self.assertFileContentEqual(expected_dec_file_path, "This is a test file.")
        self.remove_temp_files(temp_file_path, expected_dec_file_path)

    def test_process_file_encrypt_valid_file_vigenere_with_numbers(self):
        plaintext = "This is a test file with numbers: 12345."
        temp_file_path = self.create_temp_file(plaintext)
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_VIGENERE,
            CONFIG_KEY_KEY: "password"
        }
        encryptor = getEncryptorFromDict(config_dict)
        processFile(temp_file_path, CONFIG_MODE_ENCRYPT, encryptor)
        expected_enc_file_path = temp_file_path.replace(".txt", ".enc")
        self.assertTrue(os.path.exists(expected_enc_file_path))
        self.assertFileContentEqual(expected_enc_file_path, "Ihak eg r wtsl xezv zxtz fqashgs: 12345.")
        self.remove_temp_files(temp_file_path, expected_enc_file_path)

    def test_process_file_decrypt_valid_file_vigenere_with_numbers(self):
        encrypted_content = "Ihak eg r wtsl xezv zxtz fqashgs: 12345."
        temp_file_path = self.create_temp_file(encrypted_content, extension=".enc")
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_VIGENERE,
            CONFIG_KEY_KEY: "password"
        }
        encryptor = getEncryptorFromDict(config_dict)
        processFile(temp_file_path, CONFIG_MODE_DECRYPT, encryptor)
        expected_dec_file_path = temp_file_path.replace(".enc", ".txt")
        self.assertTrue(os.path.exists(expected_dec_file_path))
        self.assertFileContentEqual(expected_dec_file_path, "This is a test file with numbers: 12345.")
        self.remove_temp_files(temp_file_path, expected_dec_file_path)


if __name__ == '__main__':
    unittest.main()