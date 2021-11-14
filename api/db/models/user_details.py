from sqlalchemy.inspection import inspect
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql.sqltypes import String
from conf.base import Base
from sqlalchemy.dialects.postgresql import UUID

class user_details(Base):

    __tablename__ = 'user_details'

    id =  Column(Integer(), autoincrement= True, unique = True, primary_key = True)
    user_id = Column(UUID(as_uuid=True), unique = True, nullable = False)
    first_name = Column(String(50),unique = True,nullable=False)
    last_name = Column(String(50),nullable=False)
    dob = Column(DateTime(), nullable= False)

    def to_dict(self):
        res =  {c: getattr(self,c) for c in inspect(self).attrs.keys()}
        return res
