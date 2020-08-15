#lambda - anon functions; one time use
#Map - Iterables
#Filter - Returns boolean functions

'''
Map:
def square(num):
    return num**2

my_nums = [1,2,3,4,5]
for item in map(square,my_nums):
    print(item)
--OR--
list(map(square,my_nums))
^^ Less code than using a "For loop"

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]
names = ['Oribia', 'Domo', 'Talosher']
list(map(slicer,names))
'''

'''
Filter:
def check_even(num):
    return num%2 == 0
mynums = [1,2,3,4,5,6]
list(filter(check_even,mynums))
'''

'''
Lambda:
--converting a function into a Lambda:
def square(num):
    result = num ** 2
    return result

# def square(num): return num ** 2
# lambda num: num ** 2
# Map: list(map(lambda num:num **2, mynums))
# Filter: list(filter(lambda num:num ** 2, mynums))


map(lambda name:name[0], names)
'''
