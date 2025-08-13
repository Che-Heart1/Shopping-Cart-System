# Simple CLI Shopping System with Discounts

# Product catalog: product -> price
catalog = {
    "apple": 0.50,
    "banana": 0.30,
    "bread": 1.50,
    "milk": 1.20,
    "eggs": 2.00,
    "cheese": 2.50,
    "chocolate": 1.00,
    "coffee": 3.00
}

# Cart: product -> quantity
cart = {}

DISCOUNT_THRESHOLD = 20.00  # dollars
DISCOUNT_PERCENT = 10       # percent

def display_catalog():
    print("\n--- Product Catalog ---")
    for product, price in catalog.items():
        print(f"{product.title():<15} ${price:.2f}")
    print()

def display_cart():
    if not cart:
        print("\nYour cart is empty.")
        return
    print("\n--- Your Shopping Cart ---")
    for product, quantity in cart.items():
        unit_price = catalog[product]
        total_price = unit_price * quantity
        print(f"{product.title():<15} x{quantity:<3} @ ${unit_price:.2f} = ${total_price:.2f}")
    print()

def add_to_cart():
    product = input("Enter product name to add: ").strip().lower()
    if product not in catalog:
        print("Product not found.")
        return
    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return
        cart[product] = cart.get(product, 0) + quantity
        print(f"Added {quantity} x {product} to cart.")
    except ValueError:
        print("Invalid quantity.")

def update_cart():
    product = input("Enter product name to update/remove: ").strip().lower()
    if product not in cart:
        print("Item not in cart.")
        return
    try:
        new_quantity = int(input("Enter new quantity (0 to remove): "))
        if new_quantity < 0:
            print("Quantity can't be negative.")
        elif new_quantity == 0:
            del cart[product]
            print(f"Removed {product} from cart.")
        else:
            cart[product] = new_quantity
            print(f"Updated {product} to {new_quantity}.")
    except ValueError:
        print("Invalid quantity.")

def calculate_total():
    return sum(catalog[product] * quantity for product, quantity in cart.items())

def apply_discount(total):
    if total >= DISCOUNT_THRESHOLD:
        discount = (DISCOUNT_PERCENT / 100) * total
        return discount
    return 0.0

def checkout():
    print("\n--- Final Invoice ---")
    if not cart:
        print("Your cart is empty.")
        return

    total = 0.0
    for product, quantity in cart.items():
        unit_price = catalog[product]
        subtotal = unit_price * quantity
        total += subtotal
        print(f"{product.title():<15} x{quantity:<3} @ ${unit_price:.2f} = ${subtotal:.2f}")

    discount = apply_discount(total)
    final_total = total - discount

    print(f"\nSubtotal: ${total:.2f}")
    if discount > 0:
        print(f"Discount ({DISCOUNT_PERCENT}%): -${discount:.2f}")
    print(f"Total Due: ${final_total:.2f}")
    print("Thank you for shopping!")

def main():
    while True:
        print("\n--- Shopping Menu ---")
        print("1. View Catalog")
        print("2. View Cart")
        print("3. Add to Cart")
        print("4. Update/Remove Item")
        print("5. Checkout & Exit")
        choice = input("Enter choice (1-5): ").strip()

        if choice == '1':
            display_catalog()
        elif choice == '2':
            display_cart()
        elif choice == '3':
            display_catalog()
            add_to_cart()
        elif choice == '4':
            display_cart()
            update_cart()
        elif choice == '5':
            checkout()
            break
        else:
            print("Invalid choice. Try again.")

if _name_ == "_main_":
    main()
