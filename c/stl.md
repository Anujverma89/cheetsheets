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


# Sequential Continer
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


    int main(){
        deque<int> deq;
        deq.push_back(8);
        deq.push_front(10);
        deq.emplace_front(14);
        deq.emplace_back(16);

        // assign deletes all the items in a contianer and reinitializes them
        deq.assign(125,123);

        ostream_iterator<int> screen(cout, " ");
        copy(deq.begin(),deq.end(),screen);

        // in dequeue elements can be accessed using index of any location

        return 0;
    }

```

#### List 
```cpp
    list<int> l1;
    list<int> l1;
    l1.push_back(13);
    l1.push_front(14);
    l1.push_front(15);
    cout<<l1.size();

    list<int>::iterator listiter;

    ostream_iterator<int> screen(cout," ");
    copy(l1.begin(),l1.end(),screen);
```
### Methods for `std::list`, `std::deque`, and `std::vector` in C++

### 1. Element Access

### `std::list`
- `front()`: Returns a reference to the first element.
- `back()`: Returns a reference to the last element.

### `std::deque`
- `at(index)`: Returns a reference to the element at a specified position.
- `front()`: Returns a reference to the first element.
- `back()`: Returns a reference to the last element.
- `operator[]`: Accesses the element at a specified position (no bounds checking).

### `std::vector`
- `at(index)`: Returns a reference to the element at a specified position.
- `front()`: Returns a reference to the first element.
- `back()`: Returns a reference to the last element.
- `data()`: Returns a direct pointer to the underlying array.
- `operator[]`: Accesses the element at a specified position (no bounds checking).

### 2. Capacity

### `std::list`
- `empty()`: Checks if the list is empty.
- `size()`: Returns the number of elements in the list.
- `max_size()`: Returns the maximum number of elements the list can hold.

### `std::deque`
- `empty()`: Checks if the deque is empty.
- `size()`: Returns the number of elements in the deque.
- `max_size()`: Returns the maximum number of elements the deque can hold.
- `shrink_to_fit()`: Reduces the memory usage by the deque.

### `std::vector`
- `empty()`: Checks if the vector is empty.
- `size()`: Returns the number of elements in the vector.
- `capacity()`: Returns the size of the storage space currently allocated.
- `max_size()`: Returns the maximum number of elements the vector can hold.
- `reserve()`: Reserves storage to accommodate the specified number of elements.
- `shrink_to_fit()`: Reduces the memory usage by the vector.

### 3. Modifiers

### `std::list`
- `assign()`: Assigns new values to the list.
- `push_front()`: Inserts a new element at the beginning.
- `push_back()`: Inserts a new element at the end.
- `pop_front()`: Removes the first element.
- `pop_back()`: Removes the last element.
- `insert()`: Inserts elements at a specified position.
- `erase()`: Removes elements from the list.
- `swap()`: Swaps the contents of two lists.
- `resize()`: Changes the number of elements stored in the list.
- `clear()`: Removes all elements from the list.
- `emplace_front()`: Constructs and inserts an element at the beginning.
- `emplace_back()`: Constructs and inserts an element at the end.
- `emplace()`: Constructs and inserts an element at a specified position.

### `std::deque`
- `assign()`: Assigns new values to the deque.
- `push_front()`: Inserts a new element at the beginning.
- `push_back()`: Inserts a new element at the end.
- `pop_front()`: Removes the first element.
- `pop_back()`: Removes the last element.
- `insert()`: Inserts elements at a specified position.
- `erase()`: Removes elements from the deque.
- `swap()`: Swaps the contents of two deques.
- `resize()`: Changes the number of elements stored in the deque.
- `clear()`: Removes all elements from the deque.
- `emplace_front()`: Constructs and inserts an element at the beginning.
- `emplace_back()`: Constructs and inserts an element at the end.
- `emplace()`: Constructs and inserts an element at a specified position.

### `std::vector`
- `assign()`: Assigns new values to the vector.
- `push_back()`: Inserts a new element at the end.
- `pop_back()`: Removes the last element.
- `insert()`: Inserts elements at a specified position.
- `erase()`: Removes elements from the vector.
- `swap()`: Swaps the contents of two vectors.
- `resize()`: Changes the number of elements stored in the vector.
- `clear()`: Removes all elements from the vector.
- `emplace_back()`: Constructs and inserts an element at the end.
- `emplace()`: Constructs and inserts an element at a specified position.

### 4. Operations

### `std::list`
- `merge()`: Merges two sorted lists into one.
- `splice()`: Transfers elements from one list to another.
- `remove()`: Removes elements with a specific value.
- `remove_if()`: Removes elements satisfying a specific condition.
- `reverse()`: Reverses the order of the elements in the list.
- `unique()`: Removes consecutive duplicate elements.
- `sort()`: Sorts the elements in the list.

### `std::deque` and `std::vector`
- `std::deque` and `std::vector` do not have specialized operations like `std::list`. However, you can use standard algorithms such as `std::sort`, `std::reverse`, and `std::unique` with them.

### 5. Iterators

### `std::list`
- `begin()`: Returns an iterator to the first element.
- `end()`: Returns an iterator to the past-the-end element.
- `rbegin()`: Returns a reverse iterator to the last element.
- `rend()`: Returns a reverse iterator to the element before the first.
- `cbegin()`: Returns a constant iterator to the first element.
- `cend()`: Returns a constant iterator to the past-the-end element.
- `crbegin()`: Returns a constant reverse iterator to the last element.
- `crend()`: Returns a constant reverse iterator to the element before the first.

### `std::deque`
- `begin()`: Returns an iterator to the first element.
- `end()`: Returns an iterator to the past-the-end element.
- `rbegin()`: Returns a reverse iterator to the last element.
- `rend()`: Returns a reverse iterator to the element before the first.
- `cbegin()`: Returns a constant iterator to the first element.
- `cend()`: Returns a constant iterator to the past-the-end element.
- `crbegin()`: Returns a constant reverse iterator to the last element.
- `crend()`: Returns a constant reverse iterator to the element before the first.

### `std::vector`
- `begin()`: Returns an iterator to the first element.
- `end()`: Returns an iterator to the past-the-end element.
- `rbegin()`: Returns a reverse iterator to the last element.
- `rend()`: Returns a reverse iterator to the element before the first.
- `cbegin()`: Returns a constant iterator to the first element.
- `cend()`: Returns a constant iterator to the past-the-end element.
- `crbegin()`: Returns a constant reverse iterator to the last element.
- `crend()`: Returns a constant reverse iterator to the element before the first.
- `data()`: Returns a pointer to the first element of the array used internally.

___




# Container Adapater 
#### Stack
```cpp
    int main(){

        stack<int> stk;
        stk.push(10);
        stk.push(15);
        stk.push(100);
        stk.push(120);
        stk.pop();

        cout<<stk.top()<<endl; // returns the top element
        cout<<stk.size()<<endl; // returns the no of elements in the stack
        cout<<stk.empty()<<endl; // returns true if empty

        ostream_iterator<int> screen(cout," ");
        

        return 0;
    }
```
#### Queue
```cpp

    int main(){
        queue<int> q;
        q.push(10);
        q.push(20);
        q.push(30);

        cout<<q.front()<<endl; // gives the front element
        cout<<q.back()<<endl; // gives the back element

        q.pop();
        cout<<q.front()<<endl;

        cout<<q.size()<<endl;// returns the no of elements in the queue
        cout<<q.empty()<<endl; //returns 1 if empty else returns 0;

        return 0;
    }

```
#### Priority Queue
```cpp

    int main(){
        priority_queue <int> pq,re;
        pq.push(1);
        pq.push(23);
        pq.push(11); // here though we have push 11 at last but still 23 is going to be at top becuase it priority is highest 
        pq.push(3);
        cout<<pq.top()<<endl;
        cout<<pq.size()<<endl;
        pq.pop();
        cout<<pq.top()<<endl; // no 11 will hold the higest priority
        re.push(14);
        
        pq.swap(re); // swap basically swaps the value of each other
        cout<<re.top()<<endl;
        cout<<pq.top()<<endl;
        return 0;
    }

```

### Methods for Container Adapters in C++

### 1. Element Access

### `std::stack`
- `top()`: Returns a reference to the top element.

### `std::queue`
- `front()`: Returns a reference to the first element.
- `back()`: Returns a reference to the last element.

### `std::priority_queue`
- `top()`: Returns a reference to the top element.

### 2. Capacity

### `std::stack`
- `empty()`: Checks if the stack is empty.
- `size()`: Returns the number of elements in the stack.

### `std::queue`
- `empty()`: Checks if the queue is empty.
- `size()`: Returns the number of elements in the queue.

### `std::priority_queue`
- `empty()`: Checks if the priority queue is empty.
- `size()`: Returns the number of elements in the priority queue.

### 3. Modifiers

### `std::stack`
- `push()`: Inserts a new element at the top of the stack.
- `pop()`: Removes the top element from the stack.
- `emplace()`: Constructs and inserts an element at the top.

### `std::queue`
- `push()`: Inserts a new element at the end of the queue.
- `pop()`: Removes the first element from the queue.
- `emplace()`: Constructs and inserts an element at the end.

### `std::priority_queue`
- `push()`: Inserts a new element into the priority queue.
- `pop()`: Removes the top element from the priority queue.
- `emplace()`: Constructs and inserts an element into the priority queue.

### 4. Operations
Container adapters do not have specialized operations like `std::list`, but they can be used with standard algorithms where appropriate.

### 5. Iterators
Container adapters do not provide direct iterator access because they are designed to provide restricted access to their elements.


# Associative Containers
```cpp

    // Associative containers are always sorted in nature by default. Default sorting mechanism is <(less then)
    // We can also define our own sorting criterian 
    // They are implimented using binary search tree 
    // where key of parent node is greater then the left node and smaller then right node
```

### Pairs
```cpp
    // pair helps us to write two values into single variable 
    pair<string, int> student[5];
    student[0].first = "Anuj";
    student[0].second = 3;

    student[1].first = "Akshad";
    student[1].second = 45;

    // this will run because student is a constant pointer 
    cout<<student->first<<" "<<student->second<<endl;   

    // we cannot increment the studnet itself becuase thats the constant and cannot be increment or pointed to some other value
    pair<string,int> *ptr = student;
    ptr++;
    cout<<ptr->first<<" "<<ptr->second;

    // Pairs are stored in contigious memory location 
    // i.e their first and second elements are stored contigiously 

     // pair objects can be compared 

    pair<string, int> p;
    p.first = "Anuj";
    p.second = 3;

    // compariison opertor 

    int a = p == student[0]; // Returns true since student[0].first = p.first && student[0].second == p.second;
    cout<< a<<endl;

    int b = p < student[0]; // here it returns 0 like this we can use many operators like != , <= , >=, >, <, == 
    cout<<b<<endl;

    // we can also make pair using make_pair Function which returns pair

    pair<int,int> pp = make_pair(4,5); // this is also one way of making pair without the type decleration
    cout<<pp.first<<" "<<pp.second<<endl;


    template < class t, class t1>
    pair<t,t1>make_pair(const t &x, t1 &y){
        return (pair<t,t1>(x,y));
    }

```

### Set && Multiset
```cpp
    //elementes are already sorted in less then cirterian
    // elements are arragned in accesding order 
    // set and multiset are available in <set>

    //The only difference between set and multiset is that multiset allows dupliate and set doesnot allows

     set<int> s;
    multiset<int> ms;
    // here this gap between > > is important becuase >> this is right shift operator
    set <int , greater<int> > gs;
    multiset<int, greater<int> > gms;

    set<int> cs(s);
    multiset<int, greater<int> > gsc(gms);
    set<int> ecs(s.begin(),s.end());

    // Note while creating a set or multiset from other  always use the same type of set and multiset



    // manipulation operation 
    // insert()
    // clear() // clear removes everything from the set and multiset
    // erase()
    // erase(position);
    // erase(s.begin(), s.end());


    // this won't generate error but no duplicate values will be stored
    s.insert(5);
    s.insert(10);
    s.insert(15);
    s.insert(15);
    s.insert(20);
    s.insert(25);
    s.insert(25);

    // here we can store duplicate values in the multiset 
    ms.insert(5);
    ms.insert(10);
    ms.insert(15);
    ms.insert(15);
    ms.insert(20);
    ms.insert(25);
    ms.insert(25);



    set<int>::iterator siter;

    for(siter = s.begin(); siter != s.end(); siter++){
        cout<<*(siter)<<endl;
    }   

    multiset<int>::iterator msiter;
     for(msiter = ms.begin(); msiter != ms.end(); msiter++){
        cout<<*(msiter)<<endl;
    }   
    


```

### MAP && Multimap
```cpp

    // values are stored in key and value pairs
    // they are sotred by default cirterian i.e ascending order
    // they can be sorted in some other criterian 

    // only difference between map and multimap is that map doesnot allows duplicate but multimap allows duplicate


    // map is present in map file


    map<string, int> m;
    multimap<string, int> mm;
    multimap<string, int, greater<int> > mmm;
    map<string, int> mp(m);


    // all the creation function 
    // map(key, int) m;
    //ct(key, value) m(another);
    // ct(key, value) m(begin(), end());
    // ct(key, value, sortermethod) m();
    // ct(key, value)
    // sorting method = less, greater, custom comperator     
    // where less is by default 


    // insertion , deletion and removal
    // ct.insert(elemnt)
    // ct.insert(postion, elemnt) // position is a iterator that tells where to begin the search for insertion returns the postion where element is stored
    // ct.clear() removes every elemtn
    // ct.erase(postion)
    // ct.erase(begin, end)
    // ct.erase(element)       


    m.insert({"ANUj",4});
    m.insert({"Nilesh",56});
    m.insert({"Sujal",0});
    m.insert({"Arjun",145});

    map<string,int>::iterator miter;
    miter = m.begin();

    for(miter; miter != m.end(); miter++){
        cout<<miter->first <<" "<< miter->second<<endl;
    }

```



# Iterators 
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

# Important 
* Padding is added in memory for better alignment so that cpu would not have to perfrom extra compuation to access the data.
* Padding ensures that each element within a structure starts at an address that is a multiple of its alignment requirement.
* alignment required is defined by the architecutre of system but it is the power of 2
* eg char takes 1 byte so if alignment is of 4 bytes then 3 bytes padding is added after character so that cpu can access the item directly at the miltile of 4 postion eg 4, 8, 12, 16 etc 