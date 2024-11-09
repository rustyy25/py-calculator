# FONTFACE FAMILY
font = "Tahoma"

# MATHEMATIC FUNCTIONS
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return round(x / y, 2)

def exponent(x, y):
    result = str(x ** y)

    if len(result) > 3:
        return f"{result[:3]}..."

    return result

def module(x, y):
    return x & y