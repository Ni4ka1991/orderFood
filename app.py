#!/usr/bin/env Python3

# app.py

# MAIN MODULE #######

import json
from os import system


file = open( "./data/food.json", "r" )

data = json.loads( file.read() )


system( "clear" )

for i in range( len(data) ):
 print( f"{i + 1:2} {data[i]["name"]:15} {data[i]["price"]["amount"]:7.2} { data[i]}["price"]["currency"]} " )

