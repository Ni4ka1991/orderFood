#!/usr/bin/env python3

# app.py

# MAIN MODULE #######

from db import *
from restaurant import *

food = load( 'food')
order = {
  "items": [],
#  "total": {# = 0
#      "amount": 0, #all food in order * quantity
#      "currency": "MDL"
      
#      },
  

}


while True:
 action = printActionsMenu(
    [
       "Show food",
       "Order food",
       "Show order ",
       "Checkout",
       "Exit"
    ],
    "MAIN MENU" 
 )
 if( action == 1 ):
   printItems( food, "TODAYS MENU" )
 
 if( action == 2 ):
   printItems( food, "TODAYS MENU" )
   item_i = int( input( "Which item? >>> " )) - 1
   item_q = int( input( f"How many < {food[item_i]['name']} > do you want? >>> " ))
   order["items"].append(
           createOrderItem( food, item_i, item_q )
        )
   #order["total"].append( "amount" : food[item_i]['name']['price'])
 if( action == 3):
#if order["items "] != "":
   printItems( order["items"], "YOUR ORDER" )
#else:
#print( "Empty list" )
   
    

 if( action == 5 ):
   break

