# Numpy 
* Numpy is a low level library written in c and fortran for high level mathematics.
* Since python is user friendly but slow so numpy was developed to overcome the limitation of a python's slow speed
* Pandas is built on top of Numpy
* Numpy stands for numerial python means maths and python
* scipy is also a mathematical library 

### Feature : 
* Linear algebra
* Sophisticated(broadcasting) functions
* N dimensional array, fourier transform, random number.
* there is a single datastrucutre N-D array
* in python there are 9 data strcutre

### N-D array 
* can have only number, float or complex
* it is homogeneous in nature
* Fixed item size


### Terminologies 
* Scaler = 1 0 or 0-dimensional tensor
* vector =[1,24,4] or array or 1-dimensional tensor
* matrix = [[][]] or 2 dim tensor


### Creating numpy array : 
* There are many ways few of which are listed here
* np.array([[]])
* np.zeros(3,4)
* np.ones(4,5)
* np.identity(5)
* np.linspace(start,end,no)
* np.arange(start,end) # one d array(vector)
* arry.copy() create new array


### Properties & functions
* aarray.shape = tells no of items in each dimension
* array.ndim = tells the no of dimensions
* array.size = total no of tiems
* array.itemsize = size of each item in a list
* arra.astype('type') = used for conversion type can be int, float or complex 
* by default int is always a 8 byte that is long in python
* arra.dtype = datatype of the array items
* array.reshape(x,y,z) = used to resize the given array


### List vs numpy arrays
* numpy arrays are faster
* uses less memory 
* More convinient to write code 


### Indexing, slicing and interation
