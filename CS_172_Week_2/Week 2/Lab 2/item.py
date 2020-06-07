import datetime

class Item():
    def __init__(self, name = "none", price = 0.0, taxable = ""):
        self.__name = name
        self.__price = price
        self.__taxable = taxable

    def __str__(self):
        result = ""
        return result

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def getTax(self, tax_rate):
        taxCharged = 0
        if(self.__taxable == "yes"):
            taxCharged = self.__price * tax_rate
        else:
            taxCharged = 0
        return taxCharged

class Receipt():
    def __init__(self, tax_rate = 0.0, purchases = []):
        self.__tax_rate = tax_rate
        self.__purchases = purchases

    def setPurchases(self, new_item):
        self.__purchases = new_item

    def __str__(self):
        full_receipt = ""
        total = self.get_tax() + self.get_sub_total()

        dateAndTime = str(datetime.datetime.now())
        full_receipt += f"----- Receipt {dateAndTime} -----\n"
        full_receipt += self.list_price_item()

        full_receipt += "\n{:_<20s}{:_>20.2f}\n".format("Sub Total", self.get_sub_total())
        full_receipt += "{:_<20s}{:_>20.2f}\n".format("Tax", self.get_tax())
        full_receipt += "{:_<20s}{:_>20.2f}\n".format("Total", total)

        return full_receipt

    def addItem(self, whatItem):
        self.__purchases.append(whatItem)

    def list_price_item(self):
        result = ""
        for item in self.__purchases:
            result += "{:_<20s}{:_>20.2f}\n".format(item.getName(), item.getPrice())
        return result

    def get_sub_total(self):
        sub_total = 0
        for item in self.__purchases:
            sub_total += item.getPrice()
        return sub_total

    def get_tax(self):
        total_tax = 0
        for item in self.__purchases:
            total_tax += item.getTax(0.07)
        return total_tax




if __name__ == "__main__":

    print(f"Welcome to Receipt Creator")
    item_name = input(f"Enter Item name: ")
    item_price = float(input(f"Enter Item Price: "))
    item_taxable = input(f"Is the item taxable (yes/no): ")

    item = Item(item_name, item_price, item_taxable)
    receipt = Receipt(0.07)
    receipt.setPurchases([item])


    add_product = input(f"Add another item (yes/no): ")

    while(add_product == "yes"):
        if(add_product == "yes"):
            item_name = input(f"Enter Item name: ")
            item_price = float(input(f"Enter Item Price: "))
            item_taxable = input(f"Is the item taxable (yes/no): ")
            new_item = Item(item_name, item_price, item_taxable)
            receipt.addItem(new_item)
        elif add_product == "no":
            print("no")
            break
        add_product = input(f"Add another item (yes/no): ")
    print(receipt)

'''
----- Receipt 2018-01-02 16:21:49.515170 -----
Hot Dog_____________________________5.15
Soda________________________________2.50
Pretzel_____________________________0.50
Candy Bar___________________________1.25

Sub Total___________________________9.40
Tax_________________________________0.26
Total_______________________________9.66

Each item listed with it's price.
The total cost of the items.
The total tax charged on all items.
The grand total with tax added.
The current date when the receipt we generated.
All values must be shown to two decimal places.
'''