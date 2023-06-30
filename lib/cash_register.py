#!/usr/bin/env python3


class CashRegister:
  
  def __init__(self, discount= 0):
    self.discount  = discount
    self.total = 0
    self.items = []
    self.last_transaction = 0

  def add_item(self, item, price, quantity = 1):
    self.last_transaction = price * quantity
    self.total += (price * quantity)
    while quantity >= 1:
      self.items.append(item)
      quantity -= 1

  def apply_discount(self):
    if self.discount != 0:
      decimal_discount = self.discount / 100
      amount_discount = self.total * decimal_discount
      self.total -= amount_discount
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
  
  def void_last_transaction(self):
    self.total -= self.last_transaction