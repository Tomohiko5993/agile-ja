def convert_celsius_to_fahrenheit():
    print("Enter the temperature in Celsius:")
    celsius = input()
    celsius = int(celsius)
    fahrenheit = (celsius * 9/5) + 32
    print(f"The Celsius temperature {celsius} you entered is {fahrenheit} in Fahrenheit.")

def convert_fahrenheit_to_celsius():
    print("Enter the temperature in Fahrenheit:")
    fahrenheit = input()
    fahrenheit = int(fahrenheit)
    celsius = (5/9) * (fahrenheit - 32)
    print(f"The Fahrenheit temperature {fahrenheit} you entered is {celsius} is Celsius.")

#テストの例
if __name__ == "__main__":
    convert_celsius_to_fahrenheit()
    convert_fahrenheit_to_celsius()