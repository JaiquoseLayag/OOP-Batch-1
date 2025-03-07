count = 0  
for i in range(10):
    num = int(input("Enter number " + str(i+1) + ": "))
    if num % 2 == 1:  
        count += 1  

print("Odd numbers:", count)

