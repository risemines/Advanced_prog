def length(list):
  return len(list)

def mean(list):
  if not list:
    return None #empty list case
  return sum(list)/len(list)

def range_of_list(list):
  if not list:
    return None #empty list case
  return max(list)-min(list)

exemple_list=[1,2,3,4,5]
print(f"Length: {length(exemple_list)}")
print(f"Mean: {mean(exemple_list)}")
print(f"Range: {range_of_list(exemple_list)}")