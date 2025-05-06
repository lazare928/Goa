words = ["ვაშლი", "ტელევიზორი", "კატა", "კომპიუტერი", "სათვალე", "ფანჯარა"]
reversed_words = words[::-1]  

index = 0  

for word in reversed_words:
    if index % 2 == 0: 
        print(word)
    index += 1  
