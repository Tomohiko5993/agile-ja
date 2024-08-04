def convert_celsius_to_fahrenheit():
    print("Enter the temperature in Celsius:")
    celsius = input()
    celsius = int(celsius)
    fahrenheit = (celsius * 9/5) + 32
    print(f"The Celsius temperature {celsius} you entered is {fahrenheit} in Fahrenheit.")