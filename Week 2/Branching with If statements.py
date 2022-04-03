#Branching with If statements.

def checkUsername(username):
    if len(username)<3:
      print('Username cannot be less than 3 characters')


checkUsername('ee')

def is_positive(number):
  if (number>0):
    return (number>0)

  else:
    return None

print(is_positive(-5))