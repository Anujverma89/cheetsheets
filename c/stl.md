# STL : Standard Template Library 

### STL 
* Stl is a collection of set of libraries that provides functionalities to work with ALgorithms and datastrucutres without writing them from scratch

### Basic and Main components of STL : 
    * Containers (Contain or store data)
    * Algorithms (Manuplate the data)
    * Iterators (Step through data)

### Containers (Contains data)
    * Sequential (List, dequeue, list)
    * Associative (map, multimap, set, multiset)
    * Container adapter (stack, Queue, Priority Queue)

### pairs
    * Pairs are key and value pair data strucutre 
    * They map a key with a value.
    * They are used in map and multimap.

### Associative containers
```cpp
    // ways to use pairs
    #include <utility> // since pairs are only available only in utility

    pair<int, int> p1; // with default construcutor 
    pair<int , int> p1(1,4); // with contructor value

    // All the values are public by default and can be accessed using first and second;
    // the default value when default construcotr is called is 0 
```


### Sequential Continer
* Every Element in a Sequential Container has a specific Position.
#### Vector 
```cpp
    // vector is a class template that is present int vector module
    #include <vector>

    //creation of vector
    // vector initialization and decleartion
    vecotor <int> vec(othervector) // initialized with another vector
    vecotor <int> vec(size) // another way
    vector <int> vec(n, ele) //creates n size vector and initialized with e elment
    vector <int> vec(begin, end)// creates an vector from beinging to the end-1
    vector <int> vec; // creating empty vector 

    // be default the elements of sized vector are initialized by 0;


    // manuplation of data in vectors
    vec.at(index)
    vec.front()
    vec.back()
    vec[3] // returns the item at beining

    // deletion item from vector 
    vec.clear() // deletes all items from vector 
    vec.erase(position)// delete from specific index
    vec.erase(beging, end) // delete all items from begining to end 
    vec.insert(position, data) // there are different instance of inset it takes position and element to store 
    // here position is the iterator and data is the data \
    // iterator is a typedef operator in a vector 

    vector<int>::iterator iterator_name (iterator name is a pointer)



    // capacity of vectors 
    v.capacity()
    v.max_size() // maximum elements that a system can hold it depends on system architecture it's not the total amount of memory
    v.size()
    v.empty()
    

    v.push_back(); // here object is crated and then copied into vector which has overhead of copying creating and copying item in a memeory
    v.emplace_back(); // here object is created directly into the memory 

    // vector used dynamic arrays behind the scnene 
    // stack is not into the sequence container becuase they cannot be indexed and cannot be accessed randomly but deque, list and vector elements can be accessed;
```

#### Deque
```cpp
    // they are sequential container because their items can be accessed randomly 
    // doubly-ended queue so deque

    // this is provided in the algorithm file hence 
    #include <algorithm>
    copy(startsoruce, end_source, start_destination);

    // when we increment the pointer or do pointer arithematic it doesn't adds value to the pointer insteaed it increments by n times where n is no which is added to tht pointer.
    // while incrementing it points to the next address of the same type.

    deque<int> deq;
    deq.push_front(14);
    deq.push_back(15);
    deq.assign(ncopies, elem);


```

#### List 



### Container Adapater 
#### Stack
#### Queue
#### Priority Queue




### Iterators 
```cpp
    //iterators are the ways to access the items of container
    // two most common operations on iterators 
        //1) Arithematic (increment)
        //2) * derefrencing operator
    // types of iterator 
        // 1) input : read data from input stream
        // 2) output : print data to output media
        // 3) Bidirectional :(cannot be used with adapter containers i.e. can only be used with vector, list, deque, map, multimap, set, multiset)
        // 4) Forward : combines the functionality of input and output operators
        // 5) Random : works only with vector, array,string and deque
```