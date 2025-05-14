
start = int(input("დაწყების რიცხვი: "))
end = int(input("დასრულების რიცხვი: "))

if end < start:
    print("არასწორი შუალედი.")
else:
    total = 0
    print("შუალედი:")
    for i in range(start, end + 1):
        print(i)
        total += i
    print("ჯამი:", total)
