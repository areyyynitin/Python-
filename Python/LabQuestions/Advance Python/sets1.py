# Restaurant Management System :  
# Scenario: You are helping a restaurant manage its menu. The restaurant has a regular menu and a special weekend menu. 
# Tasks: 
# 1. Create a set regular_menu with items 'pizza', 'burger', 'salad', and 'pasta'. 
# 2. Create another set weekend_menu with items 'steak', 'salmon', 'pasta', and 'wine'. 
# 3. Find out which items are available on both the regular and weekend menus.
#  4. Determine the items that are only available on the weekend. 
# 5. Add a new item 'dessert' to both menus. 6. The restaurant decides to stop offering 'burger'. Remove it from the regular menu.

regularMenu={'pizza', 'burger', 'salad', 'pasta'}
weekendMenu={'steak', 'salmon', 'pasta', 'wine'}

print("Regular Menu: ", regularMenu)
print("Weekend Menu: ", weekendMenu)


print("Items available on both the regular and weekend menus: ", regularMenu.intersection(weekendMenu))
print("Items only available on the weekend: ", weekendMenu.difference(regularMenu))

regularMenu.add('dessert')
weekendMenu.add('dessert')
regularMenu.remove('burger')

print("Regular Menu: ", regularMenu)
print("Weekend Menu: ", weekendMenu)