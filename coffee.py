# this is a simple coffee ordering system
# it allows users to select coffee from a menu, add items to their order, view their order, and checkout


class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, coffee):
        self.items.append(coffee)
        print(f"Added {coffee.name} to your order.")

    def total(self):
        return sum(item.price for item in self.items)

    def show_order(self):
        if not self.items:
            print("No item is ordered")
            return
        print("\nYour order:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ${item.price}")
        print(f"Total: ${self.total()}\n")

    def checkout(self):
        if not self.items:
            print("Your cart is empty.")
            return
        self.show_order()
        confirm = input("Proceed to checkout? (1/0): ").strip().lower()
        if confirm == '1':
            print("Order confirmed! Thank you.")
            self.items.clear()
        else:
            print("Checkout canceled.")

def main():
    menu = [
        Coffee("Espresso", 2.0),
        Coffee("Black coffee", 3.5),
        Coffee("Latte", 4.5),
        Coffee("Cappuccino", 3.0),
        Coffee("Americano", 5.0)
    ]
    order = Order()
    while True:
        print("\n-----Coffee menu-----")
        for i, coffee in enumerate(menu, 1):
            print(f"{i}. {coffee.name} - $ {coffee.price}")
        print("6. View order")
        print("7. Checkout")
        print("8. Exit")
        choice = input("Choose an option: ")
        if choice in ['1', '2', '3', '4','5']:
            order.add_item(menu[int(choice) - 1])
        elif choice == '6':
            order.show_order()
        elif choice == '7':
            order.checkout()
        elif choice == '8':
            print("Thank you for visiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()