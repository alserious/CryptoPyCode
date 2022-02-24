### Cryptopycode

#### Script for encryption and decryption Python modules

##### You need to install the package

```bash
pip install cryptopycode
```

##### Can be used as commands for python

```bash
python3 -m cryptopycode --help
python3 -m cryptopycode -n secret.py -k encrypt
python3 -m cryptopycode -n secured.py -k decrypt
```

##### Can be imported to you project

###### imports

```python
import os

from cryptopycode import CryptoModule
```

###### get crypto module instance

```python
crypto_module = CryptoModule()
```

###### encrypt

###### open decrypted file with name "secret.py" and create encrypted file with name "secured.py"

```python
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
```

###### decrypt

###### open encrypted file with name "secured.py" and create decrypted file with name "secret.py"

```python
crypto_module.create_opened_module(
    path_to_secured_module=os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "secured.py"
    ),
    path_to_opened_module=os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "secret.py"
    ),
)
```
