#!/usr/bin/env/ Python3

from os import system

def printItems( items, title = None ):

 system( "clear" )
 print( "#"*30 )
 print( title ) 
 print( "#"*30 )
 for i in range( len( items ) ):
     print(
     f"{i + 1:2} {items[i]['name']:15} {items[i]['price']['amount']:7.2f} { items[i]['price']['currency']} "
 )
 print( "#"*30 )
