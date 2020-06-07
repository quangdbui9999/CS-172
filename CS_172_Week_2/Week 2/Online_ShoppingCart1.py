# Type code for classes here

class ItemToPurchase():
    def __init__(self, item_name = "none", item_price = 0.0, item_quantity = 0, item_description = "none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
        
    def cost_items(self):
        return self.item_price * self.item_quantity
    
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(self.cost_items())}")
    
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


if __name__ == "__main__":
    # Type main section of code here
    print("Item 1")
    item1 = ItemToPurchase(input("Enter the item name:\n"), float(input("Enter the item price:\n")), int(input("Enter the item quantity:\n")), input("Enter the item description:\n"))
    print("\nItem 2")
    item2 = ItemToPurchase(input("Enter the item name:\n"), float(input("Enter the item price:\n")), int(input("Enter the item quantity:\n")), input("Enter the item description:\n"))
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    
    print("ITEMS")
    item1.print_item_description()
    item2.print_item_description()
    
    total = item1.cost_items() + item2.cost_items()
    print(f"\nTotal: ${int(total)}")
    
'''
Chocolate Chips
3
1
Famous Amos
Bottled Water
1
10
Deer Park, 12 oz.
'''