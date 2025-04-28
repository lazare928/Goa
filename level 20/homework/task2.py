
sum_positive = 0

while True:
    number = int(input("Enter a number (negative number to stop): "))
    
    if number < 0:
        break
    elif number > 0:
        sum_positive += number
    

# შედეგის დაბეჭდვა
print("Sum of all positive numbers is:", sum_positive)
