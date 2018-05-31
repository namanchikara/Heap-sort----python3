def heapify(arr,i,heapsize):
    l = 2*i
    r = 2*i +1
    largest = -1

    if  (l< heapsize) and (arr[l] > arr[i]):
      largest = l
    else:
      largest = i
  
    if r< heapsize and arr[r] > arr[largest]:
      largest = r

    if largest != i:
      arr[i], arr[largest] = arr[largest], arr[i]
      heapify(arr, largest,heapsize)


def build_max_heap(arr):
  for x in range(int(len(arr)/2), 0, -1):
    heapify(arr,x,len(arr))

def heapsort(a):
  heapsize = len(a)
  build_max_heap(a)
  for i in range(len(a)-1, 1, -1):
    a[i], a[1] = a[1], a[i]
    heapsize -= 1
    heapify(a,1,heapsize)

if __name__ == '__main__':
  unsorted_array = [int(y) for y in input().split()]

  sorted_array = [1]

  for x in unsorted_array:
    sorted_array.append(x)

  heapsort(sorted_array)
  print("Sorted array = ", sorted_array)
