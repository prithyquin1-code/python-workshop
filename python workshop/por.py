fruit_name=["orange","mango","strawberry","pineapple","watermelon","kiwi","grapes"];
print(fruit_name)
print("-------")
print(fruit_name[-2])
fruit_name[1]="watermelon"
print(fruit_name)
fruit_name.append("guava")
print(f" added guava :{fruit_name}")

fruit_name.remove("guava")
print(f"Remove guava :{fruit_name}")

fruit_name.remove("pineapple")
print(f"Remove pineapple :{fruit_name}")

fruit_name.insert(1,"rasberry")
print(fruit_name)


fruit_name.insert(2,"apple")
print(fruit_name)

fruit_name.insert(3,"dragon fruit")
print(fruit_name)

fruit_name.pop(3)
print(fruit_name)


fruit_name.pop(1)
print(fruit_name)

fruit_name.pop(1)
print(len(fruit_name))

fruit_name.pop(1)
print(f"Length of List :{len(fruit_name)}")

print(fruit_name.reverse())
print(type(fruit_name))
