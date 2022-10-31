import rsa


def generateKeys(public_key_path, private_key_path):
    (publicKey, privateKey) = rsa.newkeys(2048)

    with open(public_key_path, 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open(private_key_path, 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))


def loadKeys(public_file_path, private_file_path):
    with open(public_file_path, 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open(private_file_path, 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())

    return publicKey, privateKey


def encrypt(message, key):
    return rsa.encrypt(message.encode('UTF-8'), key)


def decrypt(ciphertext, key):
    return rsa.decrypt(ciphertext, key).decode('UTF-8')
