import math
import sys

ctrName = sys.argv[1]
pntName = sys.argv[2]

try:
    with open(ctrName) as centerFile:
        centerX, centerY = map(float, centerFile.readline().split())
        rad = float(centerFile.readline())

    with open(pntName) as pointFile:
        result = []

        for line in pointFile:
            pointX, pointY = map(float, line.strip().split())

            dist = math.sqrt((pointX - centerX) ** 2 + (pointY - centerY) ** 2)

            if dist < rad:
                result.append("1")
            elif dist == rad:
                result.append("0")
            else:
                result.append("2")

    print("\n".join(result))

except FileNotFoundError as e:
    print("Файл не найден:", e.filename)
