# SQLAlchemy : A tool used for python language used to interact with Database. 

## Parts : 
* Core : Engine( for connection ), Transation , SQL execution
* ORM : Mapping db table with python object 

## Reading core now : 
* Engine : Engine is a way to connect with database and it holds the connection pool required to make connection
```py
    from sqlalchemy import create_engine

    # engine is part of core and is used to connect with the db server for further operation 
    # it holds connection to the server and connection pool
    engine = create_engine("url_to_bb", config_option)

'''
    url = dialect+driver://user_name:password@IP:port/databasename
    dialet = domain db translator of raw python
    driver = carrier of data 
    user_name = db_username
    password = db_password
    ip = IP 
    port = port at which db is running
    database_name = name of the databse you want to connect
'''
```


## Core :           
    * Engine -> Connection -> Query -> Execution -> result -> 
    * Language depended code -> dialect -> Driver -> db server ( Execution )              


## Engine is a way to connect with database server 
```py

    with engine.connect() as conn: 
        conn.execute(text("INSERT INTO some_table (X,Y) where values(:X, :Y)"),values({"x":12,"y":14}))
        conn.commit()

    
    # conn.execute() is a code for execution 
    # conn.commit() is used to commit()
    # if we don't commit the transaction will roll back
    # connection executes the raw sql

```



## Session in orm 

```py
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Sessoin

    engine = create_engine(url)

    with Session(engine) as session: 
        yeild sesssion


    session.add()
    session.commit() # open conn and perform action 

    # session has much more to do then just executing raw sql 
    # session tracks the object in memeory 
    # tracks the lifecycle 
    # converts the pythong code in sql 
    # opens up a connection 
    # executes it if commited 


```


## Working with ORM to create Tables, MetaData, Column 
```py
    from sqlalchemy import MetaData, Column, Table 

    meta_dataobj = MetaData() # metadata object is an object which contians all the tables keyed to it's name


    user_table = Table(
        "user_table",
        meta_dataobj,
        Column("id", UUID(), unique = true)
    )

    # here this user_table is attached to meta_dataobj
    meta_dataobj."user_table" # will print 


```



# Topics : 

## Connection 

## Metadata 
* There should be only one metadata per application for a convinience and maintenance
* `meta_dataobj.create_all()` to create all database tables. 
* `meta_dataobj.drop_all()` to drop all database tables.
* however these are only suitable for small use cases and small applications for large apps we should use  `Alembic`

## ORM : Class based data manuplation  

## Query & Transaction execution 



* `MetaData object` contains info about `Table object` info 
    * table contains `Column Object` 
        * Columns contains `Datatypes` and `ConstraintsObject` 
            * Columns of a table can be accessed using a object c  `table_name.c`


# Execution 
`Database Server` -- `Client Interface` -- `Client` 

* Client Interface : Helps to connect the database server with client 
* Every client has client specific client interface 


## PostgreSQL 
* libpq : Client interface for c lanauge to connect with db.
* ECPG : Client interface for c to write native SQL inside C code.


* python : 
    * asyncpg - async connector for python 
    * psychopg2 - sync connector for python 


* DB server connection ways : 
* from programming language - language interface 
* from cli - Cli interface (psql)
* from GUI - GUI interface ( pg admin )




## Dependency Injection : 
* Dependency injection is a way to achieve loose coupling by delegating the work of object creation to dependency injection provider. 
* `ways to achieve dependency injection `
    * Constructor injection ( most common)
    * Variable assignment 
    * Setters 
    * through dependency injection managers 



## Important parts in DB ( SQL )
* Installation 
* Server configuration 
* Server programming ( PSQL : Procedural SQL )
* Client interfaces ( way to connect to server)
* SQL Syntax 
* Migration & Upgrade 




## Regression Testing : 
* Regression testing is a way to ensure that, the new feature realease doesn't breaks the existing system or we can say it's a way to check the compatibility of the new feature with older system.


## Foreign Key : 
* Only a dependent cloumn has a foreign key pointing to the depending column like address has foreign key to the user.


## SQL Expression language : 
* SQL expression language in python is a way to write a SQL query using python construct. 
* SQL expression language in SQL is a expression that evaluates to a single query e.g. a mathematical expression. 


## Database reflection : 
* Database reflection is a way to create a python object or table metadata from existing database tables. 
```py

user_table = Table(
    "table_name",
    metadata,
    autoload_with = engine
)

# this automatically creates user_table metadata with from exisiting table
# this helps to perform a query operations on the database tables operations. 
```


## working with data 
* Insert operation with insert function 
* select operation with select function 
* Update and delete operation 

```py

    from sqlalchemy import insert, select, update, delete 

    stmt = insert(user_table).values(name="ANuj", age = 24)
    stmt.compile()

    engine = create_engine("db_url")
    with engine.connect() as conn:
        conn.execute(stmt)



    # this is the core way of working with data manuplation in case you don't use ORM 
```



## data manipulation using ORM 
```py
    from sqlalchemy.orm import session 
    from sqlalchemy import create_engine

    engine = create_engine()

    with Session(engine) as session:
        yeild session 
    

    session = next(session)

    session.add(obj)
    session.commit()

```

* Identity map : In memory store for the python objects it's unique and it mostly tracks the primary key for the object, two object with same primary key will always be same.
* flush : flush writes a query in the database.
* commit : commit commits the transaction.
* autoflush : when authflush is enabled chages are automatically pushed into db
* dirty : when python object in memory changes. 
* Transient state : object in a memory but not in session.


* create an object - add to session -> make changes -> flush it -> commit it()


### in sqlalchemy construct usually means the python object that resembles something in SQL be it statement, element or schema defination eg, Table, Colum, Constratints , MetaData(), relationship()


## Object states in sqlalchemy 
* transient : When object is created but not in session.
* pending : when object is added to the session. Session.add()
* persistant : when data is written to the db after flush and commit or it already exists in db
* detach : when object gets detached from the session.


## Dialet : 
* Dialet in sqlalchemy is a translator that transalte the python object into db specific query. 



## DPAPI or database driver : 
* dbapi is a way through which the backend communicates to with db server. 
* It is resonsible for establishing communication with db server using tcp-ip.



## Registory in orm ::
* It is a tool to keep the track of python classes and the communication and linking between db tables and python classes. 
* `Metadata` holds the configuration data about table
* Registory uses `metadata` & `python class` to fasciliate the automatic query creation. 



## Loading stratigies :: 
* When we have to query data between tables which are internally related we need joins. 
* In ORMS there are loading stratigies that are used to load data from related table. 
* `lazy` : `lazy loading by  lazy = raise` it creats N+1 problem 
* `joinedload` : makes a join query to load data. `select(User).options(joinedload(User.addresses))`
* `selectin` : It solves the problem of N+1 in two queries 1 for main query and other for related queries 
* `subqueryload`
* `lazy options` : `lazy = no-load || raise_on_sql`
* `immediateload` : 
* `contains_eager`: `options(contains_eager(User.addresses)`


## Ways we can connect classes with DB in orm 
* Implicit decleration : Using declerative base 
```py
    class Base(DeclerativeBase):
        pass

    class User(Base):
        pass 

```

* Explicit configuratioon : reg = registory() map it to class using decorator @reg.mapped
```py
    reg = registory()

    reg.mapped
    class Object:
        pass
        # this class is not mapped class
```


* imperative mapping : 
```py
    reg = registory()

    user_table = Table(
        "user", 
        reg.metadata,
        Column("name", Integet, primary_key = true)
    )

    class User:
        pass

    reg.map_imperatively = (User,user)
```