def sum_list(l):
  s = 0
  
  # Write your logic here
  s = sum([s + sum(i) for i in l])
  
  return s
