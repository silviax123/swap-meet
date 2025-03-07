class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def get_by_category(self, category):
        return list(filter(lambda item: item.category == category, self.inventory))

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.remove(my_item)
        self.add(their_item)
        other_vendor.remove(their_item)
        other_vendor.add(my_item)
        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        my_first_item = self.inventory[0]
        other_first_item = other_vendor.inventory[0]

        self.remove(my_first_item)
        self.add(other_first_item)
        other_vendor.remove(other_first_item)
        other_vendor.add(my_first_item)
        return True

    def get_best_by_category(self, category):
        category = self.get_by_category(category)
        if category:
            return max(category, key=lambda item: item.condition)

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        if not my_best_item or not their_best_item:
            return False

        self.swap_items(other, my_best_item, their_best_item)
        return True
