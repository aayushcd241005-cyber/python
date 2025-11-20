# Program to convert inches into foot, yard, centimetres, and meter

inches = float(input("Enter value in inches: "))
foot = inches / 12
yard = inches / 36
centimetres = inches * 2.54
meter = inches / 39.37
print("Value in Foot:", foot)
print("Value in Yard:", yard)
print("Value in Centimetres:", centimetres)
print("Value in Meter:", meter)
