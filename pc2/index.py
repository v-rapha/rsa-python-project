import os
from rsa_functions import loadKeys, encrypt, decrypt


def main_funcPc2():
    pvt_key_path = 'pc2/privateKey_pc2.pem'
    pc1_pub_key_path = 'pc2/publicKey_pc1.pem'

    pbc_key, pvt_key = loadKeys(pc1_pub_key_path, pvt_key_path)

    print('(1) Para criptografar')
    print('(2) Para descriptografar')
    op = int(input('Opção: '))
    if op == 1:
        message = input('Escreva sua mensagem: ')
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
            print('Arquivo de mensagem não encontrado.')
