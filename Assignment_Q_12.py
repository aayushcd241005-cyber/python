# program to find LCM and GCD for multiple test cases
n=int(input("Enter number of testcases: "))
for i in range(1,n+1):
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    if a>b:
        greater=a
        smaller=b
    else:
        greater=b
        smaller=a
    for j in range(greater,a*b+1):
        if j%a==0 and j%b==0:
            lcm=j
            break
    for k in range(smaller,0,-1):
        if a%k==0 and b%k==0:
            gcd=k
            break    
    print(lcm,gcd)
