"""
******
PART 2
******
Define a function celsius that takes a single float parameter, the temperature in fahrenheit. The function RETURNS (not print) the celsius reading of the temperature

The formula for converting from fahrenheit to celsius:
C = (F - 32) * 5/9
"""

def celsius(f):
  c = f - 32
  c = c / 9
  c = c *5
  return c