import argparse
import os
import sys

from cryptopycode.cryptopycode import CryptoModule


def create_parser():
    parser = argparse.ArgumentParser(
        prog="cryptopycode",
        usage="%(prog)s [options]",
        description="Script for encryption and decryption Python modules.",
    )
    parser.add_argument(
        "-n",
        "--name",
        help="Name of file with confidential information",
        type=str,
        dest="name",
        default="secret.py",
    )
    parser.add_argument(
        "-p",
        "--path",
        help="Path to file with confidential information",
        type=str,
        dest="path",
        default=os.path.join(os.path.abspath(os.path.dirname(__file__)), ""),
    )
    parser.add_argument(
        "-k",
        "--key",
        help="Choice of <encrypt> and <decrypt> python module",
        type=str,
        dest="key",
        choices=["encrypt", "decrypt"],
    )
    return parser


if __name__ == "__main__":
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    module = CryptoModule()

    if namespace.key == "encrypt":
        path_opened = os.path.join(namespace.path, namespace.name)
        secured = "secured_" + namespace.name
        path_secured = os.path.join(namespace.path, secured)
        module.create_secured_module(
            path_to_opened_module=path_opened, path_to_secured_module=path_secured
        )
        print(f"Created file: {secured}")

    elif namespace.key == "decrypt":
        path_secured = os.path.join(namespace.path, namespace.name)
        opened = "opened_" + namespace.name
        path_opened = os.path.join(namespace.path, opened)
        module.create_opened_module(
            path_to_secured_module=path_secured, path_to_opened_module=path_opened
        )
        print(f"Created file: {opened}")
