# ask how many work entries user want to calculate
works = int(input("Enter number of works: "))
for i in range(works):
    SH = int(input(f"Enter starting hour of work {i+1}: "))
    SM = int(input(f"Enter starting minute of work {i+1}: "))
    EH = int(input(f"Enter ending hour of work {i+1}: "))
    EM = int(input(f"Enter ending minute of work {i+1}: "))
    start = SH * 60 + SM
    end = EH * 60 + EM
    duration = end - start
    hours = duration // 60 #it removes the decimal part
    minutes = duration % 60
    print(f"You worked {hours} hr {minutes} min")
