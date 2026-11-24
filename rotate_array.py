nums = [10, 20, 30, 40, 50]
k = 2

n = len(nums)
k = k % n

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

reverse(nums, 0, n - 1)
reverse(nums, 0, k - 1)
reverse(nums, k, n - 1)

print(nums)