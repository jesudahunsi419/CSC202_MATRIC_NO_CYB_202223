fruits = ["Apple", "Pear", "Orange"]


defmake_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")

make_pie(5)
