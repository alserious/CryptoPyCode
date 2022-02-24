import os

from cryptopycode.cryptopycode import CryptoModule

crypto_module = CryptoModule()

# encrypt
# read decrypted secret.py file and create encrypted secured.py file
crypto_module.create_secured_module(
    path_to_opened_module=os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "secret.py"
    ),
    path_to_secured_module=os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "secured.py"
    ),
    create_key=True,
    delete_source_opened_module=False,
)

# decrypt
# read encrypted secured.py file and create decrypted secret.py file
crypto_module.create_opened_module(
    path_to_secured_module=os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "secured.py"
    ),
    path_to_opened_module=os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "secret.py"
    ),
)
