# Number of people
# Take all inputs first
N = int(input("Enter number of people: "))
X = int(input("Enter minimum skill required: "))

skills = [int(input()) for _ in range(N)]

for s in skills:
    print("YES" if s >= X else "NO")
