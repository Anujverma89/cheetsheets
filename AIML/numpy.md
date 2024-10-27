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
*type(np.concatinate) returns _arrayfunctiondispatcher* 

**this is filter technique**
another = newarray[newarray > 5]

### reference
| **Function Type**             | **Purpose**                                   | **Examples**                             | **Sample Code**                                                                                      |
|-------------------------------|-----------------------------------------------|------------------------------------------|------------------------------------------------------------------------------------------------------|
| **Array Creation**            | Create new arrays of specific shapes and types | `np.array()`, `np.zeros()`, `np.ones()`  | ```python\nimport numpy as np\na = np.zeros((2, 2))\nprint(a)\n```                                   |
|                               |                                               | `np.arange()`, `np.linspace()`           | ```python\na = np.linspace(0, 1, 5)\nprint(a)\n```                                                  |
|                               |                                               | `np.random.rand()`, `np.random.randint()`| ```python\na = np.random.randint(0, 10, (2, 3))\nprint(a)\n```                                      |
| **Mathematical Operations**   | Perform element-wise math operations          | `np.add()`, `np.subtract()`, `np.multiply()` | ```python\na = np.array([1, 2])\nb = np.array([3, 4])\nprint(np.add(a, b))\n```                      |
|                               |                                               | `np.exp()`, `np.log()`, `np.power()`     | ```python\na = np.array([1, 2, 3])\nprint(np.exp(a))\n```                                           |
| **Statistical**               | Calculate stats across arrays                 | `np.sum()`, `np.mean()`, `np.std()`      | ```python\na = np.array([1, 2, 3])\nprint(np.mean(a))\n```                                          |
|                               |                                               | `np.min()`, `np.max()`, `np.percentile()` | ```python\na = np.array([1, 3, 2])\nprint(np.percentile(a, 50))\n```                                |
| **Array Manipulation**        | Reshape or rearrange array structure          | `np.reshape()`, `np.ravel()`, `np.flatten()` | ```python\na = np.array([[1, 2], [3, 4]])\nprint(np.reshape(a, (4,)))\n```                          |
|                               |                                               | `np.concatenate()`, `np.vstack()`        | ```python\na = np.array([1, 2])\nb = np.array([3, 4])\nprint(np.concatenate((a, b)))\n```            |
| **Logical**                   | Perform logical or comparison operations      | `np.greater()`, `np.less()`, `np.equal()` | ```python\na = np.array([1, 2])\nb = np.array([2, 2])\nprint(np.greater(a, b))\n```                  |
|                               |                                               | `np.logical_and()`, `np.logical_or()`    | ```python\na = np.array([True, False])\nb = np.array([False, False])\nprint(np.logical_and(a, b))\n```|
| **Linear Algebra**            | Perform matrix and linear algebra operations  | `np.dot()`, `np.matmul()`, `np.linalg.inv()` | ```python\na = np.array([[1, 2], [3, 4]])\nprint(np.linalg.inv(a))\n```                             |
| **Fourier Transform**         | Analyze frequency components                  | `np.fft.fft()`, `np.fft.ifft()`          | ```python\na = np.array([1, 2, 1, -1])\nprint(np.fft.fft(a))\n```                                   |
| **Random Number Generation**  | Generate random numbers or samples            | `np.random.rand()`, `np.random.randint()`| ```python\na = np.random.rand(2, 2)\nprint(a)\n```                                                  |
|                               |                                               | `np.random.choice()`, `np.random.shuffle()` | ```python\na = np.array([1, 2, 3])\nnp.random.shuffle(a)\nprint(a)\n```                             |
| **Bitwise**                   | Perform bitwise operations                    | `np.bitwise_and()`, `np.bitwise_or()`    | ```python\na = np.array([1, 2])\nb = np.array([2, 3])\nprint(np.bitwise_and(a, b))\n```             |
| **Set Operations**            | Perform operations treating arrays as sets    | `np.unique()`, `np.intersect1d()`, `np.union1d()` | ```python\na = np.array([1, 2, 3, 1])\nprint(np.unique(a))\n```                                    |
| **Indexing and Slicing**      | Retrieve elements based on indices/conditions | `np.take()`, `np.choose()`, `np.nonzero()` | ```python\na = np.array([0, 3, 4])\nprint(np.nonzero(a))\n```                                      |


### Furior transformation -> Conversion of data from time domation to frequency domain 

