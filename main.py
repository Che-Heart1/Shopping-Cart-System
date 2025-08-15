# Product catalog stored as dictionary: {product_name: (price, discount_eligible)}
catalog = {
    "indomie": (6.0, True),
    "milo": (1.5, False),
    "milk": (3.0, True),
    "gari olonka": (2.5, False),
    "bag of rice": (10.0, True)
}

# User's cart: {product_name: quantity}
cart = {}

def display_catalog():
    print("\n--- Product Catalog ---")
    for product, (price, discount) in catalog.items():
        discount_tag = " (Buy 3 get 1 free)" if discount else ""
        print(f"{product.title()} - ${price:.2f}{discount_tag}")

def add_to_cart():
    product = input("Enter product name to add: ").lower()
    if product in catalog:
        quantity = int(input(f"Enter quantity of {product}: "))
        cart[product] = cart.get(product, 0) + quantity
        print(f"{quantity} {product}(s) added to cart.")
    else:
        print("Product not found in catalog.")

def update_cart():
    product = input("Enter product name to update/remove: ").lower()
    if product in cart:
        action = input("Type 'update' to change quantity or 'remove' to delete: ").lower()
        if action == "update":
            quantity = int(input("Enter new quantity: "))
            if quantity > 0:
                cart[product] = quantity
                print(f"Updated {product} to quantity {quantity}.")
            else:
                print("Quantity must be at least 1.")
        elif action == "remove":
            del cart[product]
            print(f"{product} removed from cart.")
    else:
        print("Product not in cart.")

def calculate_total():
    total = 0
    for product, quantity in cart.items():
        price, discount_eligible = catalog[product]
        if discount_eligible and quantity >= 4:
            free_items = quantity // 4
            total += price * (quantity - free_items)
        else:
            total += price * quantity
    return total

def print_invoice():
    print("\n--- Final Invoice ---")
    print("{:<10} {:<10} {:<10}".format("Item", "Qty", "Price"))
    print("-" * 30)
    for product, quantity in cart.items():
        price, discount_eligible = catalog[product]
        if discount_eligible and quantity >= 4:
            free_items = quantity // 4
            cost = price * (quantity - free_items)
        else:
            cost = price * quantity
        print("{:<10} {:<10} ${:<10.2f}".format(product.title(), quantity, cost))
    total = calculate_total()
    print("-" * 30)
    print(f"Total: ${total:.2f}")

def main():
    while True:
        print("\n1. View Catalog")
        print("2. Add Product")
        print("3. Update/Remove Product")
        print("4. View Invoice")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            display_catalog()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            update_cart()
        elif choice == "4":
            print_invoice()
        elif choice == "5":
            print("Thanks for shopping!")
            break
        else:
            print("Invalid option. Try again.")

# Run the program
main()
