# მომხმარებლისგან ორი რიცხვის მიღება
first_num = int(input("შეიყვანეთ პირველი რიცხვი: "))
second_num = int(input("შეიყვანეთ მეორე რიცხვი: "))

# პირველი რიცხვიდან მეორეს ჩათვლით ყველა რიცხვის გამოყვანა
for num in range(first_num, second_num + 1):
    print(num)
