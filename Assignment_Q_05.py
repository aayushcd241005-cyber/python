#hexadecimal number
#given value
val = 0xCAFE


last4 = val & 0xF


count_bits = bin(last4).count("1")

if count_bits >= 3:
    print("1. At least three of the last 4 bits are ON")
else:
    print("1. Less than three bits are ON")


reversed_val = ((val & 0xFF) << 8) | ((val >> 8) & 0xFF)
print(f"2. Reverse byte order: {hex(reversed_val)}")

rotated_val = ((val >> 4) | (val << 12)) & 0xFFFF
print(f"3. Rotate 4 bits: {hex(rotated_val)}")
