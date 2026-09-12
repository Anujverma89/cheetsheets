# Learning fast api : 


* Fast api is built on top of starlett and pydantic. 
* Fastapi is build on principle of fast coding and fast execution. 

* starlett is a SGI library used to parse the http request and pass to fastapi it handles request and response. 
* Pydantic is a data validation and type hint used for modelling and type checking.

# Network Flow : 
* Uvicorn ( ASGI application ) --> Starlett ( SGI async library) --> Fast api 


## env setup : 
* use pydantic settings 


## uv setup : 
* uv add library_name 
* dev dependencies : `uv add --dev dependencyname` e.g uv add --dev mypy
* sync : `uv sync` to add all the dependencies
* sync no dev : `uv sync --no-dev` add files that are not a dev dependencies. 


## env setup in prod : 
* evn setup in prod is done using 
    * Defining a system variables using export in linux export DATABASE_URL = "postgres:asyncpg:///user:pass@host:port/db"
    * defining variables in docker itself 
    * defining variables in kubernetes 




## Servers process things in main two ways : 
* Immediate response ( Synchronous and asynchronous )
* Background tasks called as Jobs ( Corn jobs, event driven jobs) (has producer, has Queue, has consumer)
    * Heavy background task is processed by celery, messageQueues like rabbit MQ 
    * Light background task can be processed by BackgroundTask of FastAPI 
    * `background_task.add(send_mail, email, message="You are on-boarded")`

```python 

    import fastapi from FastAPI

    app = fastAPI()

    app.get("/")
    def home():
        return {"home":"Home"} 

    #path parameter 
    #incase of path we use app.get('{user_id:path}') there helps to read everything after path as a single string even with forward slashes 
    app.get('/user/{user_id:str}')
    def getUser(user_id:str):
        return db.fetch(user_id:user_id)


    #query paramether 
    app.get('/product/')
    def getProduct(offset:int = 0, limit:int = 20):
        return db.fetch('product where id is between offset and limit'))

    # path/item?id=something&time=something1
    # path/item/?id=something&time=something1 both are same becasue in rest the trailing slashes are terminated 


    # if you give a default value it's not required, but if you give a no value it will always be requried like query parameter 

    #required data query param
    app.get('/salesreposet')
    def getSalesReport(startDate:Date, endDate:Date):
        return db.fetch(SalesReport(startDate = startDate, endDate = endDate))

```


## Static files 
```py
    # storing and serving static files
    from fastApi import FastAPI

    app = FastAPI()
    app.mount("/static", StaticFiles(directory = "the_folder_to_hold_files"), name="static")

    # here name if for internal reference inside fastAPI 
    # StaticFiles(directory = "where the files will be stored")
    # "/static" is the sub app inside the main app 
    # mount helps to mount the sub application at specific path. 

```

## BackgroundTask 

```py
    from fastAPI import BackgroundTask, FastAPI 

    app = FastAPI()

    def send_mail(email:str, message:str):
        mail.send(to:email, body:message)

    @app.post("/create-user")
    async def create_user(user_name:Annotate[str, Body(embed=True)], email:Annotated[str, Body(embed=True)],background_task:BackgroundTask):
        res = db.save(user_name, email)
        if(res.success)
            background_task.add(send_mail, email, message="You are on-boarded")
        #this background task will be processed on same thread os of server but later in some time.
        #If you want for a heavy background task or to run on some seperate server you probably need something like celery and rabbitMQ 
        return {"message" : "user created"}


```



## Validation methods 

```py
    from fastApi import Query, Body, Path, Header, Cookie
    from typing Annotated 


    #earlier version of fastapi 
    app.get("product")
    def product(q:str | None = Query(default = "somequery", min_length = 4, max_length = 50, pattern = "^regExPattern$")):
        return db.find(product(q))


    app.get("products")
    def gerProduct(qq: Annotated[str | None, Query(min_length=3, max_length=50)] = None):
            return db.find(product(qq))


    app.get("user")
    def getUser(user: Annotated[User|None , Body(default = None)]): # here user by default is none and it's a body parameter 
            db.find(user)


    # query parameter can also be list because url supports multiple queries 
    url = "https://www.jivem.com/products?pd=shocks&pd=shirt&price=200&pricd=400"

    app.get("/products")
    def getProducts(pd: Annotated[list[str], Query(min_length=3)], price: Annotated[list[int]|None, Query()] = 0):
        return db.find(product(pd & price))


    # below things can be set in Query validation 
    Query (
        title = 
        decs = 
        alias = 
        max_length = 
        min_length = 
        default = 
        pattern = 
    )

    # this is path
    @app.get("/somepath/{prameter}")
    #path operation function
    def function ():
        return {"key":"value"}

```


## Status code and http exception 
* httpException 
```py
    from fastapi import FastAPI, status 



    app = FastAPI()

    @app.get("/user",status_code = 200) # here 200 is default code, you can always return something else by raising exception 
    def getUser(user:User, q:Annotated[str|None , Query()]= None):
        if user.pass == db.user.pass :
            rasie HTTPException{
                status_code = 401 #unauthorized
                detail = "You are not authorized"
            }
        return user.task # if user is validated and authorized

    # you can also use status codes from starlett and fastapi 
    # status.HTTP_201_CREATED
```

## When you want to read a form data 
```py

    #inorder to work with file upload you will have to add : $ uv add python-multipart

    from fastAPI import FastAPI, Form()
    from pydantic import BaseModel 

    @app.post("login")
    def login(username:Annotated[str, Form(alisa="user-name")], password:Annotated[str,Form()]):
        return db.authenticate(username, password)

    
    # you can also generate a formModle 

    class userCred(BaseModel):
        username:str
        password:str
        model_config={"extra":"forbid"} #this code here forbids the clinet to send any extra field apart from username and password

    
    # here the heavy lifiting will be done by fast api to add the related field to the model 
    @app.post("login")
    def login(data:Annotated[userCred, Form()]):
        return db.authenticate(data)

    
    #File is a class that inherits directly from Form.
    #But remember that when you import Query, Path, File and others from fastapi, those are actually functions that return special classes.
        


    # file upload 

    from fastAPI import File , UploadFile

    @app.post("uploadfile")
    async def uploadFile(file:Annotated[UploadFile])


```




## to validate path parameter 
```py

    #user Path() in place of query 
    # path has following aspects 
    # le = less than 
    # ge = greater than 
    # gt 
    Path(title, desc, le , ge, gt, lt, max_length, min_length)

```

## You can also model for query paramters and define only things that will be accepted in the query
```py
    class FilterParams(BaseModel):
        model_config = {"extra": "forbid"}

        limit: int = Field(100, gt=0, le=100)
        offset: int = Field(0, ge=0)
        order_by: Literal["created_at", "updated_at"] = "created_at"
        tags: list[str] = []
```


## pydantic model validation :

```py 

    from pydantic import BaseModel, Field 

    class User(BaseModel):
        user:str = Field(max_length = 100, default = None, title = "Some title") # here filed defins the type of the data the field accepts
        age:str = Field(lt = 200, gt= 0 )

```


## Nested models in fastpi 
```py
    from pydantic import BaseModel 
    class Image(BaseModel):
        url:string
        timeStamp:DateTime
        caption:string

    class Post(BaseModel):
        id:UUID
        caption:string
        timeStamp:DateTime
        images:list[Image]

    
    # here above we have shown an example of multi model 

```


## We can set exmaple for any of the method like Query(), Body(), Field(), Header(), Cookie(), Form() and also example for Models 
## examples helps develop to under more about the models 
```py

    from pydantic import BaseModel

    class Item(BaseModel):
        name:str
        desc:str | None = Field( examples=["exmaple", "example2"])

        model_config = {
            "json_schema_extra":{
                "examples":[
                    {
                        name:"Baseball",
                        desc:"This is another",
                    }
                ]
            }
        }

```


## other datatypes in fastpi 
```py
    from uuid import UUID

    datetime.datetime
    datetime.date
    datetime.timedelta
    datetime.time
    UUID
    frozenset
    bytes
    decimal

    class Item(BaseModel):
        item_id :UUID,
        name:str




```



## Accepting a request body in api 
* you have to define a pydantic model and pass it to a controller function 
* else if you have a singular object you will have to declare it as Body in function paramater name:str = Body(embed = true)

```py
 
    from pydantic import Body, BaseModel 

    class User(BaseModel):
        name:str
        age:int

    
    app.get("create_user"):
        def createUser(user:User):
            db.add(user)
            #bydefault the user here is type of User model


    app.get("user_name"):
        def findUser(name:str = Body(embed = true))
            db.find(name)
            # here also the name sent in request body will be treat as body    


```

## Response in fastapi 
```py
    
    #can be a list 
    # can be a object 
    # can be a model 
    # can be a super class 

    @app.get("/getuser")
    def getUser(user_id):
        return {"user":"Name", "person":"Another"}


```



### Note : 
* Cookie, path, Body, Query() all are them inherit param 
* but they are functions returning a different class.
* Cookie(), Header() we have to make a parameter a type of Cookie() if we want a cookie and same goes for header()


## Header and duplicate header 
* It is possible to recive multiple values for same header field so we shuold user list of header

```py
    
    #here user can receive multiple user_agent
    app.get("user")
    def getUser(auth_token : Annotated[str | None, Cookie()] = None, theme : Annotated[list[str], Header()]):
        return db.find(user(decrypt(auth_token)))



    # If you have multiple cookies or multiple header you can make headerModel (), or CookiesModel

    class Cookie(BaseModel):
        auth_cookie,
        theme,

    class Header(BaseModel):
        accept
        authorization

```




# HTTP tutorial 
## request : 
* request_body : data sent by browser
* request_url : 
* request_header : ( method, authorization, content-type, host, cookie, X-user-defined)

* in browser based request cookie is attached to request by default 
* in code based request like fetch we attach is manually by setting `credentials:"include"`
```js

    var requestUrl = "https://www.api.jivem.in/classes/user_name?date=today"
    // we can have many url and many path parameter in same request
    // origin = protocol + domain + port 
    // default http port is 80 you don't have to add with request 
    // url = protocol + host + path + query/pathparamter + fragement eg . https://www.jivem.in/user/user_id?date=today

fetch("api",{
    header:{
        credentials:"include"  // incase the the HttpOnly is true set by the servre and the request is in cross domain; cookie 
        secure:true
        authorization: bearer || basic || Digest
        Host: //auto set 
        user-agent : //auto set by browser or manually in case of mobile 
        origin : // where the request orginates from
        referer : //previous page 
        accept : //content accepted 
    },
    body:{
        // data is sent in 4 main ways : formdata, binary data, xml , file upload, Json

    }

    // request body is sent mainly in these formats formdata, Json, file upload
    // fileupload = multipart/form-data (data is sent in multiple part) each field is spearted by boundry which is generated by browser
    // formdata = application/x-www-form-urlencoded ( send in one single string )


})
```

### Inheritance : 
```py
    
    # subclass can return an object of super class 

    class Car:
        type :str
        name:str
    
    class Maruti(Car):
        model:str
        power:float
    
    Car car1 = Maruti() #valid
    Maruti m1 = Car() #invalid

```



## response : 
* response_header
* response_body : data sent by server
```js

    res.send(data,{
        header:{
            HttpOnly : true
            Content-Type: application/json
            Content-Length: 92
            Set-Cookie: session=xyz
            Cache-Control: no-cache
            ETag: "a8b7c6"
            Location: /users/101
        }
    })

    res.setCookie(
        key: "refresh_token"
        value: avaluebsaTUyenso
        HttpOnly:true
        secure=True,
        samesite="strict",
        max_age=7 * 24 * 60 * 60,
        path="/auth/refresh"
    )

```

## Access Token & Refresh token : 
* acess token is short lived and used to authenticate and authorize user on every request 
* Refresh token is long lived and used to get new access token 

```js

    // access token is stored in memory and sent with every required request using : 
    authorization : Bearere ${access_token}

    // refresh token is stored in cookie so sent with request defined in path 
    // path in cookie says the browser when to add the cookie in the request. Cookie is only added in the reqeust by browser when the path matches 


```



# Note : 
* /parentdir/subdir/ 
* ending with slash at end is a directory in general sense but in rest apis it's just an end point
* /directory/file
* not ending with slash at end is a file in general sense but in rest they are same.


## Same origin - Cross Origin ( CORS)
## CSRF : Cross site request frogery
## XSS - Cross site scripting 



## Cookie : 
* cookie can be set as `HttpOnly` i.e. can only be accessed over http request not in browser. 
* cookie is sent by browser on every request in both fetch and browser request if its between same origin. 
* cookie is not sent by default if the communication is between different domain, in fetch request i.e we have to set `credentials:"include"`
```js
    Set-Cookie: session_id=abc123;
    Expires=Wed, 30 Jul 2026 18:30:00 GMT;
    Max-Age=3600;
    Domain=.example.com;
    Path=/;
    Secure;
    HttpOnly;
    SameSite=Lax

    SameSite : Strict, Lax , None 
    // Strict means strictly same site 
    // Lax means realx 
    // None means no SameSite request

```


## CORS : Corss origin resource sharing
* Browsers impliment a policy called SOP : Same origin policy 
* `Origin : ptotocol + domain + port `
* If Cors is not implimented any sites can request you api 
* CORS are implimented by browser because they block cross site request. 
* So server has to say browser please allow these origin.
* Now when there is a communication between cross domain browser will impliment cors and block the `response`.
* for this we have to set options in response : `Access-Control-Allow-Credentials : true`, `Access-Control-Allow-Origin : "domain"`
* don't include `*` wildcard becuase this will not work. 


## CSRF : Cross Site request forgery 
* A different site opened on your browsers makes a request to your account when you are logged in and performs some unauthorized actions because browser attaches a cookie with every request. 
* To prevent some this a server sents CSRF token to prevent the CSRF attackes because only legitimate sites will have a valid csrf token.
* Sub domains are considered as a same site.


## XSS : Cross site scripting 


## SQL Injection 


## Click Hijacking 



## Validated reponse using Reponse Model
* we carete model as a response for better code readibility and performance 

```py
    from fastapi import Response 
    from pydantic import BaseModel 

    app  = FastAPI()

    class User(BaseModel):
        name:str
        age:int
        bankAccount:int

    class userIn(User)


    app.get("user", response_model=Item, response_model_exclude_unset=True)
    def getUser()->User:
        return userIn 

    # here the fastapi will validate and only return user leaving the password behind.
    # response_model is used to validate the response which is permitted in response_model.
```






## General API response 

* is either array [] of an object 
* or an object that has an array for multiple items
* or a single object 

* or an object that has an array for multiple items
```json
//object with an array of object
    {
        "fruits" : [
            {
                "id":1,
                "name":"mango"
            },
            {
                "id":2,
                "name":"apple"
            }

        ]
    }
```

* is either array [] of an object
```json
// array of an objects
[
    {
        "user_id": 13,
        "name": "anuj",
    },
    {
        "user_id": 14,
        "name": "anuj",
    },
    {
        "user_id": 15,
        "name": "anuj",
    },
]
```

* or a single object 
```json
//single object
{
    "user":{
        "user_id": 13,
        "name": "anuj",
    }
}

```


## lru_cache is a caching tool : 
* it is a python tool that is used for memoization and used to cache the result for same arguments. 
* if arguments will be different it will return different object. 


## Generator function :
* generator functions are used to return stream of values at certain interval 
* inorder to use it we have to use a single object which will when called next() gives the current value and advances the yield again. 
* generator function when called returns an iterable which we can iterate using next. 
```py

    def gene():
        for i in range(5):
            yield i

    iterable_obj = gene() #returns iterable object 

    next(iterable_obj) # retuns a value

```


## __magic methods__ like __add__, __len__ 
* they are also called dunder methods and they are called automatically by the python to perfrom some specifc task 
* it is also used for method overloading. 
* they are exposed by python for developers to let developers extend their user defined types streamline with native python object. 




# Things to consider in production grade system 
* deactivate the link of docs in production 
* define environment variables in system or docker 
* donot copy env file 
* use `uv sync --no-dev` to only download the production libraries 
* don't use fat routers : seperate router, service, and repositories
* don't mix schema and orm models
* use migration tools like alembic
* use consistent api versioning 
* consistent error response 
* pagination on list items 
* request , response validation 
* rate limiting, authentication ,authorization 
* refresh and access token based authentication 
* loggind and monitoring 
* avoid lazyloading use selectin or joinload 
* Multiple Uvicorn/Gunicorn workers behind a reverse proxy (nginx) — never a single worker in prod
* use dependency injection 
* use background task for backgroud work. 
* use cors mechanism. 


* `Deployment configuration`
    * create docker image 
    * create CI pipeline 
    * create gunicorn-conf file 