import doctest

def calculate_windchill(temperature, speed):
    """
    Function: calculate_windchill
        Calculates windchill based on international formula (Metric)
    Parameters:
        temperature in Fahrenheit
        speed in miles per hour
    Returns: windchill index (floating point value) in Fahrenheit
    Require: temp/speed in metric units
    Ensure: metric -> imperial unit conversions prior to calculation

    Usage Examples:
    >>> calculate_windchill(32, 10)
    23.691426059765107

    >>> calculate_windchill(-5, 13)
    -24.53809896705898

    >>> calculate_windchill(20, 5)
    12.94189674345419

    """
    # converts the wind speed to kilometers per hour (kph)
    conversion_value = 1.6
    speed_kph = speed * conversion_value

    # converts the air temperature to Celsius for the calculation.
    celsius_temperature = convert_fahrenheit_to_celsius(temperature)
    
    # computes the wind chill index in Celsius and converts back to Fahrenheit
    windchill_index_celsius = 13.12 + 0.6215 * celsius_temperature \
        - 11.37 * (speed_kph ** 0.16) + 0.3965 \
        * celsius_temperature * (speed_kph ** 0.16)

    windchill_index_fahrenheit = \
        convert_celsius_to_fahrenheit(windchill_index_celsius)

    return windchill_index_fahrenheit


def convert_fahrenheit_to_celsius(temperature):
    return ( temperature - 32 ) * 5 / 9

def convert_celsius_to_fahrenheit(temperature):
    return ( temperature * 9 / 5 ) + 32


print(doctest.testmod())
