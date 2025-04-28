
even_count = 0
odd_count = 0

while True:
    number = int(input("Enter a number (negative number to stop): "))
    
    if number < 0:
        break
    elif number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# შედეგის გამოშვება
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
