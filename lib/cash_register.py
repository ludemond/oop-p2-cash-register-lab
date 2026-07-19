#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

        if not isinstance(self.discount, int):
            print("Not valid discount")
            self.discount = 0
        elif self.discount < 0 or self.discount > 100:
            print("Not valid discount")
            self.discount = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.previous_transactions.append(
            {"item": title, "price": price, "quantity": quantity}
        )

    def apply_discount(self):
        if self.discount == 0 or not self.previous_transactions:
            print("There is no discount to apply.")
            return

        self.total *= (1 - (self.discount / 100))
        print(f"After the discount, the total comes to ${self._format_currency(self.total)}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction["price"] * last_transaction["quantity"]
        self.items = self.items[:-last_transaction["quantity"]]

    def _format_currency(self, value):
        return f"{value:.2f}".rstrip("0").rstrip(".")
