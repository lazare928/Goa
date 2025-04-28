number = int(input("შეიყვანეთ რიცხვი: "))

if number > 0:
    print("დადებითი")
    if number % 2 == 0:
        print("ლუწი")
    else:
        print("კენტი")
else:
    print("უარყოფითი")
