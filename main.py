class Pizza:
    def __init__(self, name,size, toppings, price):
        self.name = name
        self.size = size
        self.toppings = toppings
        self.price = price 
        
    def __str__(self):
        return f"{self.size} {self.name} Pizza with {','.join(self.toppings)}"







def display_menu():
    print("Welcome to Pizza Paradise")
    print("Choose your pizza")
    for i, pizza in enumerate(pizza_menu, start=1):
        print(f"{i}. {pizza.name} - ${pizza.price}")
        

def order_pizza():
    selection = int(input("Enter the number of your chosen pizza: "))
    selected_pizza = pizza_menu[selection - 1]   
    
    size = input("Enter pizza size (small, medium, large)").lower()
    while size not in ["small", "medium","large"]:
        size = input("Enter pizza size (small, medium, large)").lower() 
        
    toppings = input("Enter toppings (comma seperated): ").split(",")
    num_pizzas= int(input("Enter the number of pizzas: "))  
    
    total_price = selected_pizza.price*num_pizzas
    print("\nOrder Summery: ")
    print(f"Pizza: {selected_pizza}")
    print(f"Size: {size}")
    print(f"Toppings: {','.join(toppings)}")
    print(f"Number of pizzas: {num_pizzas}")
    print(f"Total Price: ${total_price}")











#Main program
pizza_menu =[
Pizza("Margarita", "Cheese Burst", ["Tomato Sauce", "Mozarella Cheese"], 10),
Pizza("Pepperoni", "Regular Crust", ["Tomato Sauce", "Pepperoni", "Mozzarella Cheese"], 12),
Pizza("Vegetarian", "Thin Crust", ["Tomato Sauce", "Mushrooms", "Bell Peppers", "Onions"], 11),
Pizza("Hawaiian", "Regular Crust", ["Tomato Sauce", "Ham", "Pineapple", "Mozzarella Cheese"], 13),
Pizza("BBQ Chicken", "Thick Crust", ["BBQ Sauce", "Grilled Chicken", "Onions", "Mozzarella Cheese"], 14)
]



display_menu()
order_pizza()