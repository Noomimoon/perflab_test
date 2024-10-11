import json
import sys

testsJsonPath = sys.argv[1]
valuesJsonPath = sys.argv[2]

def updateTestValues(testsObject, valuesObject):
    
    if 'id' in testsObject:
      testId = testsObject["id"]
    if 'value' in testsObject:
      testValue = getValueValue(valuesObject, testId)
      testsObject["value"] = testValue

    valuesArray = testsObject.get("values")
    if valuesArray is not None:
        for valueObject in valuesArray:
            updateTestValues(valueObject, valuesObject)
    valuesArray = testsObject.get("tests")
    if valuesArray is not None:
        for valueObject in valuesArray:
            updateTestValues(valueObject, valuesObject)
    
def getValueValue(valuesObject, valueId):
    valuesArray = valuesObject["values"]

    for valueObject in valuesArray:
        id = valueObject["id"]

        if id == valueId:
            return valueObject["value"]

    return ""

try:
    with open(testsJsonPath) as testsFile:
        testsObject = json.load(testsFile)

    with open(valuesJsonPath) as valuesFile:
        valuesObject = json.load(valuesFile)

    updateTestValues(testsObject, valuesObject)
    

    with open("report.json", "w") as reportFile:
        json.dump(testsObject, reportFile)

except FileNotFoundError as e:
    print("Файл не найден:", e.filename)

except json.JSONDecodeError as e:
    print("Ошибка JSON:", e)

