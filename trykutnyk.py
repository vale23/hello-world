a = None
b = None
c = None

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)


a = float(text_prompt('Enter A:'))
b = float(text_prompt('Enter B:'))
c = float(text_prompt('Enter C:'))
if a + b > c and a + c > b and b + c > a:
  print('triangle')
else:
  print('not triangle')
