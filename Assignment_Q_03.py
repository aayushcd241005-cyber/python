# Arithmetic Progression Program

a = int(input("Enter the first term (a): "))
d = int(input("Enter the common difference (d): "))
n = int(input("Enter the term number (n): "))

nth_term = a + (n - 1) * d

sum_n = (n * (2 * a + (n - 1) * d)) // 2

print("Nth term of the AP:", nth_term)
print("Sum of first n terms:", sum_n)
