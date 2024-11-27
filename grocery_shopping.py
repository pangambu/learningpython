

def main():
    grocery_items = [
        {"name": "Apples", "price": 2.5},
        {"name": "Bananas", "price": 1.75},
        {"name": "Milk", "price": 3.0},
        {"name": "Bread", "price": 2.0},
        {"name": "Eggs", "price": 2.25},
        {"name": "Cheese", "price": 5.0},
        {"name": "Chicken", "price": 7.5},
        {"name": "Rice", "price": 4.0},
        {"name": "Tomatos", "price": 2.0},
        {"name": "Potatoes", "price": 1.5}
        
    ]
    
    cart = [] 
    
    while True:
        show_grocery_items(grocery_items)
        choice = int(input("Enter the number of the grocery item you  want to buy: "))
        quatity = int(input("Enter the quatity: "))
        
        selected_item = grocery_items[choice - 1]
        selected_item['quantity'] = quatity
        cart.append(selected_item)
        
        another_item = input("Do you want to add another items? (yes/no)").lower()
        if another_item != yes:
            break
    
    
    print("\nItems in your shopping cart: ")
    for item in cart:
        print(f"{item['name']}: {item['quantity']} x ${item['price']:.2f} = ${item['quantity'] * item['price']:.2f}")

        
    
    