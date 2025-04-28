correct_pin = "1234"  
attempts = 0  

while True:
    user_pin = input("გთხოვთ შეიყვანოთ 4 ციფრიანი PIN კოდი: ")
    attempts += 1  
    
    if user_pin == correct_pin:
        print(f"ავტორიზაცია წარმატებით გაიარა! ცდების რაოდენობა: {attempts}")
        break  
    else:
        print("არასწორი PIN კოდი, სცადეთ ისევ.")
