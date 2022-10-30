import rsa
import os
from pe2 import loadKeys, encrypt, decrypt


def generateKeys(public_key_path, private_key_path):

    pbc_path_exists = os.path.exists(public_key_path)
    pvt_path_exists = os.path.exists(private_key_path)

    if not (pbc_path_exists and pvt_path_exists):
        (publicKey, privateKey) = rsa.newkeys(2048)

        with open(public_key_path, 'wb') as p:
            p.write(publicKey.save_pkcs1('PEM'))
        with open(private_key_path, 'wb') as p:
            p.write(privateKey.save_pkcs1('PEM'))


def main_func():
    public_file_path = 'pc2/publicKey_pc1.pem'
    private_file_path = 'pc1/privateKey_pc1.pem'
    public_file_path_pc2 = 'pc1/publicKey_pc2.pem'

    generateKeys(public_file_path, private_file_path)
    pbc_key, pvt_key = loadKeys(public_file_path_pc2, private_file_path)

    print("(1) Criptografar")
    print('(2) Descriptografar')
    op = int(input('Opção: '))
    if op == 1:
        message = input('Write your message here:')
        msg = encrypt(message, pbc_key)
        with open('msg_pc1.txt', 'wb') as f:
            f.write(msg)
    elif op == 2:
        msg = ''
        with open('msg_pc2.txt', 'rb') as f:
            msg = decrypt(f.read(), pvt_key)

        print(msg)
