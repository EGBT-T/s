from sqlalchemy import create_engine, Table, MetaData, Column, String, Integer
from sqlalchemy.dialects.mssql import insert
import pandas as pd
import numpy as np
engine = create_engine('')

metadata = MetaData()

class tb:
    my_table = Table(
        'table', metadata,
        Column('id', Integer, primary_key=True),
        Column('va', Integer)
    )

cl = tb()
cl_att = cl.my_table

df = pd.DataFrame({'id': list(range(12, 21)), 
                   'va': np.random.randint(9, 10, 9)})

isrt = insert(cl_att).values(df.to_dict(orient='records'))
uprt = isrt.on_duplicate_key_update(
    va = isrt.inserted.va
)

with engine.connect() as conn:
    conn.execute(uprt)
