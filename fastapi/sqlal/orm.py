# orm is used to create a db using ORM style configuration : 
# Object realtion mapping 

from sqlalchemy.orm import Mapped 




## Mapped class : mapped class is a class that resembles a table in a database ( Mapped classes = Tables )
## Column : columns are represented using mapped_column()
## Datatype annotation : name:Mapped[String] : = mapped_column(primary_key = True)

## DeclerativeBase : MetaData, Registory 