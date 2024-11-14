import json
import os

# Path to the JSON file where order data will be saved
orderDataFile = "orders.json"

# Menu data
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
def loadOrders():
    if os.path.exists(orderDataFile):
        with open(orderDataFile, "r") as file:
            return json.load(file)
    else:
        return []


# Save order data to JSON file
def saveOrders(orders):
    with open(orderDataFile, "w") as file:
        json.dump(orders, fp=file, indent=4)


# Display menu
def displayMenu():
    print("Menu:")
    for category, items in Menu.items():
        print(f"{category}:")
        for item in items:
            print(f"  {item['name']} - £{item['price']}")


# This is the Main order processing function
def processOrder():
    print("Welcome to our Restaurant!")
    displayMenu()
    orderList, totalCost = takeOrder()
    confirmOrder(orderList, totalCost)


# Take order from customer
def takeOrder():
    orderList = []
    totalCost = 0

    while True:
        itemName = input("Enter item name to add to order (or type 'done' to finish): ").strip()
        if itemName.lower() == 'done':
            break

        itemFound = False
        for category, items in Menu.items():
            for item in items:
                if itemName.lower() == item['name'].lower():
                    customisationCost = customiseOrder()
                    totalItemCost = item['price'] + customisationCost
                    orderList.append({
                        "name": item['name'],
                        "price": item['price'],
                        "customisationCost": customisationCost,
                        "totalCost": totalItemCost
                    })
                    totalCost += totalItemCost
                    print(f"Added {item['name']} to order with a total cost of £{totalItemCost}.")
                    itemFound = True
                    break
            if itemFound:
                break

        if not itemFound:
            print("Item not found on the menu.")

    return orderList, totalCost


# Handle item customisation
def customiseOrder():
    customisationInput = input("Would you like to customise (Yes/No)? ").strip().lower()
    if customisationInput == "yes":
        return 1  # Customisation adds a cost of £1
    else:
        return 0


# Calculate the total cost including tax
def calculateTotalCost(totalCost):
    taxRate = 0.2
    return totalCost + (totalCost * taxRate)


# Display order summary
def displayOrderSummary(orderList, totalCost):
    print("\nOrder Summary:")
    for item in orderList:
        print(f"{item['name']} - £{item['price']} + Customisation £{item['customisationCost']} = £{item['totalCost']}")
    print(f"Subtotal: £{totalCost}")
    totalWithTax = calculateTotalCost(totalCost)
    print(f"Total with tax: £{totalWithTax}")
    return totalWithTax


# Confirm order
def confirmOrder(orderList, totalCost):
    confirmation = input("Would you like to confirm this order (Yes/No)? ").strip().lower()
    if confirmation == "yes":
        finalCost = displayOrderSummary(orderList, totalCost)
        generateReceipt(orderList, finalCost)
        saveOrders(orderList)
        print("Order confirmed!")
    else:
        cancelOrder()


# Generate and display receipt
def generateReceipt(orderList, finalCost):
    print("\nReceipt:")
    for item in orderList:
        print(f"{item['name']} - £{item['price']} + Customisation £{item['customisationCost']} = £{item['totalCost']}")
    print(f"Total Cost with tax: £{finalCost}")
    print("Thank you for your order!")


# Cancel order
def cancelOrder():
    print("Order cancelled.")


# Run the order processing system
processOrder()