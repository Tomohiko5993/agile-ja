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

def convert_kelvin_to_celsius():
    print("Enter the temperature in Kelvin")
    kelvin = input()
    kelvin = int(kelvin)
    celsius = kelvin - 273.15
    print(f"The Kelvin temperature {kelvin} you entered is {celsius} in Celsius")

def convert_celsius_to_kelvin():
    print("Enter the temperature in Celsius:")
    celsius = input()
    celsius = int(celsius)
    kelvin = celsius + 273.15
    print(f"The Celsius temperature {celsius} you entered is {kelvin} in Kelvin.")


def main():
    while True:
        print("Enter c if you want to convert from Fahrenheit to Celsius")
        print("Enter f if you want to convert from Celsius to Fahrenheit")
        print("Enter k2c of you want to convert from Kelvin to Celsius")
        print("Enter c2k if you want to convert from Velsius to Kelvin")
        choice = input().strip().lower()
        if choice == 'c':
            convert_fahrenheit_to_celsius()
        elif choice == 'f':
            convert_celsius_to_fahrenheit()
        elif choice =='k2c':
            convert_kelvin_to_celsius()
        elif choice =='c2k':
            convert_celsius_to_kelvin()
        else:
            print("Incorrect input. Please try again.")
            continue
        break

#テストの例
if __name__ == "__main__":
    main()

