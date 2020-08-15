# *args and **kwargs

'''*args == arguments as many arguments
as you want as a tuple
*args can be any word as long as * preceeds'''

'''**kwargs == keyword arguments. Builds a
dictionary of arguments.
'''

'''
Ex:
def myfunc(a,b):
  # Returns 5% of the sum a & b
  return sum((a,b)) * 0.5
myfunc(40,60)

def myfunc(*args):
    return sum(args) * 0.05

def myfunc(**kwargs):
    if 'fruit' in krwags:
        print("My fruit of choice is {}".format(kwargs['fruit']))
    else:
        print("I did not find any fruit here.")

def(*args,**kwargs):
    print('I would like {}{}'.format(args[0],kwargs['food']))
'''
