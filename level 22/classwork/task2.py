
cold_drinks = ["კოლა", "ფანტა", "სპრაიტი", "აის თი", "ლიმონათი"]


favorite_drink = cold_drinks[0]  


new_drink = input("შემოიტანე ერთი ცივი სასმელი მაცივარში დასამატებლად: ")
cold_drinks.append(new_drink)  


print("აირჩიე სასმელი სიიდან შემდეგი ნომრით:")
for index, drink in enumerate(cold_drinks):
    print(f"{index}: {drink}")

choice = int(input("შეიყვანე სასმელის ნომერი: "))
print("თქვენ აირჩიეთ:", cold_drinks[choice])  


my_name = "ლაზარე"


print("ჩემი სახელიდან 3 სიმბოლო:", my_name[1:4])
