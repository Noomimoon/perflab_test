import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

array = m * [i for i in range(1, n + 1)]
result = ''

for i in range(m-1, m*n, m-1):
    if array[i] != 1:
        result += str(array[i-(m-1)])
    else:
        result += str(array[i - (m - 1)])
        break
print ("Полученный путь: " + result)