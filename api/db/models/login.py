from sqlalchemy.inspection import inspect
from sqlalchemy import Column, Integer
from sqlalchemy.sql.sqltypes import String
from conf.base import Base
from sqlalchemy.dialects.postgresql import UUID

class user_login(Base):

    __tablename__ = 'user_login'

    id =  Column(Integer(), autoincrement= True, unique = True, primary_key = True)
    user_id = Column(UUID(as_uuid=True), unique = True, nullable = False)
    user_name = Column(String(50),unique = True,nullable=False)
    user_pass = Column(String(50),nullable=False)

    def to_dict(self):
        res =  {c: getattr(self,c) for c in inspect(self).attrs.keys()}
        return res

                                                          