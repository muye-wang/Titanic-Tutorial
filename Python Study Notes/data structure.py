###String:
    Basics:
        1. A string is a sequence of characters: s[i], s[-1], s[-2], s[::-1]
        2. To get the length: len(s)
        3. loop: "for letter in words:" or "while i < len(words):"
        4. string slices: s[n:m] including nth, excluding mth.
                      s[n:] start from nth until the end
                      s[:m] start from the begining until m-1th
        5. strings are immutable: You cannot change an existing string:  words[i] = char (this is illegal)
            The best you can do is to create a new string that is a variation on the original. 
        6. string methods:
            word.capitalize()
            word.count(str,ben=0,end=len(string)): Counts how many times str occurs in a string or substring
            word.upper()
            word.lower()
            word.find(ch,i,j): return the index of the first encounter of ch in word[i:j], if ch is not in word, returns -1.
            word.rfind(ch,i,j): same as find but search backwards in string
            word.index(ch): return the index of the first encounter of ch, if ch is not in word, return ValueError
            word.replace('m','n'): replace all the 'm' in word with 'n'
            word.isupper(): returns True if word only contain uppercase letter
            word.islower()
            word.isnumeric()
            word.isspace()
            word.istitle()
            word.lstrip(): removes all leading whitespace in string
            word.split(str="",num=string.count(str)): splits word according to delimiter str (space if not provided) and return a list of substrings
            word.splitlines(): splits string at all NEWLINEs and returns a list of each line with NEWLINES removed.
            word.strip([chars])
            word.swapcase(): inverts case for all letters in string
        7. string operators:
            +: concatenation
            *: repetition
            =,<,>: alphabetical order, uppercase come before lowercase
            in, not in: 'a' in 'banana': True; 'seed' in 'banana': False
    Tricks:
        1. To remove all the same characters from a string, you have to make a copy:   
            Newstr = oldstr.replace('m','')
        2. To remove the central character (or any character at a specific position):
            midlen = len(oldstr)/2
            newstr = oldstr[:midlen] + oldstr[midlen+1:]
        3. Get position of character inside a string:
            str.find('m'): returns -1 if m is not in str
            str.index('m'): Value Error if m is not in str
        4. To reverse a string s:
            s[::-1]


###List:
    Basics:
        1. To create a new list: newlist = [10,20,30,'m']; emptylist = [];
        2. lists are mutable: "list[5] = newItem" is legal
        3. Traversing a list: "for item in list:" or "for i in range(len(list)):"
        4. List slices: same as string
        5. List methods:
            list.append(item): add a new item to the end of the list 
            list.entend(list2): concatenate list2 to the list. This is the same as: list = list + list2
            list.sort(): sort from low to high
            list.count(obj): count numbers of obj occurs in list
            list.index(obj): return the lowest index in list that obj appears
            list.insert(index, obj)
            list.pop(index): remove and return list[index] 
            list.remove(item): if you know the element that you want to remove, instead of the index, do this.
            del list[index] or del list[i:j]: if you do not need the removed item, you can use del list[index] instead.
            list.split(): split a string into words (spliting based upon ' ').
            list.split('.'): split based upon '.'.
            list.reverse()
        6. List operations:
            +: concatenates lists: newList = list1 + list2
            *: repeats a list many times: newList = list*n; newList = [0,1]*5
            in, not in
        7. Converting a string or a set to a list of characters: l = list(word); l = list(set)
        
        8. lists references:
        8.1 a =[1,2,3]
            b = a;
           Now a and b are two references to the same objects. If i change a, then that affect b as well. This happends to mutable objects like lists.
           However, this does not really matter for strings since they are immuatble.
        8.2 When you pass a list into a function, the function gets a reference to the list. Thus if the function modify the list, the caller will see the change.
            The alternative is to create and return a new list inside the function.
    Tricks:      
        1. list[~i] = list[-i-1]=row[len(list)-1-i]: ith value of the list, counting from the right
        2. list[-1]: the last elements
        3. To make a list of n lists:   d = [[] for i in range(n)]


###Dictionary:
    Dictionaries are like lists, but the indices can be of any type, and they are called keys. Each key is associated with a single value. 
    Dictionaries are implemented using hasktable. The keys must be immutable, and thus lists cannot be the keys for a dictionary.

    Basics:
        1. To make a empty dictionary: eng2sp = dict()
        2. To make a non-empty dictionary: eng2sp = {'one':'uno','three':'tres'}. The order of the keys in a dict is unpredictable
        3. To add items to the dictionary: eng2sp['one'] = 'uno'
        4. To look up an item in a dict using the key: eng2sp['one'] returns 'uno'
        5. len(dict) returns the number of key-value pairs
        6. in operator: 'one' in eng2sp: see if a key is in the dictionary (not a value)
        7. vals = eng2sp.values(): returns a collection of values. 
        8. To loop through a dictionary: for key,item in d.items():
        9. To delete an item: d.pop('key', None)


###Tuples
    Tuples are like lists, but they are immutable.

    Basics:
        1. To create an empty tuple: t = tuple(); To create a tuple: t = 'a','b','c'; To create a tuple with a single value: t = 'a',
        2. Most list operators work on tuples except when you try to modify elements of the tuple. 
        3. zip returns a list of tuples (see below built-in functions)

###set:
    Python built-in class. No duplicates by definition

    Basics:
        1. To create a set of a sequence: s = set([iterable]): this way set s only contain the unique elements in [iterable]


###Int:
    Int are not iteratable, though it can be converted to str, and iterate through the str
    1. Binary representation of an int:
        bin(x), which returns a str: ob+binary number
        To only get the binary numbers:
        bin(x)[2:]
   


### Tricks and shortcuts:

1. Remove Duplicates from a list (): This will be in random order
    y = list(set(y))

2. Remove duplicates and retain the same order: This is slow in general
    List_no_duplicate = []
    for i in List:
        if i not in List_no_duplicate:
            List_no_duplicate.append(i)
3. sort a list:
    y.sort() # sort doesn't return anything. 

4. binary search:
    
    def binary_search(array, needle_element):
        mid = (len(array)) / 2
        if not len(array):
            raise "Error"
        if needle_element == array[mid]:
            return mid
        elif needle_element > array[mid]:
            return mid + binary_search(array[mid:],needle_element)
        elif needle_element < array[mid]:
            return binary_search(array[:mid],needle_element)
        else:
            raise "Error"

5.Swap two elements in a list:
    i = ['title', 'email', 'password2', 'password1', 'first_name', 'last_name', 'next', 'newsletter']
    a, b = i.index('password2'), i.index('password1')
    i[b], i[a] = i[a], i[b]

6. Minimal number of swaps required to sort a list:
    def minimumSwaps(arr) :    
        swap = 0
        i = 0
        while i < len(arr):
            print(arr)
            if arr[i] == (i+1):
                i += 1
                continue
            arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
            swap += 1
        return swap

7. Replace an element in a list:
    l = [1,2,3,4,5]
    l = [x if x != 4 else newElement for x in l]

8. Operate on part of a list:
    l = [1,2,3,4,5]
    l_odd = [i if i%2 != 0 else None for i in l]    #[1, None, 3, None, 5]
    l_odd_new = list( filter(lambda a: a!= None, l_odd))  #[1,3,5]

9. Find median of a list:
     def find_median(arr):
        arr_new = [i for i in arr]
        arr_new.sort()
        n = len(arr_new)
        if n%2 != 0:
            return arr_new[int(n/2)]
        else:
            return (arr_new[int(n/2-1)] + arr_new[int(n/2)])/2

10. Create a list of empty lists:
    x = [ [] for i in range(3)]