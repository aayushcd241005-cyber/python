def calculate_last_digit(base, power):
    """Calculate the last digit of base raised to power."""
    return pow(base, power, 10)

def main():
    N = int(input("Enter the number of test cases: "))

    for i in range(N):

        base = int(input("Enter the base value: "))
        power = int(input("Enter the potency of base: "))
        # Calculate the last digit
        result = calculate_last_digit(base, power)
        print(result)

if __name__ == "__main__":
    main()
