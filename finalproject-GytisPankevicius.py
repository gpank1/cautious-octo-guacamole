#Final Project
#By Gytis Pankevicius
#Creates Inventory System to manage and track items

class InventoryItem:
    
    #Attributes for each item
    def __init__(self, name, ID, quantity, price):
        self.name = name
        self.ID = ID
        self.quantity = quantity
        self.price = price

    #Updates item quantity/price
    def update_item(self, new_quantity, new_price):
        self.quantity = new_quantity
        self.price = new_price
        print("Item updated.")

    #Displays item in formatted output
    def display_item(self):
        return f"Name: {self.name.capitalize()}, ID: {self.ID}, Quantity: {self.quantity}, Price: ${self.price:,.2f}"

class InventoryManager:

    def __init__(self):
        #Entire inventory list
        self.inventory = []

    #Adds item to inventory[] list using the InventoryItem class
    def add_item(self, name, ID, quantity, price):
        #Check for duplicate ID
        for item in self.inventory:
            if item.ID == ID:
                print (f"An item with ID: {ID} already exists in the inventory.")
                return False
        self.inventory.append(InventoryItem(name, ID, quantity, price))
        return True

    #Loops through inventory[] list and displays all items
    def display_inventory(self):
        print("\nInventory:")
        for item in self.inventory:
            print(item.display_item())
    
    #Searches for an item in inventory[] list
    def search_item(self, keyword):
        matching_items = []
        for item in self.inventory:
            #Checks for match regardless of case sensitivity
            if keyword.lower() in item.name.lower():
                    matching_items.append(item)
        #return matching_item list
        return matching_items

    #Saves inventory[] to file by appending
    def write_to_file(self):
        #Checks if file can be opened
        try:
            #Using append to not rewrite entire file but to add on
            with open('inventory_data.txt', 'a') as file:
                #writes into file each item separated by commas
                for item in self.inventory:
                    file.write(f"{item.name},{item.ID},{item.quantity},{item.price}\n")
            print("Inventory saved to file.")
        except FileNotFoundError:
            print("No inventory file found.")

    #reads from file and inputs values into inventory[]
    def read_from_file(self):
        #Checks if file can be opened
        try:
            with open('inventory_data.txt', 'r') as file:
                self.inventory = []
                for line in file:
                    #assigns each value into variables by comma separation and removes extra whitespace
                    name, item_ID, quantity, price = line.strip().split(',')
                    self.add_item(name, int(item_ID), int(quantity), float(price))
            print("Inventory loaded from file.")
        except FileNotFoundError:
            print("No inventory file found.")

def main():

    #Instance of InventoryManager
    manager = InventoryManager()

    print("Welcome to the Inventory Manager!")
    #Loops options until user exits
    while True:
        print("\n1. Add an item")
        print("2. Update an item")
        print("3. View all items in inventory")
        print("4. Search for an item")
        print("5. Save inventory item data to file")
        print("6. Load inventory data from file")
        print("7. Exit")

        choice = input("Choose an option: ")

        #Adds item to inventory
        if choice == '1':

            #Input validation for inputs
            #Name can only be letters
            while True:
                name = input("Item's name: ")
                if name.isalpha():
                    break
                else:
                    print("Name must only contain letters.")

            #ID can only be positive numbers
            while True:
                try:
                    id = int(input("Item's ID: "))
                    if id < 0:
                        print("ID can only be positive")
                    else:
                        break
                except ValueError:
                    print("ID can only be numbers.")

            #Quantity can only be positive numbers
            while True:
                try:
                    quantity = int(input("Item's quantity: "))
                    if quantity < 0:
                        print("Quantity can only be positive")
                    else:
                        break
                except ValueError:
                    print("Quantity can only be a number.")

            #Price can only be positive numbers
            while True:
                try:
                    price = float(input("Item's price: "))
                    if price < 0:
                        print("Price can only be positive")
                    else:
                        break
                except ValueError:
                    print("Price can only be a number.")

            #Uses input for attributes
            manager.add_item(name, id, quantity, price)

        #Updates an item's quantity and/or price
        if choice == '2':
            try:
                #Validates number format
                item_id = int(input("Enter item's ID to update: "))
                found = False

                for item in manager.inventory:
                    if item.ID == item_id:
                        found = True
                        print("Item found. Enter new values:")

                        #Validates new quantity input for only positive numbers
                        while True:
                            try:
                                new_quantity = int(input("New quantity: "))
                                if new_quantity < 0:
                                    print("Quantity must be positive.")
                                else:
                                    break
                            except ValueError:
                                print("Quantity must be a number.")
                        
                        #Validates new price input for only positive numbers
                        while True:
                            try:
                                new_price = float(input("New price: "))
                                if new_price < 0:
                                    print("Price must be positive")
                                else:
                                    break
                            except ValueError:
                                print("Price must be a number.")

                        #Updates Item    
                        item.update_item(new_quantity, new_price)
                        break

                if not found:
                    print("Item not found.")

            except ValueError:
                print("Invalid ID format.")

        #Displays Inventory
        if choice == '3':
            manager.display_inventory()

        #Searches for an item in inventory
        elif choice == '4':

            keyword = input("Enter name to search: ")
            matching_items = manager.search_item(keyword)

            #If list contains value
            if matching_items:
                print("\nItems matching your search:")
                #Loops through list
                for item in matching_items:
                    print(item.display_item())
            else:
                print("No items found with that name.")

        #Saves inventory data to file
        elif choice == '5':
            manager.write_to_file()

        #Loads inventory data from file
        elif choice == '6':
            manager.read_from_file()

        #Exits Program
        elif choice == '7':
            print("Exiting program")
            break
        
        #If something other than the options is chosen
        else:
            print("Invalid Choice. Please try again.")


if __name__ == '__main__':
    main()