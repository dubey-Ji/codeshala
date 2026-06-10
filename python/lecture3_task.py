#Task 1: Calculator


def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid Operation"
    
number1 = float(input("enter the first number: "))
number2 = float(input("enter the second number: "))

opertor = input("enter the opertion (+, -, *, /): ")
result = calculator(number1, number2, opertor)
print(f"Result: {result}")




#Task 3: Celsius to Fahrenheit


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

total_conversions = int(input("How many temperature conversions would you like to perform? "))

for i in range(total_conversions):
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")