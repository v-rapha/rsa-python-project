import rsa

def generateKeys():
    (publicKey, privateKey) = rsa.newkeys(2048)
    with open('pc2/publcKey_pc1.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open('pc1/privateKey_pc1.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))

generateKeys()
