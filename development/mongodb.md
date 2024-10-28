# Mongodb
* Mongodb is a document based database which store data in json and bson form.
* Mongsh is a shell for working with mongodb
* Mongodb atlas is cloud based mongodb database
* Mongod is a deamon or process that runs while starting a database
* Runs at default port 27017

### Tutorial 
* Table is called Collection in mongodb.
* Row is called document in mongodb.
* Database is called database in mongodb.
* Database is not created unless there is any table in database.


| Commands | Use | comment |
|-|-|-|
| show dbs | to see all the databases | show databases is also used|
| use database | to work on current database | |
| show tables | to see all the tables in the database | show collections is also used  | 
| db.createCollection("tablename")| to create collection | collection is table |
| db.dropDatabase() | to delete database | Every table and data will be deleted | 
| db.collectionName.drop() | to drop table or collection | collectionname is anything |
| db.collectionName.insertOne() | to insert one | insertONe is case sensertive and its a function |
| db.collectionName.insertMany({},{},{}) | to insert many | to insert many | 
| db.CollectionName.findOne() | to find one | findMany() is also ther  findOne() retuns all the databases|
| db.collectionName.updateOne() | to update one | updateMany() is also there | 
| db.collectionName.delteOne() | to delete one | delteMany() is also there |
| db.collectionName.createIndex() | to create index | |
|db.collectionName.getIndexes() | to get index | | 



