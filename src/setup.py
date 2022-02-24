import setuptools

setuptools.setup(
    name="cryptopycode",
    version="0.0.4",
    author="alserious",
    description="Script for encryption and decryption Python modules",
    url="https://github.com/alserious/cryptopycode",
    packages=setuptools.find_packages(),
    install_requires=["cryptography"],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 2.7, 3.6, 3.7, 3.8, 3.9, 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires="2.7, 3.6, 3.7, 3.8, 3.9, 3.10",
)
