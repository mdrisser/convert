#####
## TEMPERATURE CONVERSIONS
def c_to_f(degrees):
    """
    Convert degrees celcius to degrees fahrenheit
    """
    return degrees * 9/5 + 32


def c_to_k(degrees):
    """
    Convert degrees celcius to degrees kelvin
    """
    return degrees + 273.15


def f_to_c(degrees):
    """
    Convert degrees fahrenheit to degrees celcius
    """
    return (degrees - 32) * 5/9


def f_to_k(degrees):
    """
    Convert degrees fahrenheit to degrees kelvin
    """
    return (degrees + 459.67) * 5/9


def k_to_c(degrees):
    """
    Convert degrees kelvin to degrees celcius
    """
    return degrees - 273.15


def k_to_f(degrees):
    """
    Convert degrees kelvin to degrees fahrenheit
    """
    return degrees * 9/5 - 459.67
