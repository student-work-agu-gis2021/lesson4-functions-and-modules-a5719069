"""
This is the new script with the functions that I wrote in Problem 1 and 2
"""

def fahr_to_celsius(temp_fahrenheit):
  """converts the input temperature from degrees Fahrenheit to degress Celsius

  parameter:temp_fahrenheit:
  return:converted_temp:
  """

  converted_temp = (temp_fahrenheit-32)/1.8
  return converted_temp

def temp_classifier(temp_celsius):
  """accepts a temperature value in Celsius that will be reclassified into intenger numbers 0~3 based on following criteria

  parameter:temp_celsius
  return:Classified number(0~3)
  """

  if temp_celsius<-2:
    return 0
  elif temp_celsius<2:
    return 1
  elif temp_celsius<15:
    return 2
  elif temp_celsius>=15:
    return 3