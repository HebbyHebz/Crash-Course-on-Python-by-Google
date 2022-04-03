# This function is to show what happens when a variable is assigned a function that does not return a value.
def greeting(name):
    print('Hello '+name)
  
#This returns 'Hello charles'
greeting('charles')

#This returns 'Hello tobi'
value = greeting('tobi')

#This returns None
print(value)
#None is a special data type in Python used to indicate that a variable or something else is empty or that nothing was returned.