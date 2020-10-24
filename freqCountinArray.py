def frequency1(array):
  N = max(array) + 1

  countArr = [0] * N

  for item in array:
    countArr[item] += 1
  
  for i in range(len(countArr)):
    if countArr[i] != 0 :
      print(i,"--",countArr[i])

def frequency2(array):
  count = {}

  for item in array:
    if item in count:
      count[item] += 1
    else:
      count[item] = 1

  for item in count:
    print(item,"--", count[item])


arr = [5,1,2,3,5,1,3]
# frequency1(arr)
frequency2(arr)



