arr = [1, 2, 3, 4, 5]
def reversearray(arr):
    if len(arr) <= 1:
        return arr
    return [arr[-1]] + reversearray(arr[:-1])

print(reversearray(arr))
