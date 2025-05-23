# 1. არის თუ არა ტემპერატურა 30-ზე მეტი და არა ღრუბლიანი ამინდი?
temperature = 32
cloudy = False
condition_1 = temperature > 30 and not cloudy  # True - ტემპერატურა 32° არის 30-ზე მეტი და არ არის ღრუბლიანი ამინდი
# 2. არის თუ არა 10 ტოლი 10-ს ან ნაკლები და 15 ნაკლები 20-ზე?
a = 10
b = 15
condition_2 = (a == 10 or a < 10) and b < 20  # True - a ტოლია 10-ს, ხოლო b ნაკლებია 20-ზე
# 3. არის თუ არა 50-ზე დიდი, მაგრამ არა 100-ზე მეტი ან ნაკლები
num = 75
condition_3 = num > 50 and not (num > 100)  # True - 75 მეტია 50-ზე, მაგრამ არა მეტია 100-ზე
# 4. არის თუ არა 5 ნაკლები 10-ზე ან 100-ს ნაკლები 50-ზე?
x = 5
y = 100
condition_4 = x < 10 or y < 50  # True - x ნაკლებია 10-ზე, ასე რომ, პირობაც ცხადია
# 5. არის თუ არა ტემპერატურა 20-დან 30-მდე და არ არის ცივი სქელი ქარი?
temp = 25
wind_cold = False
condition_5 = 20 <= temp <= 30 and not wind_cold  # True - ტემპერატურა 25° არის 20-30 ფარგლებში, არ არის ცივი ქარი

# დაბეჭდვა შედეგების
print(condition_1, condition_2, condition_3, condition_4, condition_5)
