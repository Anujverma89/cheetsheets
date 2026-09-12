# alembic : 
* Alembic is a migration tool used in python often with sqlalchemy. 


# alembic : 

## Now imagine a situation that you need to change something in database in production. 
* If you two options without migration tools : 
    * First delete everything and create new from scratch. 
    * Write manual SQL queries and run them 
* When we have migration tool like alembic : 
    * It tracks the changes in the code and matches with db. 
    * All the changes are generated as a code and later flushed in db.


## Alembic setup : 
* First install it using uv install alembic.
