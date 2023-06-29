from ex5 import *
import unittest
import shutil
import tempfile

class TestProcessDirectory(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def create_config_file(self, config_dict):
        config_file_path = os.path.join(self.test_dir, CONFIG_FILE_NAME)
        with open(config_file_path, "w") as config_file:
            json.dump(config_dict, config_file)
        return config_file_path

    def create_file_with_content(self, file_path, content):
        with open(file_path, "w") as file:
            file.write(content)

    def assertFileContentEqual(self, file_path, expected_content):
        with open(file_path, "r") as file:
            content = file.read()
            self.assertEqual(content, expected_content)

    def test_process_directory_caesar_decrypt(self):
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_CAESAR,
            CONFIG_KEY_MODE: CONFIG_MODE_DECRYPT,
            CONFIG_KEY_KEY: 3
        }
        config_file_path = self.create_config_file(config_dict)

        encrypted_texts = ["Wklv lv iloh 1.", "Wklv lv iloh 2."]
        file_paths = []
        for i, encrypted_text in enumerate(encrypted_texts, start=1):
            file_path = os.path.join(self.test_dir, f"file{i}.enc")
            self.create_file_with_content(file_path, encrypted_text)
            file_paths.append(file_path)

        processDirectory(self.test_dir)

        decrypted_texts = ["This is file 1.", "This is file 2."]
        for i, decrypted_text in enumerate(decrypted_texts, start=1):
            dec_file_path = os.path.join(self.test_dir, f"file{i}.txt")
            self.assertTrue(os.path.exists(dec_file_path))
            self.assertFileContentEqual(dec_file_path, decrypted_text)

    def test_process_directory_caesar_encrypt(self):
        file_names = ["file1.txt", "file2.txt", "file3.txt"]
        plain_texts = ["This is file 1.", "This is file 2.", "This is file 3."]

        for file_name, plain_text in zip(file_names, plain_texts):
            file_path = os.path.join(self.test_dir, file_name)
            self.create_file_with_content(file_path, plain_text)

        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_CAESAR,
            CONFIG_KEY_MODE: CONFIG_MODE_ENCRYPT,
            CONFIG_KEY_KEY: 3
        }
        config_file_path = self.create_config_file(config_dict)

        processDirectory(self.test_dir)

        encrypted_texts = ["Wklv lv iloh 1.", "Wklv lv iloh 2.", "Wklv lv iloh 3."]
        for i, encrypted_text in enumerate(encrypted_texts, start=1):
            enc_file_path = os.path.join(self.test_dir, f"file{i}.enc")
            self.assertTrue(os.path.exists(enc_file_path))
            self.assertFileContentEqual(enc_file_path, encrypted_text)

    def test_process_directory_vigenere_encrypt(self):
        file_names = ["file1.txt", "file2.txt", "file3.txt"]
        plain_texts = ["This is file 1.", "This is file 2.", "This is file 3."]

        for file_name, plain_text in zip(file_names, plain_texts):
            file_path = os.path.join(self.test_dir, file_name)
            self.create_file_with_content(file_path, plain_text)

        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_VIGENERE,
            CONFIG_KEY_MODE: CONFIG_MODE_ENCRYPT,
            CONFIG_KEY_KEY: "python"
        }
        config_file_path = self.create_config_file(config_dict)

        processDirectory(self.test_dir)

        encrypted_texts = ["Ifbz wf ugel 1.", "Ifbz wf ugel 2.", "Ifbz wf ugel 3."]
        for i, encrypted_text in enumerate(encrypted_texts, start=1):
            enc_file_path = os.path.join(self.test_dir, f"file{i}.enc")
            self.assertTrue(os.path.exists(enc_file_path))
            self.assertFileContentEqual(enc_file_path, encrypted_text)

    def test_process_directory_vigenere_from_str_decrypt(self):
        file_names = ["file1.enc", "file2.enc", "file3.enc"]
        encrypted_texts = ["Ifbz wf ugel 1.", "Ifbz wf ugel 2.", "Ifbz wf ugel 3."]

        for file_name, encrypted_text in zip(file_names, encrypted_texts):
            file_path = os.path.join(self.test_dir, file_name)
            self.create_file_with_content(file_path, encrypted_text)

        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_VIGENERE,
            CONFIG_KEY_MODE: CONFIG_MODE_DECRYPT,
            CONFIG_KEY_KEY: "python"
        }
        config_file_path = self.create_config_file(config_dict)

        processDirectory(self.test_dir)

        decrypted_texts = ["This is file 1.", "This is file 2.", "This is file 3."]
        for i, decrypted_text in enumerate(decrypted_texts, start=1):
            dec_file_path = os.path.join(self.test_dir, f"file{i}.txt")
            self.assertTrue(os.path.exists(dec_file_path))
            self.assertFileContentEqual(dec_file_path, decrypted_text)

    def test_process_directory_vigenere_from_list_encrypt(self):
        file_names = ["file1.txt", "file2.txt", "file3.txt"]
        plain_texts = ["This is file 1.", "This is file 2.", "This is file 3."]

        for file_name, plain_text in zip(file_names, plain_texts):
            file_path = os.path.join(self.test_dir, file_name)
            self.create_file_with_content(file_path, plain_text)

        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_VIGENERE,
            CONFIG_KEY_MODE: CONFIG_MODE_ENCRYPT,
            CONFIG_KEY_KEY: [1, 2, 3]
        }
        config_file_path = self.create_config_file(config_dict)

        processDirectory(self.test_dir)

        encrypted_texts = ["Ujlt kv gkof 1.", "Ujlt kv gkof 2.", "Ujlt kv gkof 3."]
        for i, encrypted_text in enumerate(encrypted_texts, start=1):
            enc_file_path = os.path.join(self.test_dir, f"file{i}.enc")
            self.assertTrue(os.path.exists(enc_file_path))
            self.assertFileContentEqual(enc_file_path, encrypted_text)

    def test_process_directory_caesar_negative_key(self):
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_CAESAR,
            CONFIG_KEY_MODE: CONFIG_MODE_ENCRYPT,
            CONFIG_KEY_KEY: -3
        }
        config_file_path = self.create_config_file(config_dict)

        file_names = ["file1.txt", "file2.txt", "file3.txt"]
        plain_texts = ["This is file 1.", "This is file 2.", "This is file 3."]

        for file_name, plain_text in zip(file_names, plain_texts):
            file_path = os.path.join(self.test_dir, file_name)
            self.create_file_with_content(file_path, plain_text)

        processDirectory(self.test_dir)

        encrypted_texts = ["Qefp fp cfib 1.", "Qefp fp cfib 2.", "Qefp fp cfib 3."]
        for i, encrypted_text in enumerate(encrypted_texts, start=1):
            enc_file_path = os.path.join(self.test_dir, f"file{i}.enc")
            self.assertTrue(os.path.exists(enc_file_path))
            self.assertFileContentEqual(enc_file_path, encrypted_text)

    def test_process_directory_vigenere_negative_key(self):
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_VIGENERE,
            CONFIG_KEY_MODE: CONFIG_MODE_ENCRYPT,
            CONFIG_KEY_KEY: [-1]
        }
        config_file_path = self.create_config_file(config_dict)

        file_names = ["file1.txt", "file2.txt", "file3.txt"]
        plain_texts = ["This is file 1.", "This is file 2.", "This is file 3."]

        for file_name, plain_text in zip(file_names, plain_texts):
            file_path = os.path.join(self.test_dir, file_name)
            self.create_file_with_content(file_path, plain_text)

        processDirectory(self.test_dir)

        encrypted_texts = ["Sghr hr ehkd 1.", "Sghr hr ehkd 2.", "Sghr hr ehkd 3."]
        for i, encrypted_text in enumerate(encrypted_texts, start=1):
            enc_file_path = os.path.join(self.test_dir, f"file{i}.enc")
            self.assertTrue(os.path.exists(enc_file_path))
            self.assertFileContentEqual(enc_file_path, encrypted_text)

    def test_process_directory_invalid_config_file(self):
        config_file_path = os.path.join(self.test_dir, CONFIG_FILE_NAME)
        self.create_file_with_content(config_file_path, "Invalid content")

        file_names = ["file1.txt", "file2.txt"]
        plain_texts = ["This is file 1.", "This is file 2."]

        for file_name, plain_text in zip(file_names, plain_texts):
            file_path = os.path.join(self.test_dir, file_name)
            self.create_file_with_content(file_path, plain_text)

        with self.assertRaises(ValueError):
            processDirectory(self.test_dir)

    def test_process_directory_invalid_cipher_type(self):
        config_dict = {
            CONFIG_KEY_TYPE: "invalid_type",
            CONFIG_KEY_MODE: CONFIG_MODE_ENCRYPT,
            CONFIG_KEY_KEY: 3
        }
        config_file_path = self.create_config_file(config_dict)

        file_names = ["file1.txt", "file2.txt"]
        plain_texts = ["This is file 1.", "This is file 2."]

        for file_name, plain_text in zip(file_names, plain_texts):
            file_path = os.path.join(self.test_dir, file_name)
            self.create_file_with_content(file_path, plain_text)

        with self.assertRaises(ValueError):
            processDirectory(self.test_dir)

    def test_process_directory_invalid_cipher_mode(self):
        config_dict = {
            CONFIG_KEY_TYPE: CONFIG_TYPE_CAESAR,
            CONFIG_KEY_MODE: "invalid_mode",
            CONFIG_KEY_KEY: 3
        }
        config_file_path = self.create_config_file(config_dict)

        file_names = ["file1.txt", "file2.txt"]
        plain_texts = ["This is file 1.", "This is file 2."]

        for file_name, plain_text in zip(file_names, plain_texts):
            file_path = os.path.join(self.test_dir, file_name)
            self.create_file_with_content(file_path, plain_text)

        with self.assertRaises(ValueError):
            processDirectory(self.test_dir)


if __name__ == '__main__':
    unittest.main()