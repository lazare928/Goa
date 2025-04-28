    
colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]

    
index = int(input("Enter an index (0-3): "))
new_color = input("Enter the new color: ")

if 0 <= index <= 3:
    colors[index] = new_color
    print("Updated colors list:", colors)
else:
    print("Invalid index! Please enter a number between 0 and 3.")
