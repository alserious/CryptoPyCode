import ast
import json
import os

from cryptography.fernet import Fernet


class CryptoModule:
    """
    Class to work with encryption Python module containing confidential information: logins, passwords.
    """

    def __init__(self, debug: bool = False) -> None:
        """
        Initialization of parameters.
        :param debug: Enable debug mode
        :return: none
        """
        self.debug = debug
        self.path = os.path.join(os.path.abspath(os.path.dirname(__name__)), "")
        self.key_filename = "crypto.key"
        self.key_path = self.path + self.key_filename

    def _write_key(self) -> None:
        """
        Encryption key generation.
        :return: none
        """
        key = Fernet.generate_key()
        with open(self.key_path, "wb") as key_file:
            key_file.write(key)

    def _load_key(self) -> bytes:
        """
        Reading the encryption key.
        :return: encryption key
        """
        return open(self.key_path, "rb").read()

    def _encrypt(self, decrypted_data: bytes, key: bytes) -> bytes:
        """
        Data encryption.
        :param decrypted_data: data for decrypt
        :param key: encryption key
        :return: decrypted data
        """
        f = Fernet(key)
        return f.encrypt(decrypted_data)

    def _decrypt(self, encrypted_data: bytes, key: bytes) -> bytes:
        """
        Data decryption.
        :param encrypted_data: data for encrypt
        :param key: encryption key
        :return: encrypted data
        """
        f = Fernet(key)
        return f.decrypt(encrypted_data)

    def return_secured_module(self, path_to_secured_module: str) -> dict:
        """
        Return the decrypted python secured module.
        :param path_to_secured_module: Path to source secured python module
        :return: dict
        """
        # Load the key
        key = self._load_key()

        # Read the file
        file = open(path_to_secured_module, "rb")
        encrypted_data = file.read()

        # Ger split string
        split_str = self._load_key()[-4:]

        # Get data
        all_data = encrypted_data.split(split_str)

        # Decryption process
        out_dict = {}

        for data in all_data[0:-1]:
            decrypted_data = self._decrypt(data, key)

            tree = ast.parse(decrypted_data)
            for node in tree.body:
                out_dict.update({node.targets[0].id: ast.literal_eval(node.value)})

        return out_dict

    def create_secured_module(
        self,
        path_to_opened_module: str = os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "secret.py"
        ),
        path_to_secured_module: str = os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "secured.py"
        ),
        create_key: bool = True,
        delete_source_opened_module: bool = False,
    ) -> None:
        """
        Encryption python module.
        :param path_to_opened_module: path to opened python module
        :param path_to_secured_module: path to secured python module
        :param create_key: create encryption key
        :param delete_source_opened_module: delete opened python module
        :return: none
        """
        # Write the key
        if create_key:
            self._write_key()

        key = self._load_key()

        file = open(path_to_opened_module, "rb")

        tree = ast.parse(file.read())

        # Create the empty file
        __empty_file = open(path_to_secured_module, "wb")
        __empty_file.close()

        # Take the last 4 symbols for split
        split_str = self._load_key()[-4:]

        # Encryption process
        with open(path_to_secured_module, "ab") as file:
            for node in tree.body:
                # if dict type
                if type(ast.literal_eval(node.value)) == dict:
                    _values = json.dumps(
                        ast.literal_eval(node.value), ensure_ascii=False, indent=2
                    ).encode("utf-8")
                # if other type
                else:
                    _values = json.dumps(
                        ast.literal_eval(node.value), ensure_ascii=False
                    ).encode("utf-8")
                # Encrypt
                _name = bytes(node.targets[0].id, encoding="utf-8")
                _ = _name + b" = " + _values
                encrypted_data = self._encrypt(_, key)
                file.write(encrypted_data + split_str)

        # Delete source python module
        if delete_source_opened_module:
            os.remove(path_to_opened_module)

    def create_opened_module(
        self,
        path_to_secured_module: str = os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "secured.py"
        ),
        path_to_opened_module: str = os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "secret.py"
        ),
    ) -> None:
        """
        Decryption python module.
        :param path_to_secured_module: path to secured python module
        :param path_to_opened_module: path to opened python module
        :return: none
        """
        # Load the key
        key = self._load_key()

        # Read the file
        file = open(path_to_secured_module, "rb")
        encrypted_data = file.read()

        # Get split string
        split_str = self._load_key()[-4:]

        # Get data
        all_data = encrypted_data.split(split_str)

        # Decryption process
        with open(path_to_opened_module, "wb") as file:
            for data in all_data[0:-1]:
                decrypted_data = self._decrypt(data, key)
                file.write(decrypted_data + b"\n")
