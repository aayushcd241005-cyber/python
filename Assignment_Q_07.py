# calculate number using switch case
amount = int(input("Enter total amount: "))
start = int(input("Enter starting denomination: "))

denominations = [100, 50, 20, 10, 5, 2, 1]

start_index = denominations.index(start)
remaining = amount

for den in denominations[start_index:]:
    match den:
        case 100:
            notes = remaining // 100
            remaining %= 100
        case 50:
            notes = remaining // 50
            remaining %= 50
        case 20:
            notes = remaining // 20
            remaining %= 20
        case 10:
            notes = remaining // 10
            remaining %= 10
        case 5:
            notes = remaining // 5
            remaining %= 5
        case 2:
            notes = remaining // 2
            remaining %= 2
        case 1:
            notes = remaining // 1
            remaining %= 1

    print(f"{den} rupees note: {notes}")
