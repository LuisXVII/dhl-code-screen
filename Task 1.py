# Simple calculator implementation. It takes condition from a file and writes the result into a different file. Input file can contain multiple
# operations each on a single line. Equals sign (=) is a terminal operation meaning that past this line no data should be read and it should be on a
# separate line. The output file should contain full equation (condition from the input file and the result). Only basic operations required: add,
# subtract, multiply, divide. There will be no complex conditions, only two numbers, an operation sign and whitespace characters. If the line
# contains any different symbols, it must be taken as erroneous.

# Input file:          Output file:
# 1 + 5                1 + 5 = 6
# 3 / 6                3 / 6 = 0.5
# a plus b             Error
# 21 - 4               21 - 4 = 17
# 6 ; 1                Error
# 2*2                  2 * 2 = 4
# =

import re

def main():
    results = []
    with open("Task 1 data.txt", "r") as operations:
        # Read the file line by line
        for line in operations:
            # Process each line
            # Remove trailing whitespace and line break characters before processing
            line = line.rstrip()

            if re.match(r"=\n?", line):
                printResults(results)
                return
            else:
                results.append(processLine(line))
    print("Error: No terminal operation found")

def processLine(operation):
    # Split the line into a list of numbers and operators using a regex
    pattern = r"((\d+) *([\+\-\*\/]) *(\d+))"
    if match := re.match(pattern, operation):
        # If the line is valid, calculate the result
        result = calculate(match.group(2), match.group(3), match.group(4))
        # Return the result
        return f"{operation} = {result}"
    # If the line is invalid, return an error message
    return "Error"

def calculate(num1, operator, num2):
    # Convert the numbers to integers
    num1 = int(num1)
    num2 = int(num2)
    # Perform the operation
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2

def printResults(operations):
    # Open output file
    with open("Task 1 output.txt", "w") as output:
        # Write the results to the output file
        output.writelines(f"{operation}\n" for operation in operations)

if __name__ == "__main__":
    main()
