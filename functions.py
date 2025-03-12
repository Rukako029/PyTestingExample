def add(a, b):
    return a + b


## corrected with substract sign
def substract(a, b):
      return a-b


def multiply(a, b):
    return a * b


def convert_fahrenheit_to_celsius(fahrenheit):
    return multiply(substract(fahrenheit, 32), 5 / 9) ## corrected  the with right formula



print(convert_fahrenheit_to_celsius(273))
