import rsa
import os
from pe2 import loadKeys, encrypt, decrypt

# Função responsável por gerar as chaves
def generateKeys(public_key_path, private_key_path):

    pbc_path_exists = os.path.exists(public_key_path)
    pvt_path_exists = os.path.exists(private_key_path)

    if not (pbc_path_exists and pvt_path_exists):
        (publicKey, privateKey) = rsa.newkeys(2048)

        with open(public_key_path, 'wb') as p:
            p.write(publicKey.save_pkcs1('PEM'))
        with open(private_key_path, 'wb') as p:
            p.write(privateKey.save_pkcs1('PEM'))


def main_funcPc2():
    # Mudar o comportamento das variáveis
    # public_file_path = 'pc1/publicKey_pc2.pem'
    # pub_key_path = 'pc1/publicKey_pc2.pem'
    pvt_key_path = 'pc2/privateKey_pc2.pem'
    pc1_pub_key_path = 'pc2/publicKey_pc1.pem'

    # generateKeys(pub_key_path, pvt_key_path)
    pbc_key, pvt_key = loadKeys(pc1_pub_key_path, pvt_key_path)

    print("(1) Criptografar")
    print('(2) Descriptografar')
    op = int(input('Opção: '))
    if op == 1:
        message = input('Write your message here:')
        msg = encrypt(message, pbc_key)
        with open('msg_pc2.txt', 'wb') as f:
            f.write(msg)
    elif op == 2:
        msg = ''
        if os.path.exists('msg_pc1.txt'):
            with open('msg_pc1.txt', 'rb') as f:
                msg = decrypt(f.read(), pvt_key)

            print(msg)
        else:
            print('File not found')
