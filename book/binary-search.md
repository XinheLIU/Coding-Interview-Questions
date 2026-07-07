# Binary Search

```py
# Template 1
left, right = 0, len(array) - 1 
while left <= right: 
      mid = (left + right) / 2 
      if array[mid] == target: 
            # find the target!! 
            break or return result 
      elif array[mid] < target: 
            left = mid + 1 
      else: 
            right = mid - 1

# Template 2
if len(A) == 0 or A == None:
    return -1

start,end = 0, len(A) - 1

if target < A[start] or target > A[end]:
    return -1

while start + 1 < end:
    mid = start + (end - start) >> 1
    if target == A[mid]:
        return mid
    elif target > A[mid]:
        start = mid
    else:
        end = mid

if target == A[end]:
    return end
elif target == A[start]:
    return start
else:
    return -1
```

## key points

* while loop condition
  * l &lt;= r: always return in the loop
  * l + 1 &lt;r: needs post-processing, left an right do not meet
* mid
  * use l + \(r-l\) &gt;&gt; 1 to be faster and avoid overflow in common languages
* update left and right pointer
  * l &lt;= r: use +1, -1 to avoid dead loop
  * l + 1 &lt; r: use l = mid, r = mid

Assumptions

* only works for array\(storage supports random access and consecutive\)
* data is sorted
* data is bounded\(usually\)

Use In Engineering

The existence of sorted data structures\(tree, hash tables\) with fast search make binary search become most useful in searching approximation values \(eg. first/last occurrence of a value/in a range\)

* search location range of IP adrress