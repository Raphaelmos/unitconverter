# English Units Conversions

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def kilometers_to_miles(kilometers):
    """Convert kilometers to miles."""
    return kilometers * 0.621371

def miles_to_kilometers(miles):
    """Convert miles to kilometers."""
    return miles / 0.621371

def get_float_input(prompt):
    """Get a float input from the user with validation."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def main():
    print("Welcome to the Unit Converter!")
    
    while True:
        print("\nSelect a conversion type:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Kilometers to Miles")
        print("4. Miles to Kilometers")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            celsius = get_float_input("Enter temperature in Celsius: ")
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")

        elif choice == '2':
            fahrenheit = get_float_input("Enter temperature in Fahrenheit: ")
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit:.2f}°F is equal to {celsius:.2f}°C")

        elif choice == '3':
            kilometers = get_float_input("Enter distance in kilometers: ")
            miles = kilometers_to_miles(kilometers)
            print(f"{kilometers:.2f} km is equal to {miles:.2f} miles")

        elif choice == '4':
            miles = get_float_input("Enter distance in miles: ")
            kilometers = miles_to_kilometers(miles)
            print(f"{miles:.2f} miles is equal to {kilometers:.2f} km")

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
