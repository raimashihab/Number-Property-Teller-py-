"""Number-Property Teller: Take an integer user input and print the following info about it: (i) Odd/Even,
(ii) Prime/Composite, (iii) Palindrome or not, (iv) No. of factors, (iv) Sum of all natural nums till that num,
(v) factorial of that num, (vi) all fibonacci numbers till that num, (vii) no.of digits in the num"""
def oddeven(n):
    if n%2==0:
        print(n,"is an even number.")
    else:
        print(n,"is an odd number.")
        
def prime(n):
    sravani=False    
    if n>1:
        for i in range(2,n):
            if n%i==0:
                sravani=True
                break
    else:
        print(n,"is neither prime nor composite.")        
    if sravani:
        print(n,"is a composite number.")
    else:
        print(n,"is a prime number.")
        
def palindrome(n):
    n=str(n)
    if n==n[::-1]:
        print(n,"is a palindrome.")
    else:
        print(n,"is not a palindrome.")
        
def factors(n):
    print("The factors of",n,"are:")
    if n==0:
        print("Every integer is a factor of 0")
    i=1
    while i<=n:
        if i<n:
            if n%i==0:
                print(i,end=", ")
        else:
            if n%1==0:
                print(i,end="\n")
        i+=1
        
def sumn(n):
    count=0
    for i in range(1,n+1):
        count+=i
    print("The sum of all natural numbers till",n,"is:",count)
    
def fibonacci(n):
    n1,n2=0,1
    count=0
    if n==1:
        print("Fibonacci sequence upto",n,"is:")
        print(n1)
    else:
        print("Fibonacci sequence upto",n,"is:")
        while count<=n:
            print(n1)
            n3=n1 + n2
            n1=n2
            n2=n3
            count+=1
            
def digits(n):
    num1=n
    count=0
    if n==0:
        print("The no. of digits in", n, "is: 1")
    while n!=0:
        n//=10
        count+=1
    if num1!=0:
        print("The no. of digits in",num1, "is:",count)

print("-----NUMBER PROPERTY TELLER-----")
num=int(input("Enter a number to find out its properties: "))
print("Number properties:")
print("""1. Check whether the number is even or odd
2. Check whether the number is prime or composite
3. Check whether the number is a palindrome or not
4. Find the factors of the number
5. Find the sum of all natural numbers till the number
6. Find all the fibonacci numbers till the number
7. Find the no. of digits in the number
8. All properties""")

ans='y'
while ans=='y':
    ch=int(input("Enter your choice:"))
    if ch==1:
        oddeven(num)
    elif ch==2:
        prime(num)
    elif ch==3:
        palindrome(num)
    elif ch==4:
        factors(num)
    elif ch==5:
        sumn(num)
    elif ch==6:
        fibonacci(num)
    elif ch==7:
        digits(num)
    elif ch==8:
        oddeven(num)
        prime(num)
        palindrome(num)
        factors(num)
        sumn(num)
        fibonacci(num)
        digits(num)
    else:
        print("Invalid choice!")
    ans=input("Do you want to go again?y/n: ")
    
    


