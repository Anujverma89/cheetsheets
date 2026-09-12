# PostgreSQL 
* PostgreSQL is an ORDBMS system based on postgres version 4.2 which was developed at university of California at berkeley.
* It is a descendant of berkeley code.
* It is open source project which can be extended according to the need of the user.

# Installation : 
* Is available in Ubuntu directly.
* But you can install it on any other platform using the the installation guide given in postgreSQL documentation.
* Yoou can download the source file and then you can compile the given soruce code and then you can execute.
* PGHOST : Tell's on which machine the postgreSQL is.
* PGPORT : Say's on which port the postgreSQL is.



# Architecture : 
* Client : web app, app, etc 
* Server : Postgres
* Client connects to server and get and posts some data in the server.
* Server can handle multiple clients connection using Fork 
* Concurrency: The main server process listens for connections and spawns (forks) a new process for each client. The client then communicates directly with its dedicated server process.


# Authentication : 
* It helps us to establish connection with database.
## Methods : 
* **Peer**
    * switch user : sudo -i -u postgres(since postgres exists on both system and database when we install postgreSQL)
    * user must exist on both system and postgres
    * First create role. 
    * Then create user in system,
    * Then switch user sudo -i -u user
    * then run psql : you will be logged in
* **Password**
    * First create the user add password then you can login using this method.
    * psql -U user_name -d db_name -h 127.0.0.1 -p 5432 => If you use this you will be prompted to enter a password.


# First initial setup : 
* When you install the postgres and it runs on the local machine.
* postgresSQL create a new user called postgres.
* Now you can use peer login to access postgreSQL since postgres is both present in system and server.
* This is peer login .
**After this you can setup new password for connection with client and backend**


# PSQL : 
* psql is an interactive shell for connecting and communicating with server.





# SQL language :
* Strings start with single quote 'string'
* =

## shell commands start with this $ : 
* createdb db_name = " Creating new db"
* psql db_name = " To use the database"
* psql = "if you type just this then default database name will be user one"
* ALTER ROLE role_name WITH LOGIN NEWPASSWORD 'pass' CREATEROLE.
* select * from table where uname = 'anuj';
* INSERT INTO weather(name, rollno, city) VALUES('anuj', 23, 'pune')
* COPY weather FROM '/home/user/weather.txt'; => this can be used to load the data from the files
* inserting multiple rows in a table using the data stored in a txt file.
* /copy data from '\home\anuj\Desktop\tutorials\data.txt' DELIMITER ',' CSV; /copy data from 'path' DELIMITER '' filetype : used to inserted multiple rows directly into table.
 


## SQL commands start with =# or => and run inside psql: 
*\du - list all role and users in db. 
*\list - list all the databases.
*\c db_name - to use database.
*\dt - to list all the tables;
*show port : to list the port in which it is running;
*\i basics.sql : to execute the sql command in psql 
*user is a reserved keyword in postgreSQL so we can't use it now.


# SQL (Structured Query Language)  : 
* DDL : Data defination language - (Create, alter, drop, truncate) 
* DQL : Data Query language - (select) 
* DML : Data manipulation language - (insert, update, delete) 
* DCL : Data control language -  (Grant, Revoke) 
* TCL : Transaction control language -  (commit, rollback, savepoint)


## DQL : fetching data from one single table at once
* Select * from table; == select everything from table
* select columnname from table; == select some specific columns from table;
* select * from tablename where (some condition); select something where some conditions are true;
* select distinct columnname from tablename; == Select distinct element from columname
* select * from tablename order by columnname; == Arrange the data in some order

## Joins : 
* ->to fetch data from two or more different tables and present them as one table;
* Inner join, outer join, 



## Aggregate functions : 
* **Aggregate functions are the function used to calculate the single output from multiple input rows**.
* 
* 



# Note : 
* we create table, delete table and use table from user.(inside terminal with user available in db)
* we run sql commands from psql(insite psql)
* Role and databases are different.
* default port for postgres : 5432



# Database : 
* Driver : Connect with database using database native method
* ORM : Convert the class & Object native code into the SQL 

# user-> Frontend -> (rest,graphsql,websocket) over https/http -> Backend -> (database driver) over native methods -> Database


# pg driver : 
* nextjs driver : pg 
* flutter driver : postgres 
* Drivers are provided by the database vendor itself.




# Connection pooling : 
* Means to establish multiple connections with database.
* We can assign the max no in the connection list.
* Imagine a scenerio when there are 100 of users making request to web which needs database connectivity.
* when request comes backend makes connection upto max pool limit.
* Each request takes one connection until it needs it and once the response is returned the connection becomes idle.
* When all the connections are idle some of them are disconnected while others still stay connected to further process.



# Schema : 
* Schema is a logical structure for database. 
    * It's not the structure for the table but for the database.


    
# Database setup in production
* Okay so we mostly use ORM for production. 
* We don't have to write SQL on development and production environment it is handled by ORM.
* If you have something like django you know what is ORM, ORM bascially generates the sql code from python classes.
* If you make any changes in table schema we can use ORM to upate the table and data won't be lost.
* We always have to use migrations with ORM never deletee for truncate teh table manually.


# Interface : is a medium using which we can interact with system.
    * Interface gives us a method to define and interact with existing system by defining own code. 
    * Is a way to interact with system in general way.
# Classes : Define a user define data structure along with the code to interact with that data.
# Encapsulation : Combining both data and operation on data together.
# Inheritance : To inherit the feature of something.
# Abstraction : Hiding implementation detail.
# Polymorphism : One class does multiple things. ( Method Over riding, over loading)


# NOTE : 
    * Install server ( already installed ) in ubuntu. 
    * login using the peer login - postgres( system user name )  , postgres database user. 
    * create new user , password.
    * create database.
    * connect with the connection url using sqlalchemy.
    * get connection.
    * perform execution. 
    * define data and schema using sqlalchemy.orm DecleartiveBase and column_mapper, Mapped[a].
    
    

# Installation : 
* `Binary Package` You can install it from binary packages ( means packaged applications like .deb, .apk). They are pre compiled. 
* `Source code` : For someone who is looking to develop for postgres, it is recommended for him/her to build from scratch.


# Configuration : 
* `Database cluster` : A database cluster is an area on a disk where all database files are stored. It is also a collection of all the databases that are accessed and managed by single instance of running server. `SQL Standard : Catalog Cluster`
* One db server can have only one Database cluster 
* setup using `initdb -D /usr/var/pgsql/data` here -D stands for data directory 
* We can also connect `NFS ( network file system ) and file system` with any server instance. 


# PostgreSQL : Is a object relational database management system (ORDBMS) 
* It is free of cost and can be modified, distributed and used for any purpose.
Fast performing, free and OpenSource database 

# History : 
    * POSTGRES(1986) -> Barkely postgres project 
    * postgres95 -> added SQL in POSTGRES
    * postgreSQL officially named

# Architecture : 
    * Client (any clinet like webapp, mobileapp)
    * Server (postgres)


# Installation and configuration 
* Install it using apt command becuase it is available opensource
    * sudo apt install postgresql
* Running, stoping and checking as service 
    * systemctl status postgresql
    * systemctl stop postgresql
    * systemctl restart postgresql
    * systemctl start postgresql
* we can install from binary because they are precompiled.
* we can also build from source code as wll

    
# Peer login : 
* Peer authentication method : 
* It is used by Postgres to validate the user against the postgres user.
* Lets take an example 
* The user of os is anuj and is currently switched to anuj account 
* now when we run psql (It checks if the current os user is available in postgres)
* If yes then it allows to login else rejects.
* We cannot use password and username for login in peer login unless we modify the configuration.

    
    


# Authentication setup 
current password : ( user : root ) ( password : aahar)
* Login using user and password : psql -U root -W 
* password
* sudo -u postgres psql (Using superuser login user) and no password
* postgres uses a peer authentication method by default 
* postgres is a super user 



# Commands and syntax 
```JS
    $ -> stands for shell
    => stand for sql 
```

<!-- $createdb databasename -->



# Running on terminal 


# psql  ( PostgreSQL Interactive terminal)
* psql is a postgresql shell which is used to interact with postgres server 
* psql command tries to connect with postgres server 
* it requires user and password for the same purpose
* psql doesnot required password unless we don't modify the configuration file and the peer is set to md5
* we can modify this file `sudo nano /etc/postgresql/*/main/pg_hba.conf` to change the method of authentication from peer to password


# Configuration & Setup : 
* A database cluster is a collection of databases that is managed by a single instance of a running database server



# password and user 
* ubntai - user 
* ubntaihome - pass
* you have to grant permission to user for doing different stuff


# MongoDB with django ( Note mongo by default only works with Relational database)
* Connecting MongoDB with Django can be done using few libraries : 
    * PyMongo (Most prefered one for working, it's also standard one)
    * Djongo (used when migrating from sql to mongodb so don't have to change schema)
    * MongoEngine (Object Document Mapper, Provides Declarative API ) 
    * The way to use mongodb in django is similar to other frameworks like node and all

* Terminology : 
    * Database : Database
    * Collection : table 
    * Document : Rows 
    * field : columns 
    
    
# Inorder to send mail from django 
* Django uses django mailer 
* we have use all our cerdentials 
* Inorder to use the google account we have to use smtp server and we have to turn on 2FA as well.
* We have to generate application specific password and use it

# "I was born alone, I'm a alone. Nothing else." I have to give not except.


