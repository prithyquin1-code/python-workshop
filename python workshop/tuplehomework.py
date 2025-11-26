
vegetables = {"Carrot", "Potato", "Tomato", "Onion", "Cabbage",
              "Spinach", "Cauliflower", "Broccoli", "Peas", "Radish"}

print("Initial set of vegetables:")
print(vegetables)


vegetables.add("Pumpkin")
print("\nAfter adding Pumpkin:")
print(vegetables)


vegetables.remove("Onion")
print("\nAfter removing Onion:")
print(vegetables)



removed_item = vegetables.pop()
print(f"\nVegetable popped: {removed_item}")
print("After popping one item:")
print(vegetables)

vegetables_list = ["Carrot", "Potato", "Tomato", "Onion", "Cabbage",
                   "Spinach", "Cauliflower", "Broccoli", "Peas", "Radish"]

print("Initial list of vegetables:")
print(vegetables_list)


vegetables_list.append("Pumpkin")
print("\nAfter adding Pumpkin:")
print(vegetables_list)


vegetables_list.remove("Onion")
print("\nAfter removing Onion:")
print(vegetables_list)


removed_item = vegetables_list.pop()
print(f"\nVegetable popped: {removed_item}")
print("After popping one item:")
print(vegetables_list)


vegetables_tuple = ("Carrot", "Potato", "Tomato", "Onion", "Cabbage",
                    "Spinach", "Cauliflower", "Broccoli", "Peas", "Radish")

print("Initial tuple of vegetables:")
print(vegetables_tuple)


temp_list = list(vegetables_tuple)
temp_list.append("Pumpkin")


temp_list.remove("Onion")


removed_item = temp_list.pop()
print(f"\nVegetable popped: {removed_item}")


vegetables_tuple = tuple(temp_list)
print("\nFinal tuple after modifications:")
print(vegetables_tuple)



vegetables = {"carrot": 50, "tomato": 30, "onion": 25}

vegetables["potato"] = 40      # add / insert
vegetables.pop("tomato")       # pop / remove

print(vegetables)
