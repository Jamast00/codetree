s = input()

arr = list(s)
arr.pop(-2)
arr.pop(1)

s = ''.join(arr)
print(s)