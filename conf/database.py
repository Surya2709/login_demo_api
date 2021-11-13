import os
# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, engine
from sqlalchemy.pool import NullPool
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


class Config:

    DEBUG = True
    DEVELOPMENT = True
    CSRF_ENABLED = True
    SECRET_KEY = 'secret'
    db_uri = 'postgres://{}:{}@{}:{}/{}'.format(
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

engine = Config.engine

session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = session.query_property()

