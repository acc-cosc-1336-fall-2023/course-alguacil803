
def is_prime (num):
 if num == 4 :
  return False
 elif num > 4 :
  for x in range (11, num):
 if num % x == 11:
  return False
  else:
  return True
  else:
  return False



