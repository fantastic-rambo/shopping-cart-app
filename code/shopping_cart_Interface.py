import tkinter as tk
from tkinter import simpledialog

class ShoppingCartApp:
    def __init__(self):
        self.cart = []

        self.root = tk.Tk()
        self.root.title("Rambo City Shopping Center")

        # Set background color
        self.root.configure(bg="#ff5733")  # You can change the color code as per your preference

        # Increase the size of the window by adjusting the geometry
        self.root.geometry("600x400")

        # Add a canvas for the logo
##        self.canvas = tk.Canvas(self.root, width=100, height=100, bg="#e6e6e6")  # Adjust width and height as needed
##        self.canvas.pack()

        # Add a logo image (replace 'logo.png' with the actual file name)
##        logo_image = tk.PhotoImage(file="cart-logo.png")  # Make sure to place the logo file in the same directory as your script
##        self.canvas.create_image(50, 50, image=logo_image)

        self.label = tk.Label(self.root, text="Welcome to the Shopping Cart!", font=("Helvetica", 14), bg="#e6e6e6")
        self.label.pack()

        # Increase button sizes and adjust font size
        button_options = {"width": 20, "height": 2, "font": ("Helvetica", 12)}

        self.button_add = tk.Button(self.root, text="Add items to cart", command=self.add_items_to_cart, **button_options)
        self.button_add.pack()

        self.button_view = tk.Button(self.root, text="View cart", command=self.view_cart, **button_options)
        self.button_view.pack()

        self.button_remove = tk.Button(self.root, text="Remove item from cart", command=self.remove_item_from_cart, **button_options)
        self.button_remove.pack()

        self.button_checkout = tk.Button(self.root, text="Checkout", command=self.checkout, **button_options)
        self.button_checkout.pack()

        self.button_exit = tk.Button(self.root, text="Exit", command=self.root.destroy, **button_options)
        self.button_exit.pack()

    def add_items_to_cart(self):
        product_name = simpledialog.askstring("Product Name", "Enter product name (or 'done' to finish):")
        if product_name and product_name.lower() != "done":
            try:
                price = float(simpledialog.askstring("Price", "Enter price:"))
                quantity = int(simpledialog.askstring("Quantity", "Enter quantity:"))
                if price >= 0 and quantity >= 0:
                    self.cart.append({"name": product_name, "price": price, "quantity": quantity})
                    self.show_message("Item added to cart successfully!")
                else:
                    self.show_message("Price and quantity must be non-negative.")
            except ValueError:
                self.show_message("Invalid input. Please enter valid numeric values.")
        self.label.config(text="Welcome to the Shopping Cart!")

    def view_cart(self):
        self.label.config(text="Your Shopping Cart:")
        if not self.cart:
            self.show_message("Your cart is empty.")
        else:
            total_price = 0
            cart_text = "Product\t\tPrice\tQuantity\tTotal\n"
            cart_text += "-" * 40 + "\n"
            for item in self.cart:
                item_total = item['price'] * item['quantity']
                total_price += item_total
                cart_text += f"{item['name']}\t${item['price']:.2f}\t{item['quantity']}\t${item_total:.2f}\n"
            cart_text += "-" * 40 + f"\nTotal Price: ${total_price:.2f}"
            self.show_message(cart_text)

    def remove_item_from_cart(self):
        if not self.cart:
            self.show_message("Your cart is empty.")
        else:
            item_names = [item['name'] for item in self.cart]
            selected_item = simpledialog.askstring("Remove Item", "Select item to remove:", autocomplete=item_names)
            if selected_item:
                for i, item in enumerate(self.cart):
                    if item['name'] == selected_item:
                        self.cart.pop(i)
                        self.show_message(f"{selected_item} removed from the cart.")
                        break

    def checkout(self):
        if not self.cart:
            self.show_message("Your cart is empty. Nothing to checkout.")
        else:
            total_price = sum(item['price'] * item['quantity'] for item in self.cart)
            self.show_message(f"Thank you for your purchase!\nTotal Price: ${total_price:.2f}")
            self.cart.clear()

    def show_message(self, message):
        self.label.config(text=message)


if __name__ == "__main__":
    app = ShoppingCartApp()
    app.root.mainloop()
