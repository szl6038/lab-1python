# Author: ShangYuan Lim szl6038@psu.edu
# Collaborator: Aryaman Sondhi aps6637@psu.edu
# Collaborator: Samarth Tehri sqt5555@psu.edu
# Collaborator: Douglas Hild djh6278@psu.edu


temp = input("Enter temperature: ")
unit = input("Enter unit in F/f or C/c: ")

temp = float(temp)

if unit == "C" or unit == "c":
  print ( str(temp) + "° in Celsius is equivalent to " + str(temp*9/5+32) + "° Fahrenheit.")

elif unit == "F" or unit == "f":
  print ( str(temp) + "° in Fahrenheit is equivalent to " + str((temp-32)*5/9) + "° Celsius.")

else:
  print(f"Invalid unit({unit}).")