
# Sweet Shop Management System - All-in-One

class Sweet:
    def __init__(self, sweet_id, name, category, price, quantity):
        self.id = sweet_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name} ({self.category}) - Rs.{self.price}, Qty: {self.quantity}"

class SweetShop:
    def __init__(self):
        self.sweets = {}

    def add_sweet(self, sweet):
        if sweet.id in self.sweets:
            raise ValueError("Sweet ID already exists.")
        self.sweets[sweet.id] = sweet

    def delete_sweet(self, sweet_id):
        if sweet_id in self.sweets:
            del self.sweets[sweet_id]
        else:
            raise ValueError("Sweet ID not found.")

    def view_sweets(self):
        return list(self.sweets.values())

    def search_by_name(self, name):
        return [s for s in self.sweets.values() if name.lower() in s.name.lower()]

    def search_by_category(self, category):
        return [s for s in self.sweets.values() if category.lower() == s.category.lower()]

    def search_by_price_range(self, low, high):
        return [s for s in self.sweets.values() if low <= s.price <= high]

    def purchase_sweet(self, sweet_id, qty):
        if sweet_id not in self.sweets:
            raise ValueError("Sweet not found.")
        if self.sweets[sweet_id].quantity < qty:
            raise ValueError("Insufficient stock.")
        self.sweets[sweet_id].quantity -= qty

    def restock_sweet(self, sweet_id, qty):
        if sweet_id not in self.sweets:
            raise ValueError("Sweet not found.")
        self.sweets[sweet_id].quantity += qty

# -----------------------------
# Manual Testing (Sample Usage)
# -----------------------------
if __name__ == "__main__":
    shop = SweetShop()

    # Add some sweets
    shop.add_sweet(Sweet(101, "Kaju Katli", "Dryfruit", 50, 25))
    shop.add_sweet(Sweet(102, "Gulab Jamun", "Milk", 15, 40))

    # View all sweets
    print("All sweets:")
    for sweet in shop.view_sweets():
        print(sweet)

    # Purchase sweet
    shop.purchase_sweet(101, 5)
    print("\nAfter purchasing 5 Kaju Katli:")
    print(shop.sweets[101])

    # Restock sweet
    shop.restock_sweet(102, 10)
    print("\nAfter restocking 10 Gulab Jamun:")
    print(shop.sweets[102])

    # Search examples
    print("\nSearch by name 'gulab':", shop.search_by_name("gulab"))
    print("Search by category 'Milk':", shop.search_by_category("Milk"))
    print("Search by price range 10–20:", shop.search_by_price_range(10, 20))
