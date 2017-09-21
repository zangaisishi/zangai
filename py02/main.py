def BinSearch(array, key, low, high):
 mid = int((low+high)/2)
 if key == array[mid]:
  return array[mid]
 if low > high:
  return False

 if key < array[mid]:
  return BinSearch(array, key, low, mid-1) 
 if key > array[mid]:
  return BinSearch(array, key, mid+1, high)
