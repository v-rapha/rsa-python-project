import os
from pc1.index import main_func as main_func_pc1
from pc2.index import main_funcPc2 as main_func_pc2
from rsa_functions import generateKeys


def main():
    pc1_pub_key_path = 'pc2/publicKey_pc1.pem'
    pc1_pvt_key_path = 'pc1/privateKey_pc1.pem'
    pc2_pub_key_path = 'pc1/publicKey_pc2.pem'
    pc2_pvt_key_path = 'pc2/privateKey_pc2.pem'

    pc1_pub_key_exists = os.path.exists(pc1_pub_key_path)
    pc1_pvt_key_exists = os.path.exists(pc1_pvt_key_path)
    pc2_pub_key_exists = os.path.exists(pc2_pub_key_path)
    pc2_pvt_key_exists = os.path.exists(pc2_pvt_key_path)

    if (pc1_pub_key_exists and pc1_pvt_key_exists) and (pc2_pub_key_exists and pc2_pvt_key_exists):
        flag = True
        while flag:
            print('(1) Acessar como pc1')
            print('(2) Acessar como pc2')
            op = int(input('Opção: '))

            if op == 1:
                main_func_pc1()
                flag = False
            elif op == 2:
                main_func_pc2()
                flag = False
    else:
        generateKeys(pc1_pub_key_path, pc1_pvt_key_path)
        generateKeys(pc2_pub_key_path, pc2_pvt_key_path)


if __name__ == "__main__":
    main()
