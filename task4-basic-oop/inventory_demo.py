# inventory_demo.py

from product import Product

if __name__ =="__main__":
    print("=== Inventory System ===")
    try:
        name = input("Enter the product name: ")
        price = float(input("Enter the product price: "))
        quantity = int(input("Enter the product quantity: "))   

        product = Product(name, price, quantity)
        product.show_info()

        the_choice = input("Do you want to add stock? yes/no :")
        if the_choice.lower() == "yes":
            add = int(input("Enter amount to add: "))
            product.add_stock(add)
            print("Stock added successfully.")
            product.show_info()

        the_choice = input("Do you want to remove the stock? yes/no :")
        if the_choice.lower() == "yes":
            remove = int(input("Enter amount to remove : "))
            product.remove_stock(remove)
            print("Stock removed successfully")
            product.show_info()

    except ValueError as e :
            print("error:", e)        