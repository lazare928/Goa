
vegetables = ["პომიდორი", "კარტოფილი", "კაბაჩო", "ხახვი", "ბროკოლი"]


user_choice = int(input("აირჩიეთ რიცხვი 0-დან 4-მდე: "))


if 0 <= user_choice < len(vegetables):
    print(f"თქვენ აირჩიეთ: {vegetables[user_choice]}")
else:
    print("გთხოვთ, აირჩიოთ ვალიდური რიცხვი 0-დან 4-მდე.")
