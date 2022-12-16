n = int(input())
if (n % 5 == 0 and n % 10 == 0 or n % 15 == 0) and n % 30 :
  print('yes')
else:
  print('No')