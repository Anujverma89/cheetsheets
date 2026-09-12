from sqlalchemy import Table, Column, Integer, String, create_engine, text, MetaData,String, insert, select


# create engine 
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


# getting connection 
def getconn():
        yield engine.connect()



# meta data object
meta_dataobj = MetaData()


# creating table 

user_table = Table(
    "user",
    meta_dataobj,
    Column("id", Integer, primary_key = True),
    Column("name", String, nullable = False)
)


# conn = next(getconn())
# conn.execute(text("select 'hello world'"))

print(meta_dataobj.tables) # reading all the tables
print(dir(meta_dataobj))
meta_dataobj.create_all(engine) # this can create table 
# meta_dataobj.drop_all(engine) # this drops all the tables 
meta_dataobj.reflect(bind = engine)


with engine.connect() as conn:
    result = conn.execute(
        text("INSERT INTO user (name) VALUES (:name)"),
        ({"name":"Anuj"},{"name":"Sujal"},{"name":"Hari"},{"name":"Anuj"},{"name":"kishan"}) # multivvalue 
    )
    conn.commit()



with engine.connect() as conn:
    result = conn.execute(
        text("SELECT * FROM user WHERE user.id == 1")
    )
    for r in result:
         print(r)


stmt = insert(user_table).values(name="kumesh")
compiled = stmt.compile()
print("compiled",compiled, compiled.params)

newstmt = insert(user_table)
compilednew = newstmt.compile()
print(compilednew)

# we can pass params directly whiel executing 
# here we can use insert directly 
with engine.connect() as conn:
    conn.execute(
        stmt,[{"name":"shyam"},{"name":"Hair"}]
    )
    conn.commit()
    result = conn.execute(
        select(user_table).where(user_table.c.name == "Hair")
    )
    for r in result:
        print(r)
    conn.commit()


# print(user_table.c.id)



# def yeildNumb():
#         yield 1

# numb = yeildNumb()
# print(next(numb))
# print(type(numb)) this prints a generator function 

# dialet:driver(dbapi):///user:password:ip:port/database


# Note : connection doesnot makes automatic connects 






