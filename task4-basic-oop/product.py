class Product:
    """

    A product with name, price, quantity.
    """
    def __init__(self, name, price, quantity):
        """

        Set the name, price, and quantity of the product.

        Raises: 
            ValueError: If price or quantity is negative.

        """
        if price < 0 :
            raise ValueError("Price must be Positive. ")
        if quantity < 0 :
            raise ValueError("Quantity must be Positive. ")
        
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount):
        """
        Add items to the stock.

        Raises:
            ValueError: If amount is neagative.

        """
        if amount < 0:
            raise ValueError("Amount must be positive. ")
        self.quantity += amount

    def remove_stock(self, amount):
        """
        Remove items from the stock if it's  available.
        
        Raises:
            ValueError: If amount is negative or exceeds stock.

        """
        if amount < 0 :
            raise ValueError("Amount must be postive. ")
        if amount > self.quantity:
            raise ValueError("Not Enough Stock. ")
        self.quantity -= amount

    def total_value(self):
        """
        Get the total value of the product.
        
        Returns: 
            float: Total value (price * quantity).
             
        """
        return self.price * self.quantity
    
    def show_info(self):
        """
        Print the Product details.
        """
        print("...Product's Information...")
        print("Name: ", self.name)
        print("Price: ", self.price)
        print("Quantity: ", self.quantity)
        print("Total Value: ", self.total_value())
