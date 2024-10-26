# Sqlite
*Sqlite is a server less database with zero configuration that comes installed with many os like linux (ubuntu)*  
*No password and username configuration is required since it is used to embed with application*  
*It is a file based database*  
*It has sqlite engine that executes the sql quries*  
*It is a rdbms*  
*It doesnot support write concurrency i.e. one user can write at a time and multiple user can read at time*   
*It stores data in file in B-Tree and index is stored in B-Tree* 
*Sqlite is written in c language and it provides interface to work with different language*  

**Flow of database**
| ->Frontend | ----Data to backend-----> | Backend | -------> connected to DB ----------> | DB Server or Databse |
|--------|----------|-------|--------------|----------|
| form data | post-get request | receive data at backend using request| sending data to database server | query received and being processed by engine | 
