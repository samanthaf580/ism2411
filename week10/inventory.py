
# Reflection:

# 1. The most surprising thing I learned from this module about python lists is how easily they can be changed by adding, removing, or even sorting items. 
# 2. A sceneior where lists would be helpful is keeping track of all my past and current grades. Instead of manually editing it in excel, I can use python to easily access my grades to change or edit them.








# Exercise 1

inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(inventory)
print(len(inventory))


# # Exercise 2
print(inventory[0])
print(inventory[-1])
middle_item = len(inventory) // 2
print(inventory[middle_item])


# Exercise 3
print(inventory[0:3])
print(inventory[-2:5])
print(inventory[::2])

# Exercise 4

inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)


# Exercise 5

coords = (30.7128, -74.0060)

# try to change coords:
try:
    coords[0] = 99
except TypeError as e:
    print(f"Error: {e}")

print(coords)

print("Tuples are useful for coordinates because tuples are immutable and coordinates should remain unchanged.")

print(coords)


# Exercise 6
sales = [100, 250, 75, 480, 200]
total_sales = sum(sales)
print(f"Total: {total_sales}")
count_sales = len(sales)
print(f"Number of sales: {count_sales}")
average = total_sales / count_sales
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

# Exercise 7

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    discounted_price = round(price * 0.90, 2)
    discounted.append(discounted_price)
                  
print(f"Original prices: {prices}")
print(f"Discounted prices: {discounted}")


# Exercise 8:

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = 0
count = 0
average = 0


high_sales = [sale for sale in sales if sale > 300]


print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: ~{sum(high_sales) / len(high_sales):.2f}")