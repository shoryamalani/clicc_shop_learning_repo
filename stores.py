class Store:
    products = {}
    money = 0
    def __init__(self, name, products,start_money):
        self.name = name
        self.products = products
        self.money = start_money
    def show_items(self):
        text = ""
        for key, value in self.products.items():
            if value[1] > 0:
                text+= "{}: {}\n".format(key, value[0])
        return text.rstrip("\n")
    def show_items_with_quantity(self):
        text = ""
        for key, value in self.products.items():
            if value[1] > 0:
                text+= "{}: {} at the price {}\n".format(key, value[1], value[0])
        return text.rstrip("\n")
    def buy_item(self, item, quantity,current_money):
        if item in self.products:
            if self.products[item][1] > quantity:
                if self.products[item][0]*quantity <= current_money:
                    self.products[item][1] -= quantity
                    self.money += self.products[item][0]*quantity
                    return "You bought {} {} for {}$".format(quantity, item, self.products[item][0]*quantity)
                else:    
                    return "You can't afford {} {}".format(quantity, item)
            else:
                return "We don't have {} {}".format(quantity, item)
        else:
            return "We don't have {}".format(item)

    

# The format is "Product": [Price, Quantity]
items = {"Apples": [2,5], "Bananas": [3,3], "Oranges": [1,7]}
donalds_money = 10
if __name__ == "__main__":
    store = Store("SmalMart", items, 10)
    print(store.show_items())
    for i in range(5):
        print("What would you like to do?")
        print("1. Buy an item")
        print("2. Show items")
        print("3. Show items with quantity")
        print("4. Exit")
        choice = int(input())
        if choice == 1:
            print("What item would you like to buy?")
            print(store.show_items())
            item = input().lower().capitalize()
            print("How many would you like to buy: ")
            amount = int(input())
            print(store.buy_item(item, amount,donalds_money))
        
