# NQ Decrypt
A tool to decrypt files encrypted by NQ Vault

## Requirements
* Python 3.5 or higher

## Installation

clone the repo using `git clone https://github.com/prmsrswt/nqvault-decrypt` or by downloading the zip from the button top right corner.

## Usage

copy the vault.py in the directory which contains all your encrypted files and run
```
python vault.py
```

done!

## How does nq-vault works?

- XOR first 3 bytes of file with pre-defined 3 bytes to get a result
- Use first part of result to XOR all first 128 bytes of the original file
- The above generated file is the encrypted file

## How does this program works?

As XOR is reversible in nature, we use the same steps to decrypt the first 128 bytes of the file.