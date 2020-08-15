'''Coding Exercises 1-10'''


#1 print Hello World
'''
def my_func():
    print('Hello World')
    '''

#2 print Hello {name}
'''
def myfunc(name):
    print('Hello, {}'.format.(name))
'''
#Also, print(f'Hello, {name}')

#3 simple Boolean
'''
def myfunc(a):
    if a == True:
        return 'Oh, yis'
    elif a == False:
        return 'O no'
'''

#4 using Boolean
'''
def myfunc(x,y,z):
    if z == True:
        return x
    else:
        return y
'''

#5 simple math
'''
def myfunc(a,b):
    return a+b
'''

#6 is even?
'''
def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
'''

#7 is greater?
'''
def is_greater(n,x):
    if n > x:
        return True
    else:
        return False
'''

#8 *args
'''
def myfunc(*args):
    return sum(args)
'''

#9 pick evens
'''
def myfunc(*args):
    mylist = []
    for num in args:
        if num %2 == 0:
            mylist.append(num)
    return mylist
'''

#10 skyline
'''
def myfunc(word):
    newWord = []
    for letter in range(len(word)):
        if letter%2 == 0:
            newWord.append(word[letter].lower())
        else:
            newWord.append(word[letter].upper())
    return ''.join(newWord)
'''
