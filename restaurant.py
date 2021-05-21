#!/usr/bin/env/ Python3

from os import system

def printItems( items, title = None ):#showQuantity = False
 
 system( "clear" )

 if( title != None ):
  print( "#" * 42 )
  print( f" {title}" ) 
 print( "#" * 42 )
 print( f" nr. name               price per serving" )
 print( "#" * 42 )
 for i in range( len( items ) ):
     print(
     f"{i + 1:3} {items[i]['name']:25} {items[i]['price']['amount']:7.2f} { items[i]['price']['currency']} "#{ items x 2}
  )
 print( "#" * 42 )
 input( "hit ENTER to continue ..." )


def printActionsMenu( items, title = None ):
 
 system( "clear" )
 if( title != None ):
  print( "#" * 20 )
  print( title ) 
 print( "#" * 20 )
 for i in range( len( items ) ):
     print(
     f"{i + 1:2} {items[i]} "
  )
 print( "#" * 20 )
 
 option = int( input( " Select menu item >>> " ))
 return option


def createOrderItem( food, item_i, item_q ):
  
  return {
    "name":food[item_i]['name'],
    "quantity":item_q,
    "price":{
      "amount": item_q * food[item_i]['price']['amount'],
      "currency": "MDL"
    }    
  }






