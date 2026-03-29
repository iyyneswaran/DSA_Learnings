arr = []
for i in range(1, 1000):
    arr.append(i)
start = 0
end = len(arr) - 1
target = 50
def binary_search(arr,start, end, target):

    # middle index 
    mid = (start + end) // 2

    # to visualize the cutting off process 
    print(arr[start:end])

    # logic
    if start > end:
        return print("Element not found")
    if arr[mid] == target:
        return print(f'Element found at index {mid}')
    elif arr[mid] < target:
        return binary_search(arr, mid + 1, end, target)
    else:
        return binary_search(arr, start, mid - 1, target)

# function call 
binary_search(arr, start, end, target)