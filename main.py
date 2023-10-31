#Using conditons: if
#setting variables
is_old = True
if is_old:  #this only runs if its 'true'
  print("You are old enough to drive!")
print('checkcheck')  #then the interpreter comes to this line

is_old = False
if is_old:  #this only runs if its 'true',orelse ignores & skips to line#12
  print("You are old enough to drive!")
print('checkcheck')

#Using conditons: if & else
#set variables
is_old = True
if is_old:
  print("You are old enough to drive!")
else:  #this will run only if 'if' statement is 'false'
  print("You are not old enough to drive!")
print('okokok')

is_old = False
if is_old:  #as this is 'false' now so it'll skip to line#25
  print("You are old enough to drive!")
else:  #this will run now as 'if' statement is 'false
  print("You are not old enough to drive!")
print('okokok')

#Using conditons: if, elif & else
#set variables
is_old = True
is_licensed = True
if is_old:  #if 'if' statement is true then elif & else will not                                                           be executed
  print('You are old enough to drive!')
elif is_licensed:  #this will run only if 'if' statement is 'false'
  print('You can drive now!')
else:  #this will run only if both 'if' &'elif' statements are 'false'
  print("You are not old enough to drive!")
print('okok')

is_old = False
is_licensed = True
if is_old:  #as this is 'false' now so it'll skip to line#45
  print('You are old enough to drive!')
elif is_licensed:  #this will run now as 'if' statement is 'false
  print('You can drive now!')
else:
  print("You are not old enough to drive!")
print('okok')

is_old = False
is_licensed = False
if is_old:  #as this is 'false' now so it'll skip to line#55
  print('You are old enough to drive!')
elif is_licensed:  #as this is also 'false' so it'll skip to line#57
  print('You can drive now!')
else:
  print("You are not old enough to drive!")
print('okok')

#using keyword 'and' -when we want both the conditons to be met at the same time
is_old = False
is_licensed = False
if is_old and is_licensed:  #only run when both statements are True
  print('You are old enough to drive, and you have a license!')
else:
  print("You are not old enough to drive!")
print('okok')

is_old = True
is_licensed = False
if is_old and is_licensed:
  print('You are old enough to drive, and you have a license!')
else:
  print("You are not old enough to drive!")
print('okok')

is_old = True
is_licensed = True
if is_old and is_licensed:
  print('You are old enough to drive, and you have a license!')
else:
  print("You are not old enough to drive!")
print('okok')

#Truthy VS Falsy
is_old = 'hello'
is_licensed = 5
if is_old and is_licensed:
  print('You are old enough to drive, and you have a license!')
else:
  print("You are not old enough to drive!")


