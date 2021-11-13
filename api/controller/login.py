from cryptocode import decrypt
from cryptocode.myfunctions import encrypt
from api.db.models.login import user_reg
from conf.database import Config
import cryptocode
from conf.base import session
import uuid
from Crypto.Cipher import AES
import traceback


def encrypt_pass(password):

    key = str(Config.SECRET_KEY)
    
    encrypted_pass = cryptocode.encrypt(password,key)
    return encrypted_pass



def registration(body):
    try:
    
        user_name = body.get('user_name',None)

        if session.query(user_reg).filter(user_reg.user_name==user_name).first():
            resp = { "resp" : "user name already exist"}
            return 400,resp

        user_pass =  body.get("user_pass",None)

        pass_ = encrypt_pass(str(user_pass))

        obj = { "user_id" : uuid.uuid4(),"user_name" : "surya", "user_pass" : pass_ }
        u = user_reg(**obj)
        session.add(u)
        session.commit()
        resp = { "resp" : "registration successfull"}
        return 200,resp
    except:
        session.close()
        print(traceback.print_exc())
        resp = { "resp" : "registration failed"}
        return 400,resp

def login(body):

    user_name_ = body.get('user_name',None)
    user_pass =  body.get("user_pass",None)

    user_data = session.query(user_reg).filter(user_reg.user_name==user_name_).first()
    
    if not user_data:
        resp = { "resp" : "user name does not exist"}
        return 400,resp

    print(user_data.user_pass)
    pass_ = decrypt(str(user_data.user_pass),str(Config.SECRET_KEY))

    if user_pass==pass_:
        resp = { "resp" : "success"}
        return 200,resp
    resp = { "resp" : "Invalid Password"}
    return 400,resp
    

