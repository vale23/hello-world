N = None
i = None
Result = None

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)


N = float(text_prompt('Введіть N:'))
if N < 0:
  print('N не може бути від\'ємним')
else:
  i = 0
  Result = 1
  for count in range(int(N)):
    i = i + 1
    Result = Result * i
  print(Result)
