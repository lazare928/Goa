# პაროლის მოთხოვნა მომხმარებლისგან
correct_password = "mypassword"  
entered_password = ""

# პაროლის სწორად შეყვანის დალოდება
while entered_password != correct_password:
    entered_password = input("გთხოვთ, შეიყვანოთ პაროლი: ")
    if entered_password != correct_password:
        print("პაროლი არასწორია. სცადეთ ისევ.")

print("პაროლი სწორია!")
