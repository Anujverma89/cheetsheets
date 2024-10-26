# Sqlite
*Sqlite is a server less database with zero configuration that comes installed with many os like linux (ubuntu)*  
*No password and username configuration is required since it is used to embed with application*  
*It is a file based database*  
*It has sqlite engine that executes the sql quries*  
*It is a rdbms*  
*It doesnot support write concurrency i.e. one user can write at a time and multiple user can read at time*   
*It stores data in file in B-Tree and index is stored in B-Tree* 
*Sqlite is written in c language and it provides interface to work with different language*  
*It is a case insensetive*


**Flow of database**
| ->Frontend | ----Data to backend-----> | Backend | -------> connected to DB ----------> | DB Server or Databse |
|--------|----------|-------|--------------|----------|
| form data | post-get request | receive data at backend using request| sending data to database server | query received and being processed by engine | 
| html form | https | https | JDBC or ODBC or ORM | Database server eg. MySQL , or Sqlite |


**_Commands and syantx_**
| Command | use | Description | Note |
|-|-|-|-|
| ANALYSE database_name | analyse datase  | not available 
| sqlite3 databsename.db | create db in current directory | creates filename.db file in current location |
| attach database 'dbname.db' as 'db' | used to attach file to database after creating it|attaches the given database file to database | 'temp' and 'main' cannot be used |


