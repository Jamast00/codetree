s = input()

while len(s) != 1:
    arr = list(s)
    n = int(input())
    if len(s) <= n:
        n = len(s)-1
    arr.pop(n)
    s = ''.join(arr)
    print(s)