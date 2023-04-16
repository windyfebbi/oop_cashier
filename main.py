# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cidZQ6ZpvHOZwzhe4DRrsbK_5FIubYkB
"""

from google.colab import files

!cp /content/drive/MyDrive/Colab\ Notebooks/cashier.py /content

import cashier as c

#test case 1: add item
wforder = c.Transaction()
wforder.add_item()

#test case 2: delete item
wforder.delete_item()

#test case 3: update item
wforder.update_item()

#test case 4: reset transaction
wforder.reset_trnsct()

#test case 5: check order
wforder.check_order()

#test case 6: checkout (inc total order)
wforder.checkout()

#test case 7: payment option
wforder.payment()
