#Branching with If and else and elif statements.

def checkUsername(username):
    if len(username)<3:
      print('Username cannot be less than 3 characters')

    elif len(username)>15:
      print('Invalid Username. Must be less than 15 characters')

    else: print('Valid Username')


checkUsername('eeeeweeewewewee22323wewe')

def number_group(number):
  if number > 0:
    return "Positive"
  elif number == 0:
    return 'Zero'
  else:
    return 'Negative'

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative
