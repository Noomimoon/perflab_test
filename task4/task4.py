def read(fileName):
    nums = []

    with open(fileName) as file:
        for line in file:
            values = line.split()
            for value in values:
                nums.append(int(value))
    return nums

def findMin(nums):
    minVal = float('inf')
    maxVal = float('-inf')

    for num in nums:
        minVal = min(minVal, num)
        maxVal = max(maxVal, num)

    minMoves = float('inf')
    for target in range(minVal, maxVal + 1):
        moves = sum(abs(num - target) for num in nums)
        minMoves = min(minMoves, moves)

    return minMoves

if __name__ == "__main__":
    import sys

    fileName = sys.argv[1]
    nums = read(fileName)
    minMoves = findMin(nums)
    
    print(minMoves)
