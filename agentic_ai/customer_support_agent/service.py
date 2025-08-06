fake_shop_data = {
    "name": "Mobile Kingdom",
    "address": "123 Main St, Springfield, USA",
    "phone": "+1-555-1234",
    "email": "info@mobilekingdom.com",
    "opening_hours": {
        "Monday": "9:00 AM - 9:00 PM",
        "Tuesday": "9:00 AM - 9:00 PM",
        "Wednesday": "9:00 AM - 9:00 PM",
        "Thursday": "9:00 AM - 9:00 PM",
        "Friday": "9:00 AM - 10:00 PM",
        "Saturday": "10:00 AM - 10:00 PM",
        "Sunday": "10:00 AM - 8:00 PM",
    },
}

fake_stocks = [
    {
        "item": "Iphone 14",
        "quantity": 50,
        "price": 999.99,
        "description": "Latest model of Apple's smartphone with advanced features.",
    },
    {
        "item": "Samsung Galaxy S22",
        "quantity": 30,
        "price": 899.99,
        "description": "Flagship smartphone from Samsung with high-end specifications.",
    },
    {
        "item": "Google Pixel 6",
        "quantity": 20,
        "price": 599.99,
        "description": "Google's latest smartphone with stock Android experience.",
    },
    {
        "item": "OnePlus 9",
        "quantity": 25,
        "price": 749.99,
        "description": "High-performance smartphone with fast charging capabilities.",
    },
]


class Service:
    def __init__(self):
        self.shop_info = fake_shop_data.copy()
        self.stocks = fake_stocks.copy()
        self.cart = {}

    def get_shop_info(self):
        return self.shop_info

    def get_stocks(self):
        return self.stocks

    def get_cart(self):
        return self.cart

    def add_to_cart(self, item_name: str, quantity: int):
        for item in self.stocks:
            if item["item"].lower() == item_name.lower():
                if item["quantity"] >= quantity:
                    self.cart[item["item"]] = {
                        "quantity": quantity,
                        "price": item["price"],
                    }
                    return True
                else:
                    raise ValueError(
                        f"Insufficient stock for {item['item']}. Available: {item['quantity']}, Requested: {quantity}."
                    )
        raise ValueError(f"Item {item_name} not found in stock.")

    def remove_from_cart(self, item_name: str, quantity: int):
        if item_name in self.cart:
            if self.cart[item_name]["quantity"] >= quantity:
                self.cart[item_name]["quantity"] -= quantity
                if self.cart[item_name]["quantity"] == 0:
                    del self.cart[item_name]
                return True
            else:
                raise ValueError(
                    f"Cannot remove {quantity} of {item_name}, only {self.cart[item_name]['quantity']} in cart."
                )
        raise ValueError(f"Item {item_name} not found in your cart.")

    def checkout(self):
        if not self.cart:
            raise ValueError(
                "Your shopping cart is empty. Please add items before checking out."
            )

        total_amount = sum(
            details["quantity"] * details["price"] for details in self.cart.values()
        )

        checked_out_items = self.cart.copy()

        # Update stock quantities
        for item_name, details in self.cart.items():
            for item in self.stocks:
                if item["item"].lower() == item_name.lower():
                    item["quantity"] = item["quantity"] - details["quantity"]
                    break

        # Clear the cart after checkout
        self.cart.clear()

        return {
            "total_amount": total_amount,
            "items": checked_out_items,
        }
