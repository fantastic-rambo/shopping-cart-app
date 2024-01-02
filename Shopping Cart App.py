def create_shopping_cart():
    """Creates a shopping cart and provides options for user interaction."""

    cart = []  # Initialize an empty cart

    while True:
        print("\nWelcome to the Shopping Cart!")
        print("1. Add items to cart")
        print("2. View cart")
        print("3. Remove item from cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_items_to_cart(cart)
        elif choice == "2":
            view_cart(cart)
        elif choice == "3":
            remove_item_from_cart(cart)
        elif choice == "4":
            checkout(cart)
        elif choice == "5":
            break  # Exit the loop
        else:
            print("Invalid choice. Please try again.")

def add_items_to_cart(cart):
    """Allows the user to add items to the cart."""

    while True:
        product_name = input("Enter product name (or 'done' to finish): ")
        if product_name == "done":
            break

        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        cart.append({"name": product_name, "price": price, "quantity": quantity})

def view_cart(cart):
    """Displays the current items in the cart."""

    total_price = 0
    print("\nYour Shopping Cart:")
    print("------------------")
    for item in cart:
        print(f"{item['name']} - ${item['price']:.2f} x {item['quantity']} = ${item['price'] * item['quantity']:.2f}")
        total_price += item['price'] * item['quantity']

    print("------------------")
    print(f"Total price: ${total_price:.2f}")

def remove_item_from_cart(cart):
    """Allows the user to remove an item from the cart."""

    if cart:
        print("\nItems in your cart:")
        for i, item in enumerate(cart):
            print(f"{i+1}. {item['name']}")

        index_to_remove = int(input("Enter the index of the item to remove: ")) - 1
        cart.pop(index_to_remove)
        print("Item removed successfully!")
    else:
        print("Your cart is empty.")

def checkout(cart):
    """Processes the checkout and displays a summary."""

    # Implement checkout logic (e.g., payment processing, order confirmation)
    print("\nThank you for your purchase!")
    view_cart(cart)  # Display final cart summary
    cart.clear()  # Clear the cart for the next session

# Start the shopping cart app
create_shopping_cart()
