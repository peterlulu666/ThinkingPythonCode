number = int(input("Enter a positive integer: "))
n = 1
sum = 0
while True:
    sum = sum + n * 2
    n = n + 1
    if n > number:
        break

print("Done! your sum is: " + str(sum))
