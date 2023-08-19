class TemperatureConverter:
    def convert_to_celsius(self, value):
        pass

    def convert_to_kelvin(self, value):
        pass

    def convert_to_fahrenheit(self, value):
        pass


class Celsius(TemperatureConverter):
    def convert_to_celsius(self, value):
        return value

    def convert_to_kelvin(self, value):
        return value + 273.15

    def convert_to_fahrenheit(self, value):
        return (value * 9/5) + 32


class Kelvin(TemperatureConverter):
    def convert_to_celsius(self, value):
        return value - 273.15

    def convert_to_kelvin(self, value):
        return value

    def convert_to_fahrenheit(self, value):
        return (value - 273.15) * 9/5 + 32


class Fahrenheit(TemperatureConverter):
    def convert_to_celsius(self, value):
        return (value - 32) * 5/9

    def convert_to_kelvin(self, value):
        return (value - 32) * 5/9 + 273.15

    def convert_to_fahrenheit(self, value):
        return value


def main():
    celsius = Celsius()
    kelvin = Kelvin()
    fahrenheit = Fahrenheit()

    # Convert from Celsius to other scales
    print(celsius.convert_to_kelvin(25))     # Output: 298.15
    print(celsius.convert_to_fahrenheit(25)) # Output: 77.0

    # Convert from Kelvin to other scales
    print(kelvin.convert_to_celsius(300))     # Output: 26.85
    print(kelvin.convert_to_fahrenheit(300))  # Output: 80.33

    # Convert from Fahrenheit to other scales
    print(fahrenheit.convert_to_celsius(100))   # Output: 37.77777777777778
    print(fahrenheit.convert_to_kelvin(100))    # Output: 310.92777777777775

if __name__ == "__main__":
    main()
