def greeter(name):
    return "Hello "+name+"!"
def repeat_string(word):
    return(word+word)
print(greeter("Ollie"))
print(greeter("Stan"))
print(repeat_string("hello"))
def make_abba(a, b):
  return a+b+b+a
def cigar_party(cigars, is_weekend):
  if is_weekend and cigars >= 40:
    return True
  else:
    if 40<=cigars<=60:
     return True
    else:
     return False
def date_fashion(you, date):
  if you<=2 or date<=2:
    return 0
  elif you>=8 or date>=8:
    return 2
  else:
    return 1
def squirrel_play(temp, is_summer):
  if is_summer:
    return (60<=temp<=100)
  else:
    return (60<=temp<=90)