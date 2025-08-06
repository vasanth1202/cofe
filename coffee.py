# class Coffee:
#     #initialize coffee with  price and name
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price

#     class order:        
#         #initilize order with empty list
#         def __init__(self):
#             self.items =[]

#         #add coffee to order
#         def add_item(self,Coffee):
#             self.items.append(Coffee)
#             print(f"Added {Coffee.name} to your order.")

#         #calculate total price
#         def total(self):
#             return sum(item.price for item in self.items)
        
#         #show order summery 
#         def show_order(self):
#             if not self.items:
#                 print("no item is order")
#                 return
#         print("\n your order:")

#         for i,item in enumerate(self.items,1): # type: ignore
#             print(f"{i}.{item.name} - ${item.price}")
#         print(f"total:${self.total()}\n") # type: ignore
        
#         #show checkout proces
#         def checkout(self):
#             if not self.items:
#                 print("YOur cart is empty.")
#                 return
#             self.show_order()
#             confirm =input("process to checkout? (yes/no):").strip().lower()
#             if confirm =='yes':
#                 print("order confirmed! Thankyou.")
#                 self.items.clear()
#             else:
#                 print("Checkout canceld.")

# #display menu and handle user input

# def main():
#     menu = [
#         Coffee("Espresso",2.0),
#         Coffee("Clack cofe",3.5),
#         Coffee("Latte",4.5),
#         Coffee("cappuccino",3.0),
#         Coffee("Americono",5.0)
#     ]
#     order =order()
    
#     #user interaction
#     while True:
#         print("\n-----Cofee menu-----")
#         for i,Coffee in enumerate(menu,1):
#             print(f"{i}.{Coffee.name} -$ {Coffee.price}")
#         print("5.viwe order")
#         print("6.Checkout")
#         print("7.Exit")
#         choice =input("Choose an option")
#         if choice in ['1','2','3','4']:
#             order.add_items(menu[int(choice)-1])
#         elif choice =='5':
#             order.show_order()
#         elif choice =='6':
#             order.show_checkout()
#         elif choice =='7':
#             print("Tank you for visiting .Good bye")
#             break
#         else:
#             print("invalied choice. try again")
# if __name__ =="__main__":
#     main()


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