import os
# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from dotenv import load_dotenv
load_dotenv()

class Config:

    DEBUG = True
    DEVELOPMENT = True
    CSRF_ENABLED = True
    SECRET_KEY = 'secret'
    db_uri = 'postgresql://{}:{}@{}:{}/{}'.format(
                os.getenv('POSTGRES_USER'),
                os.getenv('POSTGRES_PASS'),
                os.getenv('POSTGRES_HOST'),
                os.getenv('POSTGRES_PORT'),
                os.getenv('POSTGRES_DB')
            )
    engine = db_uri
    if os.getenv('POSTGRES_USER'):
        engine = create_engine(db_uri, pool_pre_ping=True, poolclass=NullPool)
    

    PORT = os.getenv('PORT', 8080)
    HASH_KEY = os.getenv('HASH_KEY', None)

