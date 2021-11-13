from conf.database import Config
from cryptography.fernet import Fernet


def encrypt_pass(password):

    key = Config.SECRET_KEY
    cipher_suite = Fernet(bytes(key))
    encrypted_pass = cipher_suite.encrypt(bytes(password))
    return encrypted_pass


def check_registration(body):

    resp = "working"
    return resp


def login(body):

    return "login"