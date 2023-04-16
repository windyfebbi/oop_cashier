# -*- coding: utf-8 -*-
"""cashier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14qhhJsjPEC5mkGHEPYLNQHSaF1y4P7EC
"""

'''
This module are contains some method to execute 
the self-cashier program in module main.py
'''

#import library needed
import pandas as pd
from tabulate import tabulate

class Transaction:

  #initialize class transaction
  def __init__(self):
    self.order = {}

  '''
  This method below used for adding items activities which contains 
  item_name, item_qty, and item_price
  '''  
  def add_item(self):

    #looping input for adding item
    while True:
      try:
        item_name = str.upper(input('Please type the item name: '))
        item_qty = int(input('Many quantity you want to order: '))
        item_price = int(input('Scan the barcode or type the price: Rp'))

        #make sure the input is correct
        if item_qty <= 0:
          raise ValueError("Input wrong! Quantity can't be and less than zero")
        elif item_price <= 0:
          raise ValueError("Input wrong! Price can't be and less than zero")
        
        self.order[item_name] = {
            'Qty' : item_qty, 
            'Price' : item_price, 
            'Total': item_qty*item_price
            }
        print('Item successfully added!')

        #add_item again or no
        while True:
          yn = str.upper(input('Do you want to add another item? Type Y/N only: '))
          if yn == 'Y':
            break
          elif yn == 'N':
            print('Okay!')
            return
          else:
            continue
      except Exception as e:
        print(e)

  '''
  This method below used for updating items activities 
  including item name, quantity and price
  '''
  def update_item(self):
    while True:
      update = str.upper(input("For updating item_name type N, for item_qty type Q, and for item_price type P: "))
      
      #update item_name
      if update == 'N':
        try:
          #check the item name first 
          item_name = str.upper(input('Type item name you want to update: '))
          #when item name is exist on the list of self order
          if item_name in self.order:
            update_name = str.upper(input('Type new item name: '))
            self.order[update_name] = self.order.pop(item_name)
            print(f'{item_name} successfully changed to {update_name}')
          else:
            raise NameError
        except NameError:
          print(f'{item_name} not on your list. Check the input once more')
          continue

      #update item_qty
      elif update == 'Q':
        try:
          #check the item name first
          item_name = str.upper(input('Type item name you want to update: '))
          #when item name is exist on the list of self order
          if item_name in self.order:
            new_qty = int(input('New quantity you want to order: '))
            self.order[new_qty] = self.order.pop(item_qty)
            if new_qty > 0:
              print(f'{item_qty} successfully changed to {new_qty}')
            else:
              raise ValueError
          else:
            raise NameError
        except NameError:
          print(f'{item_name} not on your list. Check your input once more')
        except ValueError:
          print(f'Quantity should be more than zero. Please enter quantity correctly!')

      #update item_price
      elif update == 'P':
        try:
          #check the item name first
          item_name = str.upper(input('Type item name you want to update: '))
          #when item name is exist on the list of self order
          if item_name in self.order:
            new_price = int(input('Enter new correct price: Rp'))
            self.order[new_price] = self.order.pop(item_price)
            if new_price > 0:
              print(f'{item_price} successfully changed to {new_price}')
            else:
              raise ValueError
          else:
            raise NameError
        except NameError:
          print(f'{item_name} not on your list. Check your input once more')
        except ValueError:
          print(f'Price should be more than zero. Please input price correctly!')
      
      else:
        continue
      
      #update_item again or no
      while True:
        yn = str.upper(input('Do you want to update another item? Type Y/N only: '))
        if yn == 'Y':
          break
        elif yn == 'N':
          print('Okay')
          return
        else:
          continue

  '''
  This method below used for deleting item in chart including 
  item name, quantity and price using item's name
  '''
  def delete_item(self):
    while True:
      try:
        #check the item name first
        item_name = str.upper(input('Type item name you want to delete: '))
        #when item name is exist on self order dict
        if item_name in self.order:
          self.order.pop(item_name)
          yn = str.upper(input(f'Are you sure want to delete {item_name}? Confirm by type Y/N: '))
          if yn == 'Y':
            print(f'{item_name} successfully deleted')
            pass
          elif yn == 'N':
            print(f'{item_name} canceled deleted')
          else:
            print('Type yes or no correctly!')
      
          #delete_item again or no
          while True:
            yn = str.upper(input('Do you want to delete another item? Type Y/N only: '))
            if yn == 'Y':
              break
            elif yn == 'N':
              print('Okay')
              return
            else:
              continue
      except ValueError:
        print(f'{item_name} not on your list. Check the input once more')

  '''
  This method below used for reset all transaction in self.order dict including
  item name, quantity and price. There's also option to make new transaction
  '''
  def reset_trnsct(self):
    while True:
      try:
        if len(self.order) != 0:
          self.order.clear()
          yn = str.upper(input(f'Are you sure want to reset all transaction? Confirm by type Y/N: '))
          if yn == 'Y':
            print('Your transaction has been canceled')
            yn = str.upper(input('Want to create new transaction? Confirm by type Y/N: '))
            if yn == 'Y':
              self.add_item()
              break
            elif yn == 'N':
              break
            else:
              print('Type yes or no correctly!')
          else:
            print('Enjoy your shopping!')
        else:
          #when there's no item added to dict
          raise ValueError
      except ValueError:
        print('Your cart is empty! Add some items first to start shopping')

  '''
  This method below used for display list of transaction in self.order dict 
  including item name, quantity, and total price with table form
  '''
  def check_order(self):
    #display list transaction
    if self.order == {}:
      print('Your cart still empty! Add some items first')
    else:
      tabel = pd.DataFrame(self.order).T
      headers = ['ITEM', 'QTY', 'PRICE', 'TOTAL']
      print(tabulate(tabel, headers= headers, tablefmt='fancy_grid'))

  '''
  This method below used for calculate total price from list of transaction 
  in self.order dict including discount requirements
  '''
  def checkout(self):
    if self.order == {}:
      print('Your cart still empty! Add some items first')
    else:
      tabel = pd.DataFrame(self.order).T
      headers = ['ITEM', 'QTY', 'PRICE', 'TOTAL']
      print(tabulate(tabel, headers= headers, tablefmt='fancy_grid'))
    
    total_price = 0
    for item in self.order:
      total_price += self.order[item]['Total']

    #discount requirements
    if 200000 < total_price <= 300000:
      final_price = total_price * 0.95
      print(f'Congratulations! You got discount 5%. Your total payment is Rp{final_price}')
    elif 300000 < total_price <= 500000:
      final_price = total_price * 0.92
      print(f'Congratulations! You got discount 8*%. Your total payment is Rp{final_price}')
    elif total_price > 500000:
      final_price = total_price * 0.90
      print(f'Congratulations! You got discount 8*%. Your total payment is Rp{final_price}')
    else: 
      total_price = total_price
      print(f'Your total payment is Rp{total_price}')

  '''
  This method below used for to do payment from list of transaction 
  in self.order dict including discount requirements
  '''
  def payment(self):
    print('Please choose payment below')
    pay = str.upper(input('Type A for QR Code and B for Debit/Credit: '))
    if pay == 'A':
      print('Please scan the code below')
      print('Thank you for your payment! Have a nice day')
    elif pay == 'B':
      print('Insert your card below')
      print('Thank you for your payment! Have a nice day')
    else:
      print('Type it correctly')