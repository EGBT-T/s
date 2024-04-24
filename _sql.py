import sqlalchemy
from sqlalchemy import create_engine, insert, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

import pandas as pd

# strConn = 'DRIVER=SQL SERVER;SERVER={S};UID={U};PWD={P};DATABASE={D};charset=utf8' \
#             .format(S=self.Server, U=self.UserID, P=self.Password, D=self.Database)

Base = declarative_base()

class User(Base):
    __tablename__ = 'test_table'
    name = Column(String(64), primary_key=True)
    nick = Column(String(255))

stmt = insert(text('test_table')).values(name='name_str', nick='nick_str')

engine = create_engine('mysql+pymysql://root:PASSWORD@host/database')
conn = engine.connect()
result = conn.execute('INSERT INTO test_table(name, nick) VALUES (%s, %s)', ('df_name_test', 'df_nick_test'))

d = {'name': ['df_name_1', 'df_name_2', 'df_name_3'], 'nick': ['df_nick_1', 'df_nick_2', 'df_nick_3']}

df = pd.DataFrame(data=d)
df.to_sql(name = 'test_table', con = conn, if_exists='append', index=False)

__r = result.fetchall()
conn.commit()

for i in __r:
    print(i)
cnx = engine.connect()
with engine.connect() as conn:
    conn.execute(stmt)
    conn.commit()
DBSession = sessionmaker(bind=engine)
session = DBSession()
new_user = User(name='df_name_test', nick='df_nick_test')
session.add(new_user)
session.commit()