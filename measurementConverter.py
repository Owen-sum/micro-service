import time
def convertMeasurement(measurement, fromType, toType):

    print("converting " + str(measurement) + fromType + " to " + toType)

    conversions = {
        "oz": {"ml": 29.5735,"cup": 1 / 8,"tsp": 6,"tbsp": 2,},
        "cup": {"oz": 8,"ml": 236.588,"tsp": 48,"tbsp": 16,},
        "ml": {"oz": 0.033814,"cup": 0.00422675,"tsp": 0.166667,"tbsp": 0.5,},
        "tsp": {"oz": 1 / 6,"cup": 1 / 48,"ml": 5,"tbsp": 1 / 3,},
        "tbsp": {"oz": 1 / 2,"cup": 1 / 16,"ml": 15,"tsp": 3,},
    }

    if fromType not in conversions or toType not in conversions[fromType]:
        return f"Unsupported conversion: {fromType} to {toType}"

    try:
        convertedValue = measurement * conversions[fromType][toType]
        return f"{convertedValue:.2f} {toType}"
    except ValueError:
        return "Invalid input."

def main():

    while True:
        with open("measurementConverter.txt", "r+") as file:
            line = file.readline().strip()
            if not line:
                print("Waiting, file is empty")
                time.sleep(2.5)
                
                continue
                
            
            try:
                measurement, fromType, toType = line.split(",")
                measurement = float(measurement)
            except (ValueError, IndexError):
                continue

            convertedValue = convertMeasurement(measurement, fromType, toType)
            file.seek(0)
            file.write(f"{convertedValue}\n")
            print(convertedValue)
        file.close()
        time.sleep(2.5)

if __name__ == "__main__":
    main()