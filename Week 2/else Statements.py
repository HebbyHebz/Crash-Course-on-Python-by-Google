#Branching with If and else statements.

def checkUsername(username):
    if len(username)<3:
      print('Username cannot be less than 3 characters')

    else: print('Valid Username')


checkUsername('ee')

def is_positive(number):
  if (number>0):
    return (number>0)

  else:
    return False

print(is_positive(-5))


def is_even(number):
  if (number%2 == 0):
    return True
  return  False 

print(is_even(20))