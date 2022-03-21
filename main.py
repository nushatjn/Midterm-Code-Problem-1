def middle_element(lst):
  average=0
  middle_index=int(len(lst)/2)
  if len(lst)%2!=0:
    return lst[middle_index]
  else:
    index1=middle_index-1
    index2=middle_index
    value1=lst[index1]
    value2=lst[index2]
    average = (value1+value2)/2
    return average
numbers = [5,3,-10,-4,4,5]
numbers2=[3,3,5,1,5,7,3]
print(middle_element(numbers))
print(middle_element(numbers2))