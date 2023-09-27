'''
Name: Jiawen Cai
Class: CS5001
This is for #2 Programming in HW2: function and testing
'''

FAHRENHEIT_BASE = 32

def convert_fahrenheit_to_celsius( fahrenheit_temp ):
    '''
    Function -- convert_fahrenheit_to_celsius
        Converts temperature from F to C
    Parameters:
        temperature (float) -- the original temperature in Fahrenheit
    Returns a float value representing the original temperature converted
        to Celsius
    '''

    return (fahrenheit_temp - FAHRENHEIT_BASE) * 5/9

def convert_celsius_to_fahrenheit( celsius_temp ):
    '''
    Function -- convert_celsius_to_farenheit
        Converts temperature from C to F
    Parameters:
        temperature (float) -- the original temperature in Celsius
    Returns a float value representing the original temperature converted
        to Fahrenheit
    '''
    
    return ((celsius_temp / 5) * 9) + FAHRENHEIT_BASE

def main():
    '''
    Function -- main
        Print four conversion result between C and F
    Parameters:
        none
    Returns a string containing float numbers 
    representing the converted results
    '''
    
    fahrenheit_temp = 68
    celsius_temp = convert_fahrenheit_to_celsius(fahrenheit_temp)
    print(f"Converting {fahrenheit_temp} fahrenheit to celsius...\
           The result is {celsius_temp:.1f}; Expected result is 20.0 ")

   
    celsius_temp = 17  
    fahrenheit_temp = convert_celsius_to_fahrenheit(celsius_temp)
    print(f"Converting {celsius_temp} celsius to fahrenheit...\
           The result is {fahrenheit_temp:.1f} ; Expected result is 62.6 ")
    
    fahrenheit_temp = -5  
    celsius_temp = convert_fahrenheit_to_celsius(fahrenheit_temp)
    print(f"Converting {fahrenheit_temp} fahrenheit to celsius...\
           The result is {celsius_temp:.1f}; Expected result is -20.6 ")
    
    celsius_temp = 26
    fahrenheit_temp = convert_celsius_to_fahrenheit(celsius_temp)
    print(f"Converting {celsius_temp} celsius to fahrenheit...\
           The result is {fahrenheit_temp:.1f} ; Expected result is 78.8 ")



if __name__ == "__main__":
    main()

