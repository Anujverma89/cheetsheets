# Cheetsheet 
### Numpy = Numerical Python 
*Used to work with ndarrays*   
*Used to work with homogeneous dataset i.e. with numbers*   
*Fixed shape and same elements are of same data type*  
*Used for scientifc  & mathematical computation*   
*Speed of C and flexibility of python*   

**Ways to create array**  
*np.array([],dtype='complex')*  
*np.ones(10)*   
*np.zeros(10)*  
*np.arrange(10).reshape(z,x,y)*  
*np.empty()*   
*np.linespace()*  
*np.random()*


**Features which make Numpy fast**  
**Broadcasting** -> When applied to dataset operation is applied to every item.    
**Vectorization** -> Is a technique in computer science of applying same instruction on multiple data.  
**(Efficient) Contigious memory allocation** -> Array element are stored in contigious memory location where in python list items are stored anywhere in memory.  

**Vectroization Working**  
**SIMD** -> **SIMD is a parallel computing techinque which uses one instruction muliple Data** *Single instruction Multiple Data Uses hardware level Parallelism. Multiple pair of elements in single CPU Cycle*
** Since Numpy array elements are stored in continious memeory locatoin they can be accessed continiously and stored in registers and processed in cpu cycle. Looping is involed at low level but due to continious and direct memory address it takes less time then python**  
**There exists a SIMD resigter which can hold data which is to be processed by SIMD instruction set like SSM (Streaming SIMD Extension)**  
**Vectorization is used in machine learning, graphics and gaming physics engine**


**Dimensions are called axes**
**numpy array is of class ndarray**

### numpy is a module it has a class named as ndarray alias array

### class ndarray:
**attributes**  
**ndarray.ndim**  
**ndarray.shape**  
**ndarray.size**  
**ndarray.dtype**    
**ndarray.itemsize**  gives the total size of the item in memeory    
**ndarray.data**  

**Arithmatic Operations**    
*np.sin()*  
*np.conv()*   
*a @ b*   
*dot product*  
*a.b*  

**Addding newaxis to array**  
*newaxis*  
*ndenumerate*  
*indicies*


**Adding multiple arrays**  
*hstack*  
*vstack*  
*column_stack*  
*concatinate* 

**Sorting**  
*argsort*  
*lexsort* 

#### Stride : Step size (how many pixel do you cover in one move to right or bottom )   


### Data types :   
* Int   
* float  
* complex  
* boolean  
*np.array([1,2,3],dtype='f')*

### Ufunc = universal function  
*They are used to perfrom operatons on numpy array on element by element fashion rather then perform action on entire array as whoel*   
*type(np.add) return np.ufunc*    
*type(np.concatinate)*   

**this is filter technique**
another = newarray[newarray > 5]
