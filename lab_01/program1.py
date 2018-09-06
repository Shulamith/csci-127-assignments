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
     return Fal