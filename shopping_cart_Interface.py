import sys

def create_shopping_cart():
    # ... (function code remains the same)

def main_menu():
    while True:
        print("\nWelcome to the Shopping Cart!")
        print("1. Add items to cart")
        print("2. View cart")
        print("3. Remove item from cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice in ["1", "2", "3", "4", "5"]:
            if choice == "1":
                add_items_to_cart(cart)
            elif choice == "2":
                view_cart(cart)
            elif choice == "3":
                remove_item_from_cart(cart)
            elif choice == "4":
                checkout(cart)
            elif choice == "5":
                sys.exit()
        else:
            print("Invalid choice. Please try again.")

# Start the shopping cart app
cart = []
main_menu()
