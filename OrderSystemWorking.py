import json
import os

# Path to the JSON file where order data will be saved
orderDataFile = "orders.json"

# Menu data: The restaurant's menu categorised into mains, drinks, and desserts
Menu = {
    "Mains": [
        {"name": "Tomato Soup", "price": 4},
        {"name": "MeatFeast Pizza", "price": 8},
        {"name": "Tuna Mayo Sandwich", "price": 4},
        {"name": "Pasta Bolognese", "price": 7},
        {"name": "Hamburger", "price": 5},
        {"name": "Beef Steak", "price": 10}
    ],
    "Drinks": [
        {"name": "Coca-Cola", "price": 3},
        {"name": "Pepsi", "price": 3},
        {"name": "Sprite", "price": 3},
        {"name": "Fruit tea", "price": 2},
        {"name": "Coffee", "price": 4},
        {"name": "Green tea", "price": 2},
        {"name": "Bottled Water", "price": 2}
    ],
    "Desserts": [
        {"name": "Cheesecake", "price": 3},
        {"name": "Apple Pie", "price": 4},
        {"name": "Strawberry Pudding", "price": 3},
        {"name": "Brownies", "price": 2},
        {"name": "Crepes", "price": 1},
        {"name": "Ice Cream", "price": 5}
    ]
}


# Load order data from JSON file, or create an empty list if file does not exist
# This ensures the program can continue smoothly even if the file is missing
def loadOrders():
    if os.path.exists(orderDataFile):
        with open(orderDataFile, "r") as file:
            return json.load(file)  # Load the stored orders into memory
    else:
        return [] # Return an empty list if the file does not exist

# Save order data to JSON file for continuity across sessions
def saveOrders(orders):
    with open(orderDataFile, "w") as file:
        json.dump(orders, fp=file, indent=4) # Save orders with good formatting


# Display menu to the user with categories and items
def displayMenu():
    print("Menu:")
    for category, items in Menu.items():
        print(f"{category}:")
        for item in items:
            print(f"  {item['name']} - £{item['price']}") # Display each item's name and price


# This is the Main order processing function
# Guides the user through the order process step-by-step
def processOrder():
    print("Welcome to our Restaurant!") # Greet the customer
    displayMenu()
    orderList, totalCost = takeOrder() # Take orders from the customer
    confirmOrder(orderList, totalCost) # Confirm the order and save it


# Take order from customer
# The function loops until the customer finalises their order
def takeOrder():
    orderList = [] # Store individual order items
    totalCost = 0

    while True:
        itemName = input("Enter item name to add to order (or type 'done' to finish): ").strip()
        if itemName.lower() == 'done': # Exit the loop if the customer is done ordering
            break

        itemFound = False # Flag to check if the item exists in the menu
        for category, items in Menu.items():
            for item in items:
                if itemName.lower() == item['name'].lower():  # Case-insensitive match for item name
                    customisationCost = customiseOrder() # Ask for customisation
                    totalItemCost = item['price'] + customisationCost # Calculate item cost with customisation
                    orderList.append({
                        "name": item['name'],
                        "price": item['price'],
                        "customisationCost": customisationCost,
                        "totalCost": totalItemCost
                    }) # Add item details to the order list
                    totalCost += totalItemCost # Update the total cost
                    print(f"Added {item['name']} to order with a total cost of £{totalItemCost}.")
                    itemFound = True # Show the item as found
                    break
            if itemFound:
                break

        if not itemFound: # Inform the customer if the item was not found in the menu
            print("Item not found on the menu.")

    return orderList, totalCost


# Handle item customisation
# Shows the customer the option to customise their item
def customiseOrder():
    customisationInput = input("Would you like to customise (Yes/No)? ").strip().lower()
    if customisationInput == "yes":
        return 1  # Customisation adds a cost of £1
    else:
        return 0 # No customisation cost


# Calculate the total cost including tax
def calculateTotalCost(totalCost):
    taxRate = 0.2 # Define a fixed tax rate of 20%
    return totalCost + (totalCost * taxRate) # Return the total cost with tax applied


# Display the summary of the customer's order
# Provides details of each item and the overall total cost
def displayOrderSummary(orderList, totalCost):
    print("\nOrder Summary:")
    for item in orderList:
        print(f"{item['name']} - £{item['price']} + Customisation £{item['customisationCost']} = £{item['totalCost']}")
    print(f"Subtotal: £{totalCost}")
    totalWithTax = calculateTotalCost(totalCost)
    print(f"Total with tax: £{totalWithTax}")
    return totalWithTax


# Confirm the customer's order
# Saves the order if confirmed, or cancels otherwise
def confirmOrder(orderList, totalCost):
    confirmation = input("Would you like to confirm this order (Yes/No)? ").strip().lower()
    if confirmation == "yes":
        finalCost = displayOrderSummary(orderList, totalCost) # Shows final cost
        generateReceipt(orderList, finalCost) # Generates the receipt
        saveOrders(orderList) # Save the confirmed order
        print("Order confirmed!")
    else:
        cancelOrder() # Cancel the order


# Generate and display a receipt of the order
def generateReceipt(orderList, finalCost):
    print("\nReceipt:")
    for item in orderList:
        print(f"{item['name']} - £{item['price']} + Customisation £{item['customisationCost']} = £{item['totalCost']}")
    print(f"Total Cost with tax: £{finalCost}")
    print("Thank you for your order!") # Show a "Thank You" message


# Cancel order
def cancelOrder():
    print("Order cancelled.") # inform the customer that the order was cancelled



# Run the order processing system
processOrder()


# It prints the saved orders
print("Here are the saved orders:")
print(loadOrders())


# Menu data for testing
#Menu = {
    #"Mains": [
        #{"name": "Tomato Soup", "price": 4},
        #{"name": "MeatFeast Pizza", "price": 8},
    #],
    #"Drinks": [
        #{"name": "Coca-Cola", "price": 3},
        #{"name": "Pepsi", "price": 3},
    #],
#}

# Function to test
#def displayMenu():
    #print("Menu:")
    #for category, items in Menu.items():
        #print(f"{category}:")
        #for item in items:
            #print(f"  {item['name']} - £{item['price']}")

# Manual Test
#displayMenu()
