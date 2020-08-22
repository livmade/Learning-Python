def add(n1, n2):
    print(n1+n2)

number1 = 10
number2 = input("please provide a number: ")

# number2 = string

add(number1,number2) # This will not work because number2 is a string

try: # The code we want to try
    # WANT TO ATTEMPT
    # MAY HAVE AN ERROR
    result = 10 + 10
except: # Error code
    print ("Hey, it looks like you aren't adding correctly.")
else: # If no error, run this
    print("Add went well!")
    print(result)
# finally: -- Code that runs regardless of error or not

'''
try:
    f = open('testfile','w')
    f.write('Write a test line')
except TypeError:
    print("There was a typer error!")
except OSError:
    print("Hey, you have an OS(i/o) error")
finally:
    print("I always run!")
'''
