# Virtual Vending Machine 

vending_machine_products = [
    {"id":100, "name":"Meed Cookie", "price":2.00},
    {"id":101, "name":"Meed Cookie", "price":2.00},
    {"id":102, "name":"Lays MAX Spicy Mexican Potato Chips", "price":4.00},
    {"id":103, "name":"Lays Cheese-flavored Potato Chips", "price":4.00},
    {"id":104, "name":"Doritos Nacho Cheese", "price":4.00},
    {"id":105, "name":"Doritos Sweet Pepper", "price":4.00},
    {"id":106, "name":"Almarai Chocolate Milk", "price":3.00},
    {"id":107, "name":"Almarai Strawberry Milk", "price":3.00},
    {"id":108, "name":"M & M's", "price":4.00},
    {"id":109, "name":"M & M's", "price":4.00},
    {"id":110, "name":"Al Rabia Orange Juice", "price":3.00},
    {"id":111, "name":"Al Rabia Orange Juice", "price":3.00},
    {"id":112, "name":"Mars Chocolate Bar", "price":2.00},
    {"id":113, "name":"Galaxy Chocolate Bar", "price":2.00},
    {"id":112, "name":"Canned Ice Tea", "price":3.00},
    {"id":113, "name":"Canned Ice Tea", "price":3.00},
    {"id":114, "name":"Aquafina Bottle Water", "price":1.00},
    {"id":115, "name":"Aquafina Bottle Water", "price":1.00},
    {"id":116, "name":"Fruit Cake Slice", "price":3.00},
    {"id":117, "name":"Fruit Cake Slice", "price":3.00},
    {"id":118, "name":"Vimto Can", "price":2:00},
    {"id":118, "name":"Vimto Can", "price":2:00}
]

def vending_selector_mechanism (product_id):
    print(vending_machine_products)
    for product in vending_machine_products:
        if product["id"] == product_id:
            return product["name"], product["price"]
        
        

def vending_dispensing_mechanism ():
    print("Product Dispensed")

vending_selector_mechanism()