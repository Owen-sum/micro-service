Hello! Thank you for using my measurment converter micro service!
_________________________________________________________________

INSTRUCTIONS:

1) Open measurementConverter.py in a code editing app.

2) Run the program. (ex. "py measurementConverter.py" in the terminal)

3) Write into measurementConverter.txt the amount,first type,end type. (ex. 20,oz,cup) and then close the file.

Example code:

	with open("measurementConverter.txt", "w") as file:
        	file.write("15,cup,ml")
		file.close()

4) Wait a second and then read measurementConverter.txt to see conversion.

Example code:

	time.sleep(3)
	with open("measurementConverter.txt", "r") as file:
        	convertedValue = file.readline().strip()

5) Great! You've got your conversion! (convertedValue)
_________________________________________________________________

Possible coversions include:

"oz", "cup", "ml", "tsp", "tbsp"