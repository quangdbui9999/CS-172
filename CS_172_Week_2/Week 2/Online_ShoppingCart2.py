class ItemToPurchase():
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
        
    def set_item_quantity(self, new_one_quantity):
        self.item_quantity = new_one_quantity

    def cost_items(self):
        return self.item_price * self.item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(self.cost_items())}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart():
    def __init__(self, customer_name="none", current_date="January 1, 2016", cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def set_customer_name(self, who):
        self.customer_name = who

    def set_current_date(self, when):
        self.current_date = when

    def set_cart_item(self, what_items):
        self.cart_items = what_items

    def get_num_items_in_cart(self):
        # item_quantity
        item_total = 0
        for product in range(len(self.cart_items)):
            item_total += self.cart_items[product].item_quantity
        return item_total

    def get_cost_of_cart(self):
        total_cost = 0
        for product in self.cart_items:
            total_cost = total_cost + int(product.cost_items())
        return total_cost

    def add_item(self, what_item):
        self.cart_items.append(what_item)

    def remove_item(self):
        print("REMOVE ITEM FROM CART")
        product_remove = input("Enter name of item to remove:\n")
        remove_success = False
        for product in range(len(self.cart_items)):
            #print(f"ten san pham: {self.cart_items[product].item_name}")
            if(product_remove == self.cart_items[product].item_name):
                del self.cart_items[product]
                remove_success = True
                break
            else:
                remove_success = False
        if(remove_success == False):
            print("Item not found in cart. Nothing removed.")

    def modify_item(self):
        find_product = False
        print("\nCHANGE ITEM QUANTITY")
        product_change = input("Enter the item name:\n")
        new_quantity = int(input("Enter the new quantity:\n"))
        for product in range(len(self.cart_items)):
            if(product_change == self.cart_items[product].item_name):
                self.cart_items[product].set_item_quantity(new_quantity)
                find_product = True
            else:
                find_product = False
        
        if(find_product == False):
            print("Item not found in cart. Nothing modified.")

    def print_total(self):
        print("OUTPUT SHOPPING CART")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}\n")
        if self.get_num_items_in_cart() == 0:
            print(f"SHOPPING CART IS EMPTY")
        else:
            for product in self.cart_items:
                product.print_item_cost()

        print(f"\nTotal: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("\nItem Descriptions")
        for product in self.cart_items:
            product.print_item_description()

    def output_information(self):
        print(f"\nCustomer name: {self.customer_name}")
        print(f"Today's date: {self.current_date}")

    def menuShoppingCart(self):
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit\n")


def print_menu(cart):
    menu_option = ""
    cart = ShoppingCart()
    cart.set_customer_name(name)
    cart.set_current_date(date)
    cart.menuShoppingCart()
    
    while menu_option != "q":
        # while menu_option != 'a' and menu_option != 'r' and menu_option != 'c' and menu_option != 'i' and menu_option != 'o' and menu_option != 'q':
        menu_option = input("Choose an option:\n")
        if menu_option == "a":
            print("\nADD ITEM TO CART")
            product_name = input("Enter the item name:\n")
            product_description = input("Enter the item description:\n")
            product_price = float(input("Enter the item price:\n"))
            product_quantity = int(input("Enter the item quantity:\n"))
            
            new_item = ItemToPurchase(product_name, product_price, product_quantity, product_description)
            
            cart.add_item(new_item)
            cart.menuShoppingCart()
        elif menu_option == "r":
            cart.remove_item()
            cart.menuShoppingCart()
        elif menu_option == "c":
            cart.modify_item()
            cart.menuShoppingCart()
        elif menu_option == "i":
            cart.print_descriptions()
            cart.menuShoppingCart()
        elif menu_option == "o":
            cart.print_total()
            cart.menuShoppingCart()
        elif menu_option == "q":
            break
        else:
            menu_option = input("Choose an option:\n")


if __name__ == "__main__":
    item1 = ItemToPurchase('Nike Romaleos', 189, 2, "Volt color, Weightlifting shoes")
    item2 = ItemToPurchase('Chocolate Chips', 3, 5, "Semi-sweet")
    item3 = ItemToPurchase('Powerbeats 2 Headphones', 128, 1, "Bluetooth headphones")

    shoppingCart = ShoppingCart()
    name = input("Enter customer's name:\n")
    date = input("Enter today's date:\n")
    shoppingCart.set_customer_name(name)
    shoppingCart.set_current_date(date)
    shoppingCart.set_cart_item([item1, item2, item3])

    shoppingCart.output_information()
    newShoppingCart = ShoppingCart()

    print_menu(newShoppingCart)