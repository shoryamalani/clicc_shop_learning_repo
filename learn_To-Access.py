products = {"Bananananan":{"price":12},"applee":{"price":3},"Rachaels hair":{"price":1,"value":"It kinda sucks bro"},"water gun":{"price":3},}
employees = [1234124,12,41,24,124124,1,24124]
# print(employees[1])
# print(products["Rachaels hair"])

class Store:
    products = {}
    money = 0
    def __init__(self, name, products,start_money):
        self.name = name
        self.products = products
        self.money = start_money
    
keckosStore = Store("keckos",products,10)
print(keckosStore.products["Rachaels hair"])
print(type(keckosStore.products))
print(type(keckosStore.products["Rachaels hair"]))
print(keckosStore.products["Rachaels hair"]["value"])
