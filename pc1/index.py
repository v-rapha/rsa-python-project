import os
from rsa_functions import loadKeys, encrypt, decrypt


def main_func():
    pvt_key_path = 'pc1/privateKey_pc1.pem'
    pc2_pub_key_path = 'pc1/publicKey_pc2.pem'

    pbc_key, pvt_key = loadKeys(pc2_pub_key_path, pvt_key_path)

    print('(1) Para criptografar')
    print('(2) Para descriptografar')
    op = int(input('Opção: '))
    if op == 1:
        message = input('Escreva sua mensagem: ')
        msg = encrypt(message, pbc_key)
        with open('msg_pc1.txt', 'wb') as f:
            f.write(msg)
    elif op == 2:
        msg = ''
        if os.path.exists('msg_pc2.txt'):
            with open('msg_pc2.txt', 'rb') as f:
                msg = decrypt(f.read(), pvt_key)

            print(msg)
        else:
            print('Arquivo de mensagem não encontrado.')
