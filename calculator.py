def calculate():
  #Enter operation in following format Addition-ADD, Subtraction-sub, Multiplication-MUL & Division-Div
  operation, number_1, number_2 = input().split()
  operation = str(operation)
  number_1 = int(number_1)
  number_2 = int(number_2)
  if operation.upper() == 'ADD':
    print('{} + {} = '.format(number_1, number_2),(number_1 + number_2))
  elif operation.upper() == 'SUB':
    print('{} - {} = '.format(number_1, number_2),(number_1 - number_2))
  elif operation.upper() == 'MUL':
    print('{} * {} = '.format(number_1, number_2),(number_1 * number_2))
  elif operation.upper() == 'DIV':
    print('{} / {} = '.format(number_1, number_2),(number_1/number_2))
  else:
	  print('You have not typed a valid operator, please run the program again.')
calculate()
