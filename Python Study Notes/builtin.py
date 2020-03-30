###Conceptual Questions:
1. Python is high-level, interpreted, interactive and object-oriented language. Python is highly readable. 
2. It can be easily integrated with C, C++ etc. 
3. Python has 5 standard data types: numbers, string, list, tuple, dictionary
4. Difference between tuples and lists: The main differences between lists and tuples are − Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can be thought of as read-only lists.
5. Convert a object to a regular expressoin: repr(x)
6. To pick a random item from a list or tuple: choice(seq)


### Ternary Conditional Operator:
a if condition else b

###Loops:
    Control Statement:
        break: terminates the loop statement and transfers execution to the statement immediately following the loop
        continue: cause the loop to skip the remainder of its body and retest its condition prior to reiterating
        pass:
    Iterator:

    For Loop:
        Short hand:      [i for i in List if i > 1]     [i if i > 0 else -i for i in List]
        Two iterators:   for f,b in zip(foo,bar): print(f,b)
        Commonly used:   for index,item in enumerate(List): 


###Try and Except (Error Handling):
    If an error is encountered in try block, then the try block code execution is stopped and transfered down to the except block.
    You can also add finally block, which will get executed regardless of whether an exception occurs.
    Example:
    try:
        index = moves.find('D')
    except ValueError:
        return False


###Built-In Function:
1. enumerate(iterable, start = 0):
    Example:    
    >>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    >>> list(enumerate(seasons))
    [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    >>> list(enumerate(seasons, start=1))
    [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

2. convert binary representation back to integers:
    int(b,2)

3. all(iterable)
    return True if all elements of the iterable are true
    example:  if all(ch in A for ch in word.lower()):

4. zip(s,t): takes two or more sequences and returns a list of tuples. Most commonly used in a for loop:
    s = 'abc'
    t = [0,1,2]
    for pair in zip(s,t):
        print(pair)
    This will print ('a',0)/n ('b',1)/n ('c',2)

5. To represent +inf and -inf, use float("inf") and float("-inf")

6. Print in a loop and refresh:
        sys.stdout.write('\r'+str(i) )
        sys.stdout.flush()

