"""
7. Custom Exceptions for Business Logic
   - Create custom exception classes `OutOfStockError` and `InvalidOrderError`. Write a function `process_order` that takes an order (a dictionary with item names and quantities) and a stock (a dictionary with item names and available quantities) as arguments. Use exception handling to manage:
     - Out of stock items (raise `OutOfStockError` with a suitable message).
     - Invalid order quantities (e.g., negative or zero, raise `InvalidOrderError` with a suitable message).
   - Test the function with various orders and stock scenarios.
"""
class OutOfStockError(Exception):
    def __init__(self, item):
        self.item = item
        super().__init__(f"Item '{item}' is out of stock.")

class InvalidOrderError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
def process_order(order, stock):
    try:
        for item, quantity in order.items():
            if item not in stock or stock[item] <= 0:
                raise OutOfStockError(item)
            if quantity <= 0:
                raise InvalidOrderError(f"Invalid quantity ({quantity}) for item '{item}'.")
            if quantity > stock[item]:
                raise OutOfStockError(item)

            stock[item] -= quantity
        print("Order processed successfully.")
    except OutOfStockError as e:
        print(f"Error: {e}")
    except InvalidOrderError as e:
        print(f"Error: {e}")

