# Author: ShangYuan Lim szl6038@psu.edu
# Collaborator: Aryaman Sondhi aps6637@psu.edu
# Collaborator: Samarth Tehri sqt5555@psu.edu
# Collaborator: Douglas Hild djh6278@psu.edu


temp = input("Enter temperature: ")
unit = input("Enter unit in F/f or C/c: ")

temp = float(temp)



if unit == "C" or unit == "c":
  conv = temp*9/5+32
  print ( f"{temp}° in Celsius is equivalent to " f"{conv}° Fahrenheit.")

elif unit == "F" or unit == "f":
  conv = (temp-32)*5/9
  print ( f"{temp}° in Fahrenheit is equivalent to " f"{conv}° Celsius.")

else:
  print(f"Invalid unit({unit}).")