from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64


def generate_keys(bites: int = 2136) -> tuple[str, str]:
    """

    :return private_key, public_key: base64 encoded
    """
    key = RSA.generate(bites)
    private_key = base64.b64encode(key.export_key(format='DER')).decode('utf8')
    public_key = base64.b64encode(key.publickey().export_key(format='DER')).decode('utf8')
    return private_key, public_key


def encrypt_rsa(message: str, public_key: str) -> str:
    """

    :param message:
    :param public_key: base64 encoded
    :return: base64 encoded
    """
    encode_message = PKCS1_OAEP.new(key=RSA.import_key(base64.b64decode(public_key))).encrypt(message.encode('utf8'))
    return base64.b64encode(encode_message).decode('utf8')


def decrypt_rsa(message: str, private_key: str) -> str:
    """

    :param message: base64 encoded
    :param private_key: base64 encoded
    :return:
    """
    decode_message = PKCS1_OAEP.new(key=RSA.import_key(base64.b64decode(private_key))).decrypt(
        base64.b64decode(message))
    return decode_message.decode('utf8')


def encrypt_aes(message: str, secret: str) -> str:
    cipher = AES.new(secret.encode('ascii'), AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
    encoded_message = base64.b64encode(cipher.nonce + ciphertext).decode('utf-8')
    return encoded_message


def decrypt_aes(message: str, secret: str) -> str:
    decoded_message = base64.b64decode(message)
    nonce = decoded_message[:16]
    ciphertext = decoded_message[16:]
    cipher = AES.new(secret.encode('ascii'), AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode('utf-8')



# 88 бит + 2048 бит = 2136 бит

# private_key, public_key = generate_keys(2136)
# passwd = '1234567890123456'
# print("pub: ", public_key)
# print("private: ", private_key)
# print("passwd: ", passwd)
#
# enc_private_key = encrypt_aes(private_key, passwd)
# print("enc_private_key: ", enc_private_key)
#
# dec_private_key = decrypt_aes(enc_private_key, passwd)
# print("dec_private_key: ", dec_private_key)
#
# enc_passwd = encrypt_rsa(passwd, public_key)
# print("enc_passwd: ", enc_passwd)
# print("dec_passwd: ", decrypt_rsa(enc_passwd, dec_private_key))