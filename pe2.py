import rsa


def loadKeys(public_file_path, private_file_path):
    with open(public_file_path, 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open(private_file_path, 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())

    return publicKey, privateKey


def encrypt(message, key):
    # return rsa.encrypt(message.encode('ascii'), key)
    return rsa.encrypt(message.encode('UTF-8'), key)


def decrypt(ciphertext, key):
    # return rsa.decrypt(ciphertext, key).decode('ascii')
    return rsa.decrypt(ciphertext, key).decode('UTF-8')


# publicKey, privateKey = loadKeys()

# message = input('Write your message here:')
# ciphertext = encrypt(message, publicKey)

# text = decrypt(ciphertext, privateKey)

# # print(f'Cipher text: {ciphertext}')
# print(text)
